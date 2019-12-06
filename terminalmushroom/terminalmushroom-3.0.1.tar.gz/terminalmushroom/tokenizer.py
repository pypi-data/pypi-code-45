import collections
import enum
from typing import List, Optional, Iterable, Union
import sys
from .structures import Node, Tree, Entity, Literal, Metadata
from .forest import Forest


class TokenType(enum.Enum):
    TREE_BEGIN = 'tree_begin'
    TREE_END = 'tree_end'
    ENTITY_BEGIN = 'entity_begin'
    ENTITY_SET = 'entity_set'
    ENTITY_INCREMENT = 'entity_increment'
    ENTITY_END = 'entity_end'
    METADATA = 'entity_metadata'
    LITERAL = 'literal'

    def __repr__(self):
        return self.name


class TokenStream(collections.UserList):
    """A tokenized representation of a source file."""

    @property
    def _current_token(self) -> str:
        return self[self.index] if self._tokens_remaining else None

    @property
    def _tokens_remaining(self) -> bool:
        return self.index < self.length

    def __init__(self, init: Iterable[Union[TokenType, str, int]]) -> None:
        super(TokenStream, self).__init__(init)
        self.index: int = 0
        self.length: int = len(self)
        self.next_key: int = 0
        self.parse_order = [
            self._try_parse_tree,
            self._try_parse_entity,
            self._try_parse_literal,
            self._try_parse_metadata
        ]

    def reset(self) -> None:
        self.index = 0
        self.next_key = 0

    def build_forest(self) -> Forest:
        self.reset()

        table_index: List[int] = []
        rows: List[Node] = []
        while self._tokens_remaining:
            start_key = self.next_key

            node_rows = self._parse_next_node()
            if not node_rows:
                break

            table_index.append(start_key)
            rows.extend(node_rows)

        return Forest(table_index, rows)

    def validate(self) -> 'TokenStream':
        depth = 0
        node_has_content = False
        inside_entity = False
        index = 0
        length = len(self)

        while index < length:
            try:
                token = self[index]
                index += 1

                if token is TokenType.TREE_BEGIN:
                    assert not inside_entity, \
                        'Token Stream Verification: Non-entity token ' \
                        'within entity block.'
                    depth += 1
                    node_has_content = False
                    identifier = self[index]
                    index += 1
                    assert isinstance(identifier, str), \
                        'Token Stream Verification: Expected identifier ' \
                        'after node begin.'
                    validate_identifier(identifier)

                elif token is TokenType.TREE_END:
                    assert not inside_entity, \
                        'Token Stream Verification: Non-entity token ' \
                        'within entity block.'
                    depth -= 1
                    assert depth >= 0, \
                        'Token Stream Verification: Unexpected node end.'
                    assert node_has_content, \
                        'Token Stream Verification: Empty nodes are not ' \
                        'permitted.'

                elif token is TokenType.ENTITY_BEGIN:
                    assert not inside_entity, \
                        'Token Stream Verification: Unexpected entity begin.'
                    node_has_content = True
                    inside_entity = True
                    identifier = self[index]
                    index += 1
                    assert isinstance(identifier, str), \
                        'Token Stream Verification: Expected identifier ' \
                        'after entity begin.'
                    validate_identifier(identifier)

                elif token is TokenType.ENTITY_SET:
                    assert inside_entity, \
                        'Token Stream Verification: Entity set outside ' \
                        'of entity block.'
                    amount = self[index]
                    index += 1
                    assert isinstance(amount, int), \
                        'Token Stream Verification: Expected amount ' \
                        'after entity set.'

                elif token is TokenType.ENTITY_INCREMENT:
                    assert inside_entity, \
                        'Token Stream Verification: Entity increment ' \
                        'outside of entity block.'
                    amount = self[index]
                    index += 1
                    assert isinstance(amount, int), \
                        'Token Stream Verification: Expected amount ' \
                        'after entity increment.'

                elif token is TokenType.ENTITY_END:
                    assert inside_entity, \
                        'Token Stream Verification: Unexpected entity end.'
                    inside_entity = False

                elif token is TokenType.LITERAL:
                    node_has_content = True
                    literal = self[index]
                    index += 1
                    assert isinstance(literal, str), \
                        'Token Stream Verification: Expected string ' \
                        'after literal marker.'

                elif token is TokenType.METADATA:
                    node_has_content = True
                    identifier = self[index]
                    index += 1
                    assert isinstance(identifier, str), \
                        'Token Stream Verification: Expected identifier ' \
                        'after metadata tag.'
                    validate_identifier(identifier)

                elif isinstance(token, str):
                    raise AssertionError('Token Stream Verification: '
                                         'Expected token; got a string.')
                elif isinstance(token, int):
                    raise AssertionError('Token Stream Verification: '
                                         'Expected token; got an int.')
                else:
                    raise AssertionError('Token Stream Verification: '
                                         'Got an unexpected item.')

            except IndexError:
                raise AssertionError('Token Stream Verification: '
                                     'Stream ended too early.')

        assert depth == 0, \
            'Token Stream Verification: Depth was not zero at stream end.'

        return self

    @classmethod
    def from_forest(cls, forest: Forest) -> 'TokenStream':
        result = []
        stack = []
        for key, node in enumerate(forest.nodes):
            if isinstance(node, Tree):
                result.extend([TokenType.TREE_BEGIN, node.identifier])
                stack.append(node.branches[-1])

            elif isinstance(node, Entity):
                result.extend([TokenType.ENTITY_BEGIN, node.identifier])
                if node.alias:
                    result.extend([TokenType.LITERAL, node.alias])

                if node.count_type is Entity.CountType.INCREMENT and node.count != 1:
                    result.extend([TokenType.ENTITY_INCREMENT, node.count])
                elif node.count_type is Entity.CountType.SET:
                    result.extend([TokenType.ENTITY_SET, node.count])

                result.append(TokenType.ENTITY_END)

            elif isinstance(node, Literal):
                result.extend([TokenType.LITERAL, node.identifier])

            elif isinstance(node, Metadata):
                result.extend([TokenType.METADATA, node.identifier])

            else:
                raise RuntimeError('Unknown node type: {0}'.format(node.__class__.__name__))

            while stack and stack[-1] <= key:
                stack.pop()
                result.append(TokenType.TREE_END)

        return cls(result)

    def _parse_next_node(self) -> List[Node]:
        if not self._tokens_remaining:
            return []

        for parser in self.parse_order:
            rows = parser()
            if rows:
                return rows
        else:
            raise RuntimeError('Could not parse node in token string. Index: {}'.format(self.index))

    def _try_parse_tree(self) -> List[Node]:
        if not self._tokens_remaining or self._current_token is not TokenType.TREE_BEGIN:
            return []
        self.index += 1

        identifier = self._current_token
        self.index += 1

        tree = Tree(self.next_key, identifier)
        self.next_key += 1

        result = [tree]
        while self._current_token is not TokenType.TREE_END:
            rows = self._parse_next_node()
            if rows:
                result.extend(rows)
                tree.branches.append(rows[0].key)
        self.index += 1

        return result

    def _try_parse_literal(self) -> List[Literal]:
        if not self._tokens_remaining or self._current_token is not TokenType.LITERAL:
            return []
        self.index += 1

        identifier = self._current_token
        self.index += 1

        literal = Literal(self.next_key, identifier)
        self.next_key += 1

        return [literal]

    def _try_parse_entity(self) -> List[Entity]:
        if not self._tokens_remaining or self._current_token is not TokenType.ENTITY_BEGIN:
            return []
        self.index += 1

        identifier = self._current_token
        self.index += 1

        entity = Entity(self.next_key, identifier)
        self.next_key += 1

        while self._current_token is not TokenType.ENTITY_END:
            token = self._current_token
            self.index += 1

            if token is TokenType.LITERAL:
                entity.alias = self._current_token
            elif token is TokenType.ENTITY_INCREMENT:
                entity.count_type = Entity.CountType.INCREMENT
                entity.count = self._current_token
            elif token is TokenType.ENTITY_SET:
                entity.count_type = Entity.CountType.SET
                entity.count = self._current_token
            self.index += 1

        self.index += 1

        return [entity]

    def _try_parse_metadata(self) -> List[Metadata]:
        if not self._tokens_remaining or self._current_token is not TokenType.METADATA:
            return []
        self.index += 1

        identifier = self._current_token
        self.index += 1

        metadata = Metadata(self.next_key, identifier)
        self.next_key += 1

        return [metadata]


