"""Test AccessConditions contract."""
#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0
import uuid

from ocean_keeper.conditions.access import AccessSecretStoreCondition
from tests.resources.helper_functions import get_consumer_account
from tests.resources.tiers import e2e_test


@e2e_test
def test_access_secret_store_condition_contract():
    access_secret_store_condition = AccessSecretStoreCondition('AccessSecretStoreCondition')
    assert access_secret_store_condition
    assert isinstance(access_secret_store_condition, AccessSecretStoreCondition), \
        f'{access_secret_store_condition} is not instance of AccessSecretStoreCondition'


@e2e_test
def test_check_permissions_not_registered_did():
    access_secret_store_condition = AccessSecretStoreCondition('AccessSecretStoreCondition')
    consumer_account = get_consumer_account()
    did_id = uuid.uuid4().hex + uuid.uuid4().hex
    assert not access_secret_store_condition.check_permissions(did_id, consumer_account.address)

# TODO Create test for check permission after access granted.
