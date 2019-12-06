from django.test import TestCase
from django.core.exceptions import ValidationError

from .models import TCKNModel
from tckn.validators import tckn_validator


class TestTCKNField(TestCase):
    invalids = ["", 12345678901, "12345678901", "1", "2134abc", "01234567890"]
    valid = "10000000146"

    def test_validator(self):
        tckn_validator(self.valid)
        for invalid in self.invalids:
            self.assertRaises(ValidationError, tckn_validator, invalid)

    def test_create(self):
        model = TCKNModel.objects.create(tckn=self.valid)
        self.assertIsInstance(model, TCKNModel)

    def test_invalids(self):
        for invalid in self.invalids:
            self.assertRaises(ValidationError, TCKNModel.objects.create, tckn=invalid)
