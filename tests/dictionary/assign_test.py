import pytest
from pyutil import assign


def test_assign_with_empty_dict():
    obj = {}
    assign(obj, {})
    expected = {}
    assert obj == expected


def test_assign_with_sources():
    obj = {"a": 1}
    assign(obj, {})
    expected = {"a": 1}
    assert obj == expected


def test_assign_with_sources_2():
    obj = {"a": 1}
    assign(obj, {"b": 2})
    expected = {"a": 1, "b": 2}
    assert obj == expected


def test_assign_with_sources_3():
    obj = {"a": 1}
    assign(obj, {"b": 2, "c": 3})
    expected = {"a": 1, "b": 2, "c": 3}
    assert obj == expected


def test_assign_with_sources_4():
    obj = {"a": 1}
    assign(obj, {"b": 2}, {"c": 3})
    expected = {"a": 1, "b": 2, "c": 3}
    assert obj == expected


def test_assign_with_sources_5():
    obj = {"a": 1}
    assign(obj, {"b": 2}, {"c": 3}, {"b": 4})
    expected = {"a": 1, "b": 4, "c": 3}
    assert obj == expected


def test_assign_with_sources_6():
    obj = {"a": 1}
    assign(obj, {"b": 2}, {"c": 3}, {"d": 4, "c": 5}, {})
    expected = {"a": 1, "b": 2, "c": 5, "d": 4}
    assert obj == expected


def test_assign_when_target_is_not_valid():
    with pytest.raises(TypeError):
        assign("foo", {})


def test_assign_when_sources_are_not_valid():
    with pytest.raises(TypeError):
        assign({}, "foo")


def test_assign_when_sources_are_not_valid_2():
    with pytest.raises(TypeError):
        assign({}, {}, {"a": 1}, "foo")
