"""
experimenting with increasingly general notions of indexing
"""
from relativity import M2M


class IndexedTriple(object):
	"""
	keeps track of "left" to "right" pairs
	"""
	def __init__(self):
		self.left, self.right = M2M(), M2M()
		self.pair_counts = {}

	def addleft(self, left, mid):
		self.left.add(left, mid)
		self._inc_pairs((left,), self.right.get(mid))

	def removeleft(self, left, mid):
		self.left.remove(left, mid)
		self._dec_pairs((left,), self.right.get(mid))

	def addright(self, mid, right):
		self.right.add(mid, right)
		self._inc_pairs(self.left.inv.get(mid), (right,))

	def removeright(self, mid, right):
		self.right.remove(mid, right)
		self._dec_pairs(self.left.inv.get(mid), (right,))

	def __contains__(self, pair):
		return pair in self.pair_counts

	def _inc_pairs(self, lefts, rights):
		for left in lefts:
			for right in rights:
				pair = (left, right)
				if pair not in pair_counts:
					self.pair_counts[pair] = 1
				else:
					self.pair_counts[pair] += 1

	def _dec_pairs(self, lefts, rights):
		for left in lefts:
			for right in rights:
				pair = (left, right)
				if self.pair_counts[pair] == 1:
					del self.pair_counts[pair]
				else:
					self.pair_counts[pair] -= 1
