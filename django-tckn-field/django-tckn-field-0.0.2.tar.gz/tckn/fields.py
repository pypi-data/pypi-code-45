from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

from .validators import tckn_validator


class TCKNField(models.CharField):

    description = _("Republic of Turkey Identification Number")

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("max_length", 11)
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        return tckn_validator(value)
