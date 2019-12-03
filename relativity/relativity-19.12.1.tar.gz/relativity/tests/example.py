from relativity import M2M, M2MGraph


class Supplier(object):
    def __init__(self, ):
        pass


SUPPLY_CHAIN = M2MGraph([
    ("manufacturer", "company"),
    ("company", "retailer"),
    ("retailer", "country"),
    ("manufacturer", "country"),
    ("company", "country"),
    ])

SUPPLY_CHAIN["manufacturer", "company"].update(
    ("foxconn", "apple"),
    ("foxconn", "amazon"),
    ("foxconn", "HP"),
    ("foxconn", "nintendo"),
    ("foxconn", "acer"),
    )
