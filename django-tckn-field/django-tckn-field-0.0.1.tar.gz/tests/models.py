from django.db import models

from tckn.fields import TCKNField


class TCKNModel(models.Model):
    tckn = TCKNField()