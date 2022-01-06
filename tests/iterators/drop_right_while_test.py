import pytest
from pyutil import drop_right_while


def test_drop_right_while_when_list_is_empty():
    lst = []
    drop_right_while(lst, lambda x: x)
    assert lst == []


def test_drop_right_while_when_func_should_remove_one_value():
    lst = [1, 2, 3, 4, 5]
    func = lambda x: x % 2 == 1

    drop_right_while(lst, func)
    assert lst == [1, 2, 3, 4]


def test_drop_right_while_when_func_should_remove_four_values():
    lst = [1, 2, 3, 4, 5]
    func = lambda x: x > 1

    drop_right_while(lst, func)
    assert lst == [1]


def test_drop_right_while_when_func_should_remove_zero_values():
    lst = [1, 2, 3, 4, 5]
    func = lambda x: x > 100

    drop_right_while(lst, func)
    assert lst == [1, 2, 3, 4, 5]


def test_drop_right_while_when_func_is_not_callable():
    with pytest.raises(TypeError):
        drop_right_while([], "foo")


def test_drop_right_while_with_set():
    with pytest.raises(TypeError):
        drop_right_while(set([]), lambda x: x)


def test_drop_right_while_with_tuple():
    with pytest.raises(TypeError):
        drop_right_while((), lambda x: x)


def test_drop_right_while_with_dict():
    with pytest.raises(TypeError):
        drop_right_while({}, lambda x: x)
