from .forest import Forest
from . import tokenizer


def view_table():
    raise NotImplementedError


def view_tree():
    raise NotImplementedError


def reconstruct_source(stream: bytes) -> str:
    return tokenizer.reconstruct_source(
        tokenizer.TokenStream.from_forest(
            Forest.from_stream(stream)))
