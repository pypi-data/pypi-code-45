# coding: utf-8
from mercury.client.model import BaseButterfly, ButterflyValueException


class UnbalancedButterfly(BaseButterfly):

    swagger_types = {
        'symbol': 'str',
        'quantity': 'int',
        'opening_date': 'date',
        'opening_price': 'float',
        'type': 'str',
        'option_legs': 'list[OptionLeg]'
    }

    attribute_map = {
        'symbol': 'symbol',
        'quantity': 'quantity',
        'opening_date': 'openingDate',
        'opening_price': 'openingPrice',
        'type': 'type',
        'option_legs': 'optionLegs'
    }

    def __init__(self,
                 symbol=None,
                 opening_date=None,
                 opening_price=None,
                 quantity=1,
                 first_leg=None,
                 mid_leg=None,
                 third_leg=None,
                 **kwargs):  # noqa: E501

        # refactor: temporary workaround
        if 'type' in kwargs:
            assert kwargs['type'] == 'unbalanced_butterfly'
            del kwargs['type']

        super(UnbalancedButterfly, self).__init__(
            symbol=symbol,
            quantity=quantity,
            opening_date=opening_date,
            opening_price=opening_price,
            first_leg=first_leg,
            mid_leg=mid_leg,
            third_leg=third_leg,
            type='unbalanced_butterfly',
            **kwargs)

        if self.first_leg.quantity == self.third_leg.quantity or \
                self.first_leg.quantity == self.mid_leg.quantity:
            raise ButterflyValueException('Invalid quantity between option legs in unbalanced butterfly setup')

        self.discriminator = None

    def __hash__(self):
        return hash(self.to_key())

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UnbalancedButterfly):
            return False

        return self.to_key() == other.to_key()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self.__eq__(other)
