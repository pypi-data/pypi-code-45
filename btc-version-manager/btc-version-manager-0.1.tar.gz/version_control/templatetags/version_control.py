from typing import Any

from django import template

from version_control.utils import safety_parse_dict

register = template.Library()


@register.simple_tag()
def get_dict_item_by_expression(dictionary: dict, expression: str) -> Any:
    """
    Фильтр для парсинга словаря на основе выражения
    :param dictionary: dict, исходный словарь
    :param expression: str, выражение
    :return: Any
    """
    return safety_parse_dict(dictionary, expression)