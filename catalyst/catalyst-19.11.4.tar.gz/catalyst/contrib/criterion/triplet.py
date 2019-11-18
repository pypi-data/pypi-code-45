import torch
import torch.nn as nn


class TripletLoss(nn.Module):
    """
    Triplet loss with hard positive/negative mining.
    Reference:
    Code imported from https://github.com/NegatioN/OnlineMiningTripletLoss.
    Args:
        margin (float): margin for triplet.
    """

    def __init__(self, margin=0.3):
        """
        Constructor method for the TripletLoss class.
        Args:
            margin: margin parameter.
        """
        super(TripletLoss, self).__init__()
        self.margin = margin
        self.ranking_loss = nn.MarginRankingLoss(margin=margin)

    def _pairwise_distances(self, embeddings, squared=False):
        """
        Compute the 2D matrix of distances between all the embeddings.
        Args:
            embeddings: tensor of shape (batch_size, embed_dim)
            squared: Boolean. If true, output is the pairwise
                     squared euclidean distance matrix. If false, output
                     is the pairwise euclidean distance matrix.
        Returns:
            pairwise_distances: tensor of shape (batch_size, batch_size)
        """
        # Get squared L2 norm for each embedding.
        # We can just take the diagonal of `dot_product`.
        # This also provides more numerical stability
        # (the diagonal of the result will be exactly 0).
        # shape (batch_size,)
        square = torch.mm(embeddings, embeddings.t())
        diag = torch.diag(square)

        # Compute the pairwise distance matrix as we have:
        # ||a - b||^2 = ||a||^2  - 2 <a, b> + ||b||^2
        # shape (batch_size, batch_size)
        distances = diag.view(-1, 1) - 2.0 * square + diag.view(1, -1)

        # Because of computation errors, some distances
        # might be negative so we put everything >= 0.0
        distances[distances < 0] = 0

        if not squared:
            # Because the gradient of sqrt is infinite
            # when distances == 0.0 (ex: on the diagonal)
            # we need to add a small epsilon where distances == 0.0
            mask = distances.eq(0).float()
            distances = distances + mask * 1e-16

            distances = (1.0 - mask) * torch.sqrt(distances)

        return distances

    def _get_anchor_positive_triplet_mask(self, labels):
        """
        Return a 2D mask where mask[a, p] is True
        if a and p are distinct and have same label.
        Args:
            labels: tf.int32 `Tensor` with shape [batch_size]
        Returns:
            mask: tf.bool `Tensor` with shape [batch_size, batch_size]
        """
        indices_equal = torch.eye(labels.size(0)).bool()

        # labels and indices should be on
        # the same device, otherwise - exception
        indices_equal = indices_equal.to("cuda" if labels.is_cuda else "cpu")

        # Check that i and j are distinct
        indices_not_equal = ~indices_equal

        # Check if labels[i] == labels[j]
        # Uses broadcasting where the 1st argument
        # has shape (1, batch_size) and the 2nd (batch_size, 1)
        labels_equal = labels.unsqueeze(0) == labels.unsqueeze(1)

        return labels_equal & indices_not_equal

    def _get_anchor_negative_triplet_mask(self, labels):
        """
        Return 2D mask where mask[a, n] is True if a and n have same label.
        Args:
            labels: tf.int32 `Tensor` with shape [batch_size]
        Returns:
            mask: tf.bool `Tensor` with shape [batch_size, batch_size]
        """
        # Check if labels[i] != labels[k]
        # Uses broadcasting where the 1st argument
        # has shape (1, batch_size) and the 2nd (batch_size, 1)
        return ~(labels.unsqueeze(0) == labels.unsqueeze(1))

    def _batch_hard_triplet_loss(
        self,
        embeddings,
        labels,
        margin,
        squared=True,
    ):
        """
        Build the triplet loss over a batch of embeddings.
        For each anchor, we get the hardest positive and
        hardest negative to form a triplet.
        Args:
            labels: labels of the batch, of size (batch_size,)
            embeddings: tensor of shape (batch_size, embed_dim)
            margin: margin for triplet loss
            squared: Boolean. If true, output is the pairwise squared
                     euclidean distance matrix. If false, output is the
                     pairwise euclidean distance matrix.
        Returns:
            triplet_loss: scalar tensor containing the triplet loss
        """
        # Get the pairwise distance matrix
        pairwise_dist = self._pairwise_distances(embeddings, squared=squared)

        # For each anchor, get the hardest positive
        # First, we need to get a mask for every valid
        # positive (they should have same label)
        mask_anchor_positive = self._get_anchor_positive_triplet_mask(
            labels).float()

        # We put to 0 any element where (a, p) is not valid
        # (valid if a != p and label(a) == label(p))
        anchor_positive_dist = mask_anchor_positive * pairwise_dist

        # shape (batch_size, 1)
        hardest_positive_dist, _ = anchor_positive_dist.max(1, keepdim=True)

        # For each anchor, get the hardest negative
        # First, we need to get a mask for every valid negative
        # (they should have different labels)
        mask_anchor_negative = self._get_anchor_negative_triplet_mask(
            labels).float()

        # We add the maximum value in each row
        # to the invalid negatives (label(a) == label(n))
        max_anchor_negative_dist, _ = pairwise_dist.max(1, keepdim=True)
        anchor_negative_dist = pairwise_dist + max_anchor_negative_dist * \
            (1.0 - mask_anchor_negative)

        # shape (batch_size,)
        hardest_negative_dist, _ = anchor_negative_dist.min(1, keepdim=True)

        # Combine biggest d(a, p) and smallest d(a, n) into final triplet loss
        tl = hardest_positive_dist - hardest_negative_dist + margin
        tl[tl < 0] = 0
        triplet_loss = tl.mean()

        return triplet_loss

    def forward(self, embeddings, targets):
        """
        Forward propagation method for the triplet loss.
        Args:
            embeddings: tensor of shape (batch_size, embed_dim)
            targets: labels of the batch, of size (batch_size,)
        Returns:
            triplet_loss: scalar tensor containing the triplet loss
        """
        return self._batch_hard_triplet_loss(embeddings, targets, self.margin)


__all__ = ["TripletLoss"]
