from collections import OrderedDict
import numpy as np


def sentence_segment(doc, candidate_pos):
    """Store those words only in cadidate_pos"""
    sentences = []
    for sent in doc.sents:
        selected_words = []
        for token in sent:
            # Store words only with cadidate POS tag
            if token.pos_ in candidate_pos and token.is_stop is False and len(token.text) > 1:
                selected_words.append(token.text.lower())
        sentences.append(selected_words)
    return sentences


def get_vocab(sentences):
    """Get all tokens"""
    vocab = OrderedDict()
    i = 0
    for sentence in sentences:
        for word in sentence:
            if word not in vocab:
                vocab[word] = i
                i += 1
    return vocab


def get_token_pairs(window_size, sentences):
    """Build token_pairs from windows in sentences"""
    token_pairs = list()
    for sentence in sentences:
        for i, word in enumerate(sentence):
            for j in range(i + 1, i + window_size):
                if j >= len(sentence):
                    break
                pair = (word, sentence[j])
                if pair not in token_pairs:
                    token_pairs.append(pair)
    return token_pairs


def symmetrize(a):
    return a + a.T - np.diag(a.diagonal())


def get_matrix(vocab, token_pairs):
    """Get normalized matrix"""
    # Build matrix
    vocab_size = len(vocab)
    g = np.zeros((vocab_size, vocab_size), dtype='float')
    for word1, word2 in token_pairs:
        i, j = vocab[word1], vocab[word2]
        g[i][j] = 1

    # Get Symmetric matrix
    g = symmetrize(g)

    # Normalize matrix by column
    norm = np.sum(g, axis=0)
    g_norm = np.divide(g, norm, where=norm != 0)  # this is ignore the 0 element in norm

    return g_norm
