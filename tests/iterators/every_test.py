import pytest
from pyutil import every


def test_every_when_seq_is_empty():
    actual = every([], lambda x: x > 1)
    assert actual == False


def test_every_when_func_is_true_for_all_values():
    actual = every([1, 2, 3, 4, 5], lambda x: x > 0)
    assert actual == True


def test_every_when_func_is__not_true_for_all_values():
    actual = every([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
    assert actual == False


def test_every_when_seq_is_not_valid():
    with pytest.raises(TypeError):
        every(1, lambda x: x > 0)


def test_every_when_func_is_not_callable():
    with pytest.raises(TypeError):
        every([1, 2, 3], "foo")
