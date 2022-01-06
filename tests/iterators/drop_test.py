import pytest
from pyutil import drop


def test_drop_when_list_is_empty():
    lst = []
    drop(lst)
    assert lst == []


def test_drop_when_n_is_1():
    lst = [1, 2, 3, 4, 5]
    drop(lst)
    assert lst == [2, 3, 4, 5]


def test_drop_when_n_is_4():
    lst = [1, 2, 3, 4, 5]
    drop(lst, 4)
    assert lst == [5]


def test_drop_when_n_is_0():
    lst = [1, 2, 3, 4, 5]
    drop(lst, 0)
    assert lst == [1, 2, 3, 4, 5]


def test_drop_when_n_is_negative():
    with pytest.raises(ValueError):
        drop([], -1)


def test_drop_with_set():
    with pytest.raises(TypeError):
        drop(set([]))


def test_drop_with_tuple():
    with pytest.raises(TypeError):
        drop(())


def test_drop_with_dict():
    with pytest.raises(TypeError):
        drop({})