class Tokenizer(object):
    """Creates token streams from raw text input."""

    WHITESPACE = ' \t\n\r,'
    QUOTE = '\'"'
    TREE_BEGIN = '('
    TREE_END = ')'
    ENTITY_TAG = '@'
    ENTITY_ALIAS = ':'
    ENTITY_INCREMENT = '+'
    ENTITY_DECREMENT = '-'
    ENTITY_SET = '='
    METADATA_TAG = '#'
    SINGLE_LINE_COMMENT = '//'
    MULTI_LINE_COMMENT_START = '/*'
    MULTI_LINE_COMMENT_END = '*/'
    IDENTIFIER_ALLOWED = '._'

    @property
    def _current_character(self) -> str:
        return self.string[self.index] if self._characters_remaining else None

    @property
    def _characters_remaining(self) -> bool:
        return self.index < self.length

    def __init__(self, string: str, allow_unquoted_strings: bool = False, prefix: str = None):
        self.string: str = string
        self.allow_unquoted_strings: bool = allow_unquoted_strings
        self.prefix: str = prefix
        self.lines: List[str] = self.string.splitlines()
        self.index: int = 0
        self.length: int = len(string)
        self.line_number: int = 0
        self.line_start_index: int = 0
        self.parse_order = [
            self._try_parse_node_begin,
            self._try_parse_node_end,
            self._try_parse_entity_tag,
            self._try_parse_meta,
            self._try_parse_string,
        ]

    def reset(self) -> None:
        self.index = 0
        self.length = len(self.string)
        self.line_number = 0
        self.line_start_index = 0

    def tokenize(self) -> TokenStream:
        self.reset()
        result = []

        while self._characters_remaining:
            self._consume_whitespace()

            if self._consume_single_line_comment():
                continue

            if self._consume_multi_line_comment():
                continue

            for parser in self.parse_order:
                tokens = parser()
                if tokens:
                    result.extend(tokens)
                    break
            else:
                if (self._consume_entity_alias() is not None or
                        self._consume_entity_increment_decrement() is not None or
                        self._consume_entity_set() is not None):
                    self._warn('Tokenize: Found an entity modifier without '
                               'an associated entity; ignoring')
                    continue

                if self._consume_identifier() is not None:
                    self._warn('Tokenize: Found an identifier that does not '
                               'begin a node; did you mean to use a string literal?')
                    continue

                if self._characters_remaining:
                    self._warn('Tokenize: Failed to parse {}; ignoring'.format(
                        repr(self._current_character)))
                    self.index += 1

        return TokenStream(result)

    def _try_parse_meta(self) -> Optional[list]:
        if not self._characters_remaining:
            return None

        # Check for tag start
        if self._current_character not in self.METADATA_TAG:
            return None

        self.index += 1

        self._consume_whitespace()

        meta = self._consume_identifier()
        if meta is None:
            self._error('Metadata tag must be followed by a valid identifier.')

        return [TokenType.METADATA, meta]

    def _try_parse_string(self) -> Optional[list]:
        if self.allow_unquoted_strings:
            literal = self._consume_string()
        else:
            literal = self._consume_quoted_string_literal()

        if literal is not None:
            return [TokenType.LITERAL, literal]

        return None

    def _try_parse_node_begin(self) -> Optional[list]:
        if not self._characters_remaining:
            return None

        start_index = self.index

        identifier = self._consume_identifier()
        if identifier is None:
            return None

        self._consume_whitespace()

        if self._characters_remaining and self._current_character in self.TREE_BEGIN:
            self.index += 1
            return [TokenType.TREE_BEGIN, identifier]
        else:
            self.index = start_index
            return None

    def _try_parse_node_end(self) -> Optional[list]:
        if not self._characters_remaining:
            return None

        if self._current_character in self.TREE_END:
            self.index += 1
            return [TokenType.TREE_END]

        return None

    def _try_parse_entity_tag(self) -> Optional[list]:
        if not self._characters_remaining:
            return None

        # Check for tag start
        if self._current_character not in self.ENTITY_TAG:
            return None

        self.index += 1

        self._consume_whitespace()

        tag = self._consume_string()
        if tag is None:
            self._error('Entity tag must be followed by a valid string.')

        result = [TokenType.ENTITY_BEGIN, tag.casefold()]

        while True:
            self._consume_whitespace()

            alias = self._consume_entity_alias()
            if alias is not None:
                result.extend([TokenType.LITERAL, alias])
                continue

            increment = self._consume_entity_increment_decrement()
            if increment is not None:
                result.extend([TokenType.ENTITY_INCREMENT, increment])
                continue

            _set = self._consume_entity_set()
            if _set is not None:
                result.extend([TokenType.ENTITY_SET, _set])
                continue

            break

        result.append(TokenType.ENTITY_END)

        return result

    def _consume_single_line_comment(self) -> bool:
        if not self._characters_remaining:
            return False

        start_index = self.index
        for char in self.SINGLE_LINE_COMMENT:
            if char != self._current_character:
                self.index = start_index
                return False
            self.index += 1

        while self._characters_remaining:
            if self._current_character in '\r\n':
                return True
            self.index += 1
        return True

    def _consume_multi_line_comment(self) -> bool:
        if not self._characters_remaining:
            return False

        start_index = self.index
        for char in self.MULTI_LINE_COMMENT_START:
            if not self._characters_remaining:
                return False

            if char != self._current_character:
                self.index = start_index
                return False
            self.index += 1

        while self._characters_remaining:
            start_index = self.index
            for char in self.MULTI_LINE_COMMENT_END:
                if char != self._current_character:
                    self.index = start_index
                    break
                self.index += 1
            else:
                return True
            self.index += 1

        return True

    def _consume_whitespace(self) -> None:
        while self._characters_remaining:
            character = self._current_character

            if character in self.WHITESPACE:
                self.index += 1

                if character in '\r\n':
                    if character == '\r':
                        if (self.index < self.length and
                                self.string[self.index] == '\n'):
                            self.index += 1
                    self.line_number += 1
                    self.line_start_index = self.index
            else:
                break

    def _consume_quoted_string_literal(self) -> Optional[str]:
        if not self._characters_remaining:
            return None

        quote_char = self._current_character
        if quote_char not in self.QUOTE:
            return None

        self.index += 1

        accum = ''
        while self._characters_remaining:
            character = self._current_character
            self.index += 1

            if character == quote_char:
                # No rewind; skip past end quote
                return accum
            else:
                accum += character

        self._error('Unterminated literal in input string.')

    def _consume_identifier(self) -> Optional[str]:
        if not self._characters_remaining:
            return None

        if not self._current_character.isalpha():
            return None

        accum = ''

        while self._characters_remaining:
            character = self._current_character
            self.index += 1

            if character.isalnum() or character in self.IDENTIFIER_ALLOWED:
                accum += character
            else:
                self.index -= 1
                break

        return accum

    def _consume_numeric_literal(self) -> Optional[int]:
        if not self._characters_remaining:
            return None

        start_index = self.index

        accum = ''

        while self._characters_remaining:
            character = self._current_character
            self.index += 1

            if character.isdecimal():
                accum += character
            else:
                self.index -= 1
                break

        try:
            value = int(accum)
            return value
        except ValueError:
            self.index = start_index
            return None

    def _consume_string(self) -> Optional[str]:
        # NB these can't be combined with an 'or' because an empty string
        # is still a valid literal.

        if not self._characters_remaining:
            return None

        literal = self._consume_quoted_string_literal()
        if literal is not None:
            return literal

        return self._consume_identifier()

    def _consume_entity_alias(self) -> Optional[str]:
        if not self._characters_remaining:
            return None

        if self._current_character not in self.ENTITY_ALIAS:
            return None

        self.index += 1

        self._consume_whitespace()

        alias = self._consume_string()

        if alias is None:
            self._error('Entity alias must be followed by a valid string.')

        return alias

    def _consume_entity_increment_decrement(self) -> Optional[int]:
        if not self._characters_remaining:
            return None

        start_character = self._current_character
        if (start_character not in self.ENTITY_INCREMENT and
                start_character not in self.ENTITY_DECREMENT):
            return None

        self.index += 1

        self._consume_whitespace()

        number = self._consume_numeric_literal()
        if number is None:
            number = 1

        return -number if start_character == self.ENTITY_DECREMENT else number

    def _consume_entity_set(self) -> Optional[int]:
        if not self._characters_remaining:
            return None

        if self._current_character not in self.ENTITY_SET:
            return None

        self.index += 1

        self._consume_whitespace()

        number = self._consume_numeric_literal()
        if number is None:
            number = 1

        return number

    def _show_location_in_line(self) -> None:
        char_in_line = self.index - self.line_start_index

        prefix = '{prefix}{line_no}:{char_no}: '.format(
            prefix=(self.prefix + ':' if self.prefix else ''),
            line_no=self.line_number,
            char_no=char_in_line)

        location = '{prefix}{line}\n{spacing}^\n'.format(
            prefix=prefix,
            line=self.lines[self.line_number],
            spacing=('-' * (char_in_line - 1 + len(prefix))))

        sys.stderr.write(location)
        sys.stderr.flush()

    def _warn(self, message: str) -> None:
        self._show_location_in_line()

        message = message.strip() + '\n\n'
        sys.stderr.write(message)
        sys.stderr.flush()

    def _error(self, message: str, exception=None) -> None:
        if exception is None:
            exception = RuntimeError

        self._show_location_in_line()

        message = message.strip()
        raise exception(message)


