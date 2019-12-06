from typing import List, Iterable
from . import forest_serialization_pb2
from .structures import Node, Tree, Entity, Literal, Metadata


class Forest(object):
    """Object representation of a compiled program."""

    def __init__(self, entry_points: Iterable[int], nodes: Iterable[Node]):
        self.entry_points: List[int] = list(entry_points)
        self.nodes: List[Node] = list(nodes)

    def serialize_to_stream(self) -> bytes:
        proto_forest = forest_serialization_pb2.Forest()
        proto_forest.entry_points.extend(self.entry_points)
        entities = set()

        for node in self.nodes:
            proto_node = proto_forest.nodes.get_or_create(node.key)

            if isinstance(node, Tree):
                proto_tree = proto_node.tree
                proto_tree.identifier = node.identifier
                proto_tree.branches.extend(node.branches)

            elif isinstance(node, Entity):
                proto_entity = proto_node.entity
                proto_entity.identifier = node.identifier
                proto_entity.alias = node.alias

                if node.count_type is Entity.CountType.INCREMENT:
                    proto_entity.increment = node.count
                elif node.count_type is Entity.CountType.SET:
                    proto_entity.set = node.count
                else:
                    raise RuntimeError('Could not serialize entity count type "{}".'.format(
                        node.count_type.value))
                entities.add(node.identifier)

            elif isinstance(node, Literal):
                proto_node.literal = node.identifier

            elif isinstance(node, Metadata):
                proto_node.metadata = node.identifier

            else:
                raise RuntimeError('Node class unsupported for serialization!')

        proto_forest.entities.extend(list(entities))

        return proto_forest.SerializeToString()

    @classmethod
    def from_stream(cls, stream: bytes) -> 'Forest':
        proto_forest = forest_serialization_pb2.Forest.FromString(stream)

        nodes = []
        for key in sorted(proto_forest.nodes.keys()):
            proto_node = proto_forest.nodes[key]
            node_type = proto_node.WhichOneof('contents')

            if node_type == 'tree':
                proto_tree = proto_node.tree
                tree = Tree(key, proto_tree.identifier, proto_tree.branches)
                nodes.append(tree)

            elif node_type == 'entity':
                proto_entity = proto_node.entity
                entity = Entity(
                    key,
                    proto_entity.identifier,
                    proto_entity.alias)
                count_type = proto_entity.WhichOneof('count')
                if count_type == 'increment':
                    entity.count_type = Entity.CountType.INCREMENT
                    entity.count = proto_entity.increment
                elif count_type == 'set':
                    entity.count_type = Entity.CountType.SET
                    entity.count = proto_entity.set
                else:
                    raise RuntimeError('Unknown entity count type in stream: {}'.format(count_type))
                nodes.append(entity)

            elif node_type == 'literal':
                literal = Literal(key, proto_node.literal)
                nodes.append(literal)

            elif node_type == 'metadata':
                metadata = Metadata(key, proto_node.metadata)
                nodes.append(metadata)

            else:
                raise RuntimeError('Unknown node type in serialized data: {}'.format(node_type))

        return cls(proto_forest.entry_points, nodes)

    def __repr__(self) -> str:
        return '{self.__class__.__name__}([{entry_pts}], ...)'.format(
            self=self,
            entry_pts=', '.join(str(x) for x in self.entry_points))
