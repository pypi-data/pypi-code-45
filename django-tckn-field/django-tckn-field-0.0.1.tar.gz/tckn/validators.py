import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def tckn_validator(value):
    if not isinstance(value, str):
        raise ValidationError(_("The number entered is not valid"), code="invalid_tckn_number")

    if not re.match("^[1-9]{1}[0-9]{10}$", value):
        raise ValidationError(_("The number entered is not valid"), code="invalid_tckn_number")

    valid = True

    int_value = [int(x) for x in list(value)]

    odd = sum(int_value[0:9:2]) * 7
    even = sum(int_value[1:8:2])
    if (odd - even) % 10 != int(value[9]):
        valid = False

    last_character = sum(int_value[0:10]) % 10
    if last_character != int(value[10]):
        valid = False

    if not valid:
        raise ValidationError(_("The number entered is not valid"), code="invalid_tckn_number")

    return value
