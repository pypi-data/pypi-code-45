from typing import Optional
from .tokenizer import Tokenizer


def compile_source(
        source_str: str,
        allow_unquoted_strings: bool = False,
        prefix: Optional[str] = None) -> bytes:
    return Tokenizer(source_str, allow_unquoted_strings, prefix)\
        .tokenize()\
        .validate()\
        .build_forest()\
        .serialize_to_stream()
