from uxapi.symbol import UXSymbol


class UXTopic:
    __slots__ = ('_id', '_exchange_id', '_market_type',
                 '_datatype', '_extrainfo')

    def __init__(self, id, exchange_id, market_type,
                 datatype, extrainfo=''):
        self._id = id
        self._exchange_id = exchange_id
        self._market_type = market_type
        self._datatype = datatype
        self._extrainfo = extrainfo

    def __eq__(self, other):
        if isinstance(other, UXTopic):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        class_name = type(self).__name__
        return (f'{class_name}(id={repr(self.id)}, '
                f'exchange_id={repr(self.exchange_id)}, '
                f'market_type={repr(self.market_type)}, '
                f'datatype={repr(self.datatype)}, '
                f'extrainfo={repr(self.extrainfo)})')

    def __str__(self):
        if self.extrainfo:
            return f'{self.datatype}:{self.extrainfo}'
        else:
            return self.datatype

    @property
    def id(self):
        return self._id

    @property
    def exchange_id(self):
        return self._exchange_id

    @property
    def market_type(self):
        return self._market_type

    @property
    def datatype(self):
        return self._datatype

    @property
    def maintype(self):
        return self._datatype.split('.')[0]

    @property
    def subtype(self):
        parts = self._datatype.split('.', maxsplit=1)
        if len(parts) > 1:
            return parts[1]
        else:
            return None

    @property
    def extrainfo(self):
        return self._extrainfo