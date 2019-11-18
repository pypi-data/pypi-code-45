import pytest
from pytest_cases import fixture_union


@pytest.fixture(params=[2, 3])
def a():
    return 'a123'


@pytest.fixture(params=[0, 1, 2])
def b():
    return 'b321'


f_union = fixture_union("f_union", [a, "b"])


def test_fixture_union(f_union):
    return
