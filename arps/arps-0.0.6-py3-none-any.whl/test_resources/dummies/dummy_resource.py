from enum import unique
import uuid

from arps.core.abstract_resource import AbstractResource
from arps.core.simulator.resource import (Resource,
                                          TrackedValue,
                                          EvtType)
from arps.core.resource_category import ResourceCategory, ValueType


class RealResource(AbstractResource):

    def __init__(self, *, environment_identifier, value=None, category):
        super().__init__(environment_identifier=environment_identifier,
                         category=DummyCategory.Range)
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


@unique
class DummyCategory(ResourceCategory):
    Range = (uuid.uuid1(), (0, 100), ValueType.int)
    Togglable = (uuid.uuid1(), ('ON', 'OFF'), ValueType.descriptive)
    Counter = (uuid.uuid1(), (0, float('inf')), ValueType.int)
    Any = (uuid.uuid1(), None, ValueType.complex)


class DummyRealResource(RealResource):
    def __init__(self, *, environment_identifier):
        super().__init__(environment_identifier=environment_identifier,
                         value='RealResource', category=DummyCategory.Any)


class DummyFakeResource(Resource):
    def __init__(self, *, environment_identifier):
        super().__init__(environment_identifier=environment_identifier,
                         value='FakeResource', category=DummyCategory.Any)


class FakeResourceA(Resource):

    def __init__(self, *, environment_identifier, value=None):
        super().__init__(environment_identifier=environment_identifier,
                         value=value, category=DummyCategory.Range)

    def _affect_resource(self, epoch):
        if not self._affected_resource:
            return

        new_value = 'ON' if self.value > 60 else 'OFF'
        if self._affected_resource.value == new_value:
            return

        self._affected_resource.value = TrackedValue(new_value,
                                                     epoch,
                                                     self.identifier,
                                                     EvtType.rsc_indirect)


class FakeResourceB(Resource):

    def __init__(self, *, environment_identifier, value=None):
        super().__init__(environment_identifier=environment_identifier,
                         value=value, category=DummyCategory.Togglable)


class FakeResourceC(Resource):

    def __init__(self, *, environment_identifier, value=None):
        super().__init__(environment_identifier=environment_identifier,
                         value=value, category=DummyCategory.Range)


class FakeReceivedMessagesResource(Resource):

    def __init__(self, *, environment_identifier):
        super().__init__(environment_identifier=environment_identifier,
                         value=0, category=DummyCategory.Counter)
