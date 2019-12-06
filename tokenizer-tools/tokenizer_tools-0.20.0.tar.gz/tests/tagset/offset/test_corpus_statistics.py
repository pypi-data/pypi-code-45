from collections import Counter

from tokenizer_tools.tagset.offset.corpus import Corpus
from tokenizer_tools.tagset.offset.corpus_statistics import CorpusStatistics
import pytest


@pytest.mark.skip(reason="not implemented yet")
def test_create_from_corpus(datadir):
    corpus = Corpus.read_from_file(datadir / "data.conllx")

    corpus_statistics = CorpusStatistics.create_from_corpus(corpus)

    expected = CorpusStatistics(
        domain=None,
        function=None,
        sub_function=None,
        intent=None,
        entity_types=None,
        entity_values=None,
    )

    assert corpus_statistics == expected


def test_collect_domain(datadir):
    corpus = Corpus.read_from_file(datadir / "data.conllx")

    corpus_statistics = CorpusStatistics.create_from_corpus(corpus)

    result = corpus_statistics.domain

    expected = Counter({'domain_one': 2, 'domain_two': 2})

    assert result == expected


def test_collect_function(datadir):
    corpus = Corpus.read_from_file(datadir / "data.conllx")

    corpus_statistics = CorpusStatistics.create_from_corpus(corpus)

    result = corpus_statistics.function

    expected = Counter({'function_one': 2, 'function_two': 2})

    assert result == expected


def test_collect_sub_function(datadir):
    corpus = Corpus.read_from_file(datadir / "data.conllx")

    corpus_statistics = CorpusStatistics.create_from_corpus(corpus)

    result = corpus_statistics.sub_function

    expected = Counter({'sub_function_one': 2, 'sub_function_two': 2})

    assert result == expected


def test_collect_intent(datadir):
    corpus = Corpus.read_from_file(datadir / "data.conllx")

    corpus_statistics = CorpusStatistics.create_from_corpus(corpus)

    result = corpus_statistics.intent

    expected = Counter({'intent_one': 2, 'intent_two': 2})

    assert result == expected
