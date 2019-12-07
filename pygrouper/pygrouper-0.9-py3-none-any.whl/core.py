from collections import defaultdict
from typing import Any, Callable, List, Tuple

from .models import CRG, CRGData, Event, NaiveGroups, Uid


def crg(
    data: List[Event],
    uids: List[Uid],
    glue: Uid,
    contradiction_solver: Callable[[CRG, Any], List[Event]] = \
        lambda state, uid_val, glue: []
) -> CRGData:
    """
    performs cross reference matching of data by uids
    grouping by grouping marker if present in matched group

    :param data: events for grouping
    :param uids: list of uids
    :param glue: uid for grouping
    :param contradiction_solver: function to solve in level contradictions
    :return: grouping result by glue uid
    """

    # initialize mutable state of
    # the upcoming cross-reference process
    state: CRG = CRG(
        get_naive_groups(data, uids),
        sorted(uids, key = lambda u: u.priority),
    )

    return group_recursively(state, glue, contradiction_solver)


def get_naive_groups(
    events: List[Event],
    uids: List[Uid],
) -> NaiveGroups:
    """
    simple grouping of data by uids;
    based on presence of equal uid values

    :param events: events for naive grouping
    :param uids: list of uids
    :return: grouping result by uids
    """

    groups = defaultdict(lambda: defaultdict(list))

    for uid in uids:
        for event in events:
            val = uid.get_value(event)
            if val:
                groups[uid][val] += [event]

    return groups


def group_recursively(
    state: CRG,
    glue: Uid,
    contradiction_solver: Callable[[CRG, Any, Uid], List[Event]],
) -> CRGData:
    """
    performs procedures recursively grouping filtering and
    solving contradictions filling the result

    :param state: current state
    :param glue: grouping uid
    :return: result mutated from current step
    """

    if state.current_group:
        group_used_ids = []

        for uid_val, uid_val_data in state.current_group.items():
            used_ids, group, glue_val = get_level_group(
                uid_val_data,
                glue,
                state,
                uid_val,
                contradiction_solver,
            )

            if group:
                state.append_group(
                    glue_val,
                    state.current_uid,
                    uid_val,
                    group,
                )
                group_used_ids += used_ids

        # filter matched data from
        # lower priority levels
        state.filter_data(group_used_ids)

        # mutate state to next level uid
        state.mutate()

        return group_recursively(
            state,
            glue,
            contradiction_solver,
        )

    return state.current_result


def get_glue_val(
    group: List[Event],
    glue: Uid
) -> Any:
    return glue.get_value(next(filter(
        lambda e: e.is_glued(glue),
        group
    )))


def get_level_group(
    group: List[Event],
    glue: Uid,
    state: CRG,
    uid_val: Any,
    contradiction_solver: Callable[[CRG, Any, Uid], List[Event]],
) -> Tuple[List[int], List[Event], Any]:
    used_ids = []
    level_group = []
    glue_val = None

    if len(group) > 1:
        group_entropy = get_group_entropy(group, glue)

        # solve contradictions
        if group_entropy > 0:
            group = contradiction_solver(state, uid_val, glue)
            group_entropy = get_group_entropy(group, glue)

        # zero entropy = zero confusion
        if not group_entropy:
            for event in group:

                if not event.is_glued(glue):
                    level_group.append(event)
                    used_ids.append(event.id)

                else:
                    glue_val = glue.get_value(event)

    return used_ids, level_group, glue_val


def get_group_entropy(group: List[Event], glue: Uid) -> int:
    entropy_container = set()

    for event in group:
        glued = event.is_glued(glue)

        if glued:
            entropy_container.update([glue.get_value(event)])

    return len(entropy_container) - 1
