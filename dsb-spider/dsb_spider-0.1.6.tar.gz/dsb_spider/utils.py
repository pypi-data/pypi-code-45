from typing import Mapping

def str_to_dict(s:str, sep:str=':') -> Mapping[str, str]:
    dict1 = {}
    for line in s.splitlines(True):
        if line.strip():
            p = line.find(sep)
            dict1[line[:p].strip()] = line[p + 1:-1].strip()
    return dict1

def typed_property(name, expected_type, default_value=None):
    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name, default_value)

    @prop.setter
    def prop(self, value):
        if isinstance(expected_type, list):
            if name not in expected_type:
                raise TypeError('{} must be in {}'.format(name, ','.join(expected_type)))
        if not isinstance(value, expected_type):
            raise TypeError('{} must be a {}'.format(name, expected_type))
        setattr(self, storage_name, value)

    @prop.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

    return pro