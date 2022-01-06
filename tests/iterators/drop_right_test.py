import pytest
from pyutil import drop_right


def test_drop_right_when_list_is_empty():
    with pytest.raises(ValueError):
        drop_right([])


def test_drop_right_when_n_is_1():
    lst = [1, 2, 3, 4, 5]
    drop_right(lst)
    assert lst == [1, 2, 3, 4]


def test_drop_right_when_n_is_4():
    lst = [1, 2, 3, 4, 5]
    drop_right(lst, 4)
    assert lst == [1]


def test_drop_right_when_n_is_0():
    lst = [1, 2, 3, 4, 5]
    drop_right(lst, 0)
    assert lst == [1, 2, 3, 4, 5]


def test_drop_right_when_n_is_negative():
    with pytest.raises(ValueError):
        drop_right([], -1)


def test_drop_right_with_set():
    with pytest.raises(TypeError):
        drop_right(set([]))


def test_drop_right_with_tuple():
    with pytest.raises(TypeError):
        drop_right(())


def test_drop_right_with_dict():
    with pytest.raises(TypeError):
        drop_right({})
