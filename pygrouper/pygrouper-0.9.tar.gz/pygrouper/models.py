from collections import defaultdict
from typing import Any, Callable, Dict, Iterable, List, Optional

class Event:
    def __init__(
        self,
        name: str,
        value: Dict[Any, Any],
        id: Optional[int] = None,
    ):
        # use provided id or
        # or create unique per event contents
        self.id = id
        if not self.id:
            self.id = frozenset(value.items()).__hash__()

        self.name = name
        self._value = value

    def is_glued(self, glue: 'Uid') -> bool:
        return glue.name in self.value

    @property
    def value(self):
        return self._value

    def update_value(self, value: Dict[Any, Any]):
        self._value.update(value)
        self.id = frozenset(self._value.items()).__hash__()

class Uid:
    """
    unique identifier of event
    """

    def __init__(
        self,
        priority: int,
        name: Any,
        value_getter: Optional[Callable[[Event], Any]] = None,
    ):
        self.name = name
        self.priority = priority

        # if no value getter provided, use default one;
        # default value getter gets uid value
        # from corresponding field in event
        self._value_getter = value_getter
        if not self._value_getter:
            self._value_getter = lambda e: e.value[self.name]

    def get_value(self, event: Event) -> Any:
        return self._value_getter(event)

    def __hash__(self) -> int:
        return self.name.__hash__()

CRGData = Dict[str, Dict[Uid, Dict[Any, List[Event]]]]
NaiveGroups = Dict[Uid, Dict[Any, List[Event]]]
NaiveGroup = Dict[Any, List[Event]]

class CRG:
    """
    state of cross-reference grouping;
    possesses a set of methods for validation and
    filtration during recursive usage
    """

    def __init__(
        self,
        groups: NaiveGroups,
        uids: List[Uid],
    ):
        # global mutable vars
        self._groups = groups
        self._unused_uids = iter(sorted(uids, key = lambda u: u.priority))
        self._incremental_result: CRGData = defaultdict(
            lambda: defaultdict(
                lambda: defaultdict(list)
            )
        )

        # level vars
        self._current_uid: Uid = next(self._unused_uids)
        self._current_level: int = self.current_uid.priority
        self._previous_uids: List[Uid] = []
        self._times_mutated = 0

    @property
    def current_result(self):
        return self._incremental_result

    @property
    def current_uid(self) -> Uid:
        return self._current_uid

    @property
    def current_level(self) -> int:
        return self._current_level

    @property
    def current_group(self) -> Optional[NaiveGroup]:
        group = []

        if self._current_uid in self.groups:
            group = self._groups[self._current_uid]

        return group

    @property
    def previous_uids(self) -> Iterable[Uid]:
        return iter(sorted(
            self._previous_uids,
            key = lambda u: u.priority,
            reverse = True,
        ))

    @property
    def times_mutated(self) -> int:
        return self._times_mutated

    @property
    def groups(self) -> NaiveGroups:
        return self._groups

    def filter_data(
        self,
        used_ids: List[int]
    ):
        filtered_groups = defaultdict(lambda: defaultdict(list))

        for mapped_uid, mapped_uid_data in self._groups.items():

            for mapped_uid_val, mapped_uid_val_data in mapped_uid_data.items():
                filtered_group = list(filter(
                    lambda x: not x.id in used_ids,
                    mapped_uid_val_data
                ))

                if filtered_group:
                    filtered_groups[mapped_uid][mapped_uid_val] = \
                        filtered_group

        self._groups = filtered_groups

    def append_group(
        self,
        glue_uid_val: Any,
        uid: Uid,
        uid_val: Any,
        group: List[Event]
    ):
        self._incremental_result[glue_uid_val][uid][uid_val] += group

    def mutate(self):
        self._previous_uids.append(self._current_uid)

        try:
            self._current_uid = next(self._unused_uids)
        except StopIteration:
            self._current_uid = None
            return self

        self._current_level = self._current_uid.priority
        self._times_mutated += 1

        return self