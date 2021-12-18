import pytest
from pyutil.chunk import chunk

def test_chunk_when_seq_is_list():
    lst = [1, 2, 3, 4, 5]
    actual = list(chunk(lst, 2))
    expected = [[1, 2], [3, 4], [5]]
    assert actual == expected

def test_chunk_when_seq_is_tuple():
    tup = (1, 2, 3, 4, 5)
    actual = list(chunk(tup, 2))
    expected = [[1, 2], [3, 4], [5]]
    assert actual == expected

def test_chunk_when_seq_is_set():
    set = {1, 2, 3, 4, 5}
    actual = list(chunk(set, 2))
    expected = [[1, 2], [3, 4], [5]]
    assert actual == expected

def test_chunk_when_seq_is_string():
    string = 'foobar'
    actual = list(chunk(string, 2))
    expected = [['f', 'o'], ['o', 'b'], ['a', 'r']]
    assert actual == expected

def test_chunk_when_n_is_greater_than_length():
    lst = [1, 2, 3, 4, 5]
    actual = list(chunk(lst, 10))
    expected = [[1, 2, 3, 4, 5]]
    assert actual == expected

def test_chunk_when_n_is_zero():
    lst = [1, 2, 3, 4, 5]
    actual = list(chunk(lst, 0))
    expected = [[1, 2, 3, 4, 5]]
    assert actual == expected

def test_chunk_when_seq_is_empty():
    actual = list(chunk([], 3))
    expected = [[]]
    assert actual == expected

def test_chunk_when_seq_is_none():
    with pytest.raises(TypeError):
        list(chunk(None, 3))

def test_chunk_when_n_is_below_zero():
    with pytest.raises(ValueError):
        list(chunk([1, 2, 3], -1))

def test_chunk_when_n_is_not_int():
    with pytest.raises(TypeError):
        list(chunk([1, 2], 'foo'))

def test_chunk_when_seq_is_not_valid():
    with pytest.raises(TypeError):
        list(chunk({'a': 1}, 10))
