from arps.core import select_resource_class, create_resource_class

from .dummy_resource import (FakeResourceA,
                             FakeResourceB,
                             FakeResourceC,
                             DummyFakeResource,
                             DummyRealResource,
                             FakeReceivedMessagesResource)


DummyResource = select_resource_class('DummyResource', DummyFakeResource, DummyRealResource)

ResourceA = create_resource_class('ResourceA', FakeResourceA)

ResourceB = create_resource_class('ResourceB', FakeResourceB)

ResourceC = create_resource_class('ResourceC', FakeResourceC)

ReceivedMessagesResource = create_resource_class('ReceivedMessagesResource',
                                                 FakeReceivedMessagesResource)
