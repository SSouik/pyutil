import pytest
from pyutil import pipe


def double(x):
    return x * 2


def increment(x):
    return x + 1


def test_pipe_with_no_functions():
    actual = pipe(10)
    expected = 10
    assert actual == expected


def test_pipe_with_funcs():
    actual = pipe(10, str)
    expected = "10"
    assert actual == expected


def test_pipe_with_funcs_2():
    actual = pipe(10, increment)
    expected = 11
    assert actual == expected


def test_pipe_with_funcs_3():
    actual = pipe(10, increment, double)
    expected = 22
    assert actual == expected


def test_pipe_with_funcs_4():
    actual = pipe(10, double, increment, str)
    expected = "21"
    assert actual == expected


def test_pipe_when_funcs_are_not_valid():
    with pytest.raises(TypeError):
        pipe(10, 123)


def test_pipe_when_funcs_are_not_valid_2():
    with pytest.raises(TypeError):
        pipe(10, increment, "foo")


def test_pipe_when_funcs_are_not_valid_3():
    with pytest.raises(TypeError):
        pipe(10, str, double, increment, "123")
