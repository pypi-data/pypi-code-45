class UXSymbol:
    def __init__(self, exchange_id, market_type, name):
        self._exchange_id = exchange_id
        self._market_type = market_type
        self._name = name
        self._name_info = name.split('.')

    @classmethod
    def fromstring(cls, s):
        return cls(*s.split(':'))

    @classmethod
    def fromargs(cls, exchange_id, market_type, **kwargs):
        if market_type in ('spot', 'swap'):
            if 'base' in kwargs and 'quote' in kwargs:
                base = kwargs['base']
                quote = kwargs['quote']
                name = f'{base}/{quote}'.upper()
                return cls(exchange_id, market_type, name)

        if market_type == 'futures':
            if 'base' in kwargs and 'contract_expiration' in kwargs:
                base = kwargs['base']
                quote = kwargs.get('quote') or 'USD'
                contract_expiration = kwargs['contract_expiration']
                name = f'{base}/{quote}.{contract_expiration}'.upper()
                return cls(exchange_id, market_type, name)

        raise ValueError('unknown market_type or missing arguments')

    def fields(self):
        return (self.exchange_id, self.market_type, self.name)

    def __eq__(self, other):
        if isinstance(other, UXSymbol):
            return self.fields == other.fields
        return False

    def __hash__(self):
        return hash(':'.join(self.fields))

    def __repr__(self):
        class_name = type(self).__name__
        return (f'{class_name}(exchange_id={repr(self.exchange_id)}, '
                f'market_type={repr(self.market_type)}, '
                f'name={repr(self.name)})')

    def __str__(self):
        return self.name

    @property
    def exchange_id(self):
        return self._exchange_id

    @property
    def market_type(self):
        return self._market_type

    @property
    def name(self):
        return self._name

    @property
    def base(self):
        assert '/' in self._name_info[0], 'invalid format'
        return self._name_info[0].split('/')[0]

    @property
    def quote(self):
        assert '/' in self._name_info[0], 'invalid format'
        return self._name_info[0].split('/')[1]

    @property
    def contract_expiration(self):
        assert len(self._name_info) > 1, 'invalid format'
        return self._name_info[1]