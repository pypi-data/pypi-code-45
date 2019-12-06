import typing
from collections import Counter
from typing import Union

if typing.TYPE_CHECKING:
    from tokenizer_tools.tagset.offset.corpus import Corpus


class CorpusStatistics:
    def __init__(
        self,
        domain: Union[Counter, None] = None,
        function: Union[Counter, None] = None,
        sub_function: Union[Counter, None] = None,
        intent: Union[Counter, None] = None,
        entity_types: Union[Counter, None] = None,
        entity_values: Union[Counter, None] = None,
    ):
        self.domain: Union[Counter, None] = domain
        self.function: Union[Counter, None] = function
        self.sub_function: Union[Counter, None] = sub_function
        self.intent: Union[Counter, None] = intent
        self.entity_types: Union[Counter, None] = entity_types
        self.entity_values: Union[Counter, None] = entity_values

    @classmethod
    def create_from_corpus(cls, corpus: "Corpus") -> "CorpusStatistics":
        domain = cls._collect_domain(corpus)
        function = cls._collect_function(corpus)
        sub_function = cls._collect_sub_function(corpus)
        intent = cls._collect_intent(corpus)
        entity_types = cls._collect_entity_types(corpus)
        entity_values = cls._collect_entity_values(corpus)

        return cls(domain, function, sub_function, intent, entity_types, entity_values)

    @classmethod
    def _collect_domain(cls, corpus: "Corpus") -> Counter:
        domain_list = [doc.domain for doc in corpus]
        return Counter(domain_list)

    @classmethod
    def _collect_function(cls, corpus: "Corpus") -> Counter:
        function_list = [doc.function for doc in corpus]
        return Counter(function_list)

    @classmethod
    def _collect_sub_function(cls, corpus: "Corpus") -> Counter:
        sub_function_list = [doc.sub_function for doc in corpus]
        return Counter(sub_function_list)

    @classmethod
    def _collect_intent(cls, corpus: "Corpus") -> Counter:
        intent_list = [doc.intent for doc in corpus]
        return Counter(intent_list)

    @classmethod
    def _collect_entity_types(cls, corpus: "Corpus") -> Counter:
        entities_list = [span.entity for doc in corpus for span in doc.entities]
        return Counter(entities_list)

    @classmethod
    def _collect_entity_values(cls, corpus: "Corpus") -> Counter:
        # TODO: wait for auto entity value binding with text feature
        pass

    def __eq__(self, other):
        pass