def reconstruct_source(tokens: TokenStream) -> str:
    index = 0
    length = len(tokens)
    result = []
    in_entity = False
    depth = 0
    while index < length:
        token = tokens[index]
        index += 1

        if token is TokenType.TREE_BEGIN:
            identifier = tokens[index]
            index += 1
            result.extend([identifier, Tokenizer.TREE_BEGIN, ' '])
            depth += 1
        elif token is TokenType.TREE_END:
            result.extend([Tokenizer.TREE_END, ' '])
            depth -= 1
        elif token is TokenType.METADATA:
            identifier = tokens[index]
            index += 1
            result.extend([Tokenizer.METADATA_TAG, identifier, ' '])
        elif token is TokenType.LITERAL:
            identifier = tokens[index]
            index += 1
            if in_entity:
                result.append(Tokenizer.ENTITY_ALIAS)
            result.extend([repr(identifier), ' '])
        elif token is TokenType.ENTITY_BEGIN:
            identifier = tokens[index]
            index += 1
            result.extend([Tokenizer.ENTITY_TAG, repr(identifier)])
            in_entity = True
        elif token is TokenType.ENTITY_SET:
            value = tokens[index]
            index += 1
            result.extend([Tokenizer.ENTITY_SET, repr(value)])
        elif token is TokenType.ENTITY_INCREMENT:
            value = tokens[index]
            index += 1
            if value > 0:
                result.append(Tokenizer.ENTITY_INCREMENT)
            else:
                result.append(Tokenizer.ENTITY_DECREMENT)
            result.append(str(abs(value)))
        elif token is TokenType.ENTITY_END:
            result.append(' ')
            in_entity = False
        else:
            raise RuntimeError('Unknown token encountered.')

        if depth == 0:
            result.append('\n')

    return ''.join(result)


def validate_identifier(string: str) -> None:
    assert string[0].isalpha(), \
        'Token Stream Verification: Identifier has an invalid character.'
    for char in string:
        assert char.isalnum() or char in Tokenizer.IDENTIFIER_ALLOWED, \
            'Token Stream Verification: Identifier has an invalid character.'
