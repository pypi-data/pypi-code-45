from collections import OrderedDict
import numpy as np
import spacy  # NLP library that analyses text to extract keywords
from spacy.lang.en.stop_words import STOP_WORDS

from keyword_text_analyser.text_analyse_utils import sentence_segment, get_token_pairs, get_vocab, get_matrix

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe(nlp.create_pipe('sentencizer'), first=True)

custom_stopwords = ['use']
stopwords = STOP_WORDS.union(set(custom_stopwords))

window_size = 4
candidate_pos = ['NOUN', 'PROPN']


def set_stopwords():
    """Set stop words"""
    for word in stopwords:
        lexeme = nlp.vocab[word]
        lexeme.is_stop = True


class TextRank4Keyword:
    """Extract keywords from text """

    def __init__(self):
        # Set stop words
        set_stopwords()
        self.d = 0.85  # damping coefficient, usually is .85
        self.min_diff = 1e-5  # convergence threshold
        self.steps = 10  # iteration steps
        self.node_weight = None  # save keywords and its weight

    def get_keywords(self, number=3):
        """Print top number keywords"""
        node_weight = OrderedDict(sorted(self.node_weight.items(), key=lambda t: t[1], reverse=True))
        keywords = ''
        for i, (key, value) in enumerate(node_weight.items()):
            # print(key + ' - ' + str(value))
            keywords += key + ' '
            if i > number:
                break
        return keywords[:-1]

    def analyze(self, text):
        """Main function to analyze text"""

        # Parse text by spaCy
        doc = nlp(text)

        # Filter sentences
        sentences = sentence_segment(doc, candidate_pos)  # list of list of words

        # Build vocabulary
        vocab = get_vocab(sentences)

        # Get token_pairs from windows
        token_pairs = get_token_pairs(window_size, sentences)

        # Get normalized matrix
        normalized_matrix = get_matrix(vocab, token_pairs)

        # Initialization for weight(Page Rank value)
        pr = np.array([1] * len(vocab))

        # Iteration
        previous_pr = 0
        for epoch in range(self.steps):
            pr = (1 - self.d) + self.d * np.dot(normalized_matrix, pr)
            if abs(previous_pr - sum(pr)) < self.min_diff:
                break
            else:
                previous_pr = sum(pr)

        # Get weight for each node
        node_weight = dict()
        for word, index in vocab.items():
            node_weight[word] = pr[index]

        self.node_weight = node_weight
