[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# pyutil

pyutil is a functional library which provides various methods that operate on lists, tuples, sets, dictionaries, and strings.
The module is meant to provide data manipulation in simple and efficient manner so that you can focus more
on your project. pyutil was inspired by the JavaScript library [lodash](https://lodash.com/docs/4.17.15) and
the python modules [itertools](https://docs.python.org/2/library/itertools.html) and [toolz](https://github.com/pytoolz/toolz).

## Version
1.0.0

## Table of Contents
* [Getting Started](#getting-started)
* [Linting](#linting)
    * [Lint Check](#lint-check)
    * [Code Formatting](#code-formatting)
* [Testing](#testing)
    * [Unit Test](#unit-tests)
    * [Coverage](#coverage)

<br/>

## Getting Started
Local development can be done with any version of Python3 after `3.4` but the preferred version is `3.10`
1. Set up Python3 virtual environment
    ```bash
    python3 -m venv .venv
    ```

2. Activate the virtual environment

    Linux/macOS
    ```bash
    source .venv/bin/activate
    ```
    Windows
    ```powershell
    .venv/Scripts/activate
    ```

3. Install dependencies
    ```bash
    python -m pip install -r requirements.txt
    ```

<br/>

## Linting
### Lint Check
This project uses [pylint](https://pylint.org/) to lint Python source files

Linting Python files
```bash
python -m pylint pyutil --ignore=pyutil.py --fail-under=10.0 # pyutil.py is ignored for now until more refactoring is done
```

<br/>

### Code Formatting
Fixing lint errors and warnings can be annoying and cumbersome, so for this project, [black](https://pypi.org/project/black/) is the recommended code formatter.

Install black
```bash
python -m pip install black
```

Format multiple files under a directory
```bash
python -m black <dir> 
```

Format a single file
```bash
python -m black <path-to-file>
```

Format a multiple files
```bash
python -m black <path-to-file> <path-to-file-2>
```

<br/>

## Testing
### Unit Tests
This project uses [pytest](https://docs.pytest.org/en/6.2.x/) for all unit tests.

Running all tests
```bash
python -m pytest tests
```
> Add `-v` to see the verbose output

Running an individual test file
```bash
python -m pytest tests/<test_file_name>.py
```
> Example: `python -m pytest tests/chunk_test.py`

Running an individual test
```bash
python -m pytest tests/<test_file_name>.py::<test_name>
```
> Example: `python -m pytest tests/chunk_test.py::test_chunk_when_seq_is_list`

<br/>

### Coverage
Coverage testing is done by using [coverage](https://coverage.readthedocs.io/en/6.2/) python package.

Running coverage tests
```bash
coverage run -m pytest tests
```
> Add `-v` to see the verbose output

Generate the coverage report
```bash
coverage report -m
```

> Coverage configuration is found at `.coveragerc`

<br/>

## Importing

```
# import entire module and access each method with dot operator
import pyutil

# import entire module but access each method without dot operator 
from pyutil import *

# import specific method
from pyutil import chunk

# import multiple methods
from pyutil import chunk, drop, groupby
```

## pyutil methods

| Method  | Parameters                 | Returns     | Description |
|:-------:|:--------------------------:|:-----------:|:------------|
| [chunk](#chunk) | seq, n | generator | Create a generator of values split into groups of length n. If the list cannot be split evenly, the final chunk will be the remaining values. |
| [compact](#compact) | seq | python2 - list python3 - generator| Remove all Falsey values from the sequence |
| [concat](#concat)  | *values | generator | Creates a generator concatenating all the lists and/or values. |
| [contains](#contains) | seq, value | bool | Check to see if a specific value is in the sequence or dictionary. |
| [countby](#countby) | seq, key | dict | Create a dictionary with keys composed of the return value of the funcion/key applied to each item in the sequence. The value for each key is the number of times each key was returned. |
| [difference](#difference) | seq, *exclude_seqs | generator | Create a generator with all the values in the sequence that are unique. |
| [drop](#drop) | lst, n = 1 | None | Drop 'n' number of values in the list starting at the beginning. Mutates the list. |
[drop_right](#drop_right) | lst, n = 1 | None | Drop 'n' number of values in the list starting at the end. Mutates the list. |
| [drop_right_while](#drop_right_while) | lst, func | None | Drop values from the list as long as the predicate function is satisfied. Starts at the end of the list. Mutates the list. |
| [drop_while](#drop_while) | lst, func | None | Drop values from the list as long as the predicate function is satisfied. Starts at the beginning of the list. Mutates the list.|
| [every](#every) | seq, func | bool | Apply callable on each value in the sequence and return True if all values satisfy the predicate function. Return False otherwise. |
| [fill](#fill) | seq, value, start = 0, end = None | generator | Fill the sequence with a value. |
| [find](#find) | seq, func, start = 0, end = None | any | Find and return the first value in the sequence that satisfies the predicate function. |
| [find_all](#find_all) | seq, func, start = 0, end = None | python2 - list python3 - generator | Find all the values in the sequence that satisfy the predicate function. |
| [find_index](#find_index) | seq, func, from_index = 0 | int | Find the index of the first value that satisfies the predicate function. Returns -1 if no value was found. |
| [groupby](#groupby) | seq, key | dict | Create a dictionary with keys composed of the return value of the funcion/key applied to each item in the sequence. The value for each key is a list of values that produced the key. |
| [head](#head) | seq | any | Return the first value in the sequence. |
| [index_of](#index_of) | seq, value, from_index = 0 | int | Return the index of a value in a sequence. Returns -1 if the value was not found. |
| [initial](#initial) | seq | generator | Create a generator of all the values in a sequence except the last. |
| [intersection](#intersection) | *seqs | generator | Creates a generator containing values found in all sequences. |
| [join](#join) | seq, separator = ',' | str | Concatenate all values in a sequence into a string separated by the separator value. |
| [last](#last) | seq | any | Return the last value in the sequence. |
| [merge](#merge) | *seqs | generator | Create a generator that contains one instance of all values from the sequences. |
| [pipe](#pipe) | data, *funcs | any | Pipe data through a series of functions. |
| [pull](#pull) | lst, *pull_vals | None |  Remove values from the list. Mutates the list. |
| [pull_all](#pull_all) | lst, pull_vals | None | Remove values from the list. Mutates the list. |
| [pull_at](#pull_at) | lst, *pull_indices | None | Remove all values at specified indices. Mutates the list. |
| [pull_all_at](#pull_all_all) | lst, pull_indices | None | Remove values at all specified indices. Mutates the list. |
| [remove](#remove) | seq, *remove_values | generator | Remove values from the sequence. |
| [remove_all](#remove_all) | seq remove_values | generator | Remove values from the sequence. |
| [remove_at](#remove_at) | seq, *remove_indices | generator | Remove values at specified indices from the sequence. |
| [remove_all_at](#remove_all_at) | seq, remove_indices | generator |Remove values at specified indices from the sequence. |
| [subset](#subset) | seq, start = 0, end = None | generator | Create a subset of the sequence. |
| [some](#some) | seq, func | bool | Return True if some value in the sequence satisfies the predicate function. Returns False otherwise. |
| [tail](#tail) | seq | generator | Return all values in the sequence except the first. |
| [assign](#assign) | target, *sources | dict | Assign all values from the sources into the target dictioanary. Mutates target dictionary. |
| [entries](#entries) | dct | generator | Creates a generator of all key value pairs in the dictionary. |
| [str_count](#str_count) | string, target, start = 0, end = None | int | Count the number of times a target string appears in a string. |
| [endswith](#endswith) | string, target | bool | Check to see if the target string is the end of the string. |
| [repeat](#repeat) | string, n | str | Repeat a string 'n' number of times. |
| [replace](#replace) | string, target, replacement, n = None | str | Replace a target string with a replacement string 'n' number of times. |
| [str_remove](#str_remove) | string, target, start = 0, end = None | str | Remove a target string from the string. |
| [words](#words) | string | generator | Find all substrings in the string that contain alphabetical characters. |

#### chunk
```
>>> lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> chunk(lst, 4)
-> [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]
```

#### compact
```
>>> lst = [True, None, False, 'hello', 'test', '', 12, 10, 0]
>>> compact(lst)
-> [True, 'hello', 'test', 12, 0] # python2 - list python3 - generator
```

#### concat
```
>>> lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> concat(lst, {11, 12, 13})
-> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] # generator
```

#### contains
```
>>> lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> contains(lst, 4)
-> True
>>> contains(lst, 12)
-> False
```

#### countby
```
>>> def even_odd(n):
...   if n % 2 == 0:
...     return 'even'
...   return 'odd'
...
>>> lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> countby(lst, even_odd)
-> {'odd': 5, 'even': 5}
```

#### difference
```
>>> lst = [1, 2, 3, 4, 5]
>>> difference(lst, [1, 2], (4, 6, 7, 'a'))
-> [3, 5] # generator
```

#### drop
```
>>> lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> drop(lst, 4)
>>> lst
-> [5, 6, 7, 8, 9, 10]
```

#### drop_right
```
>>> lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> drop_right(lst, 2)
>>> lst
-> [1, 2, 3, 4, 5, 6, 7, 8]
```

#### drop_right_while
```
>>> lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> drop_right_while(lst, lambda x: x != 6)
>>> lst
-> [1, 2, 3, 4, 5, 6]
```

#### drop_while
```
>>> lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> drop_while(lst, lambda x: x != 6)
>>> lst
-> [6, 7, 8, 9, 10]
```

#### every
```
>>> lst = [1, 2, 3, 4, 5]
>>> every(lst, lambda x: x > 0)
-> True
>>> every(lst, lambda x: x % 2 == 0)
-> False
```

#### fill
```
>>> lst = [1, 2, 3, 4, 5]
>>> fill(lst, '*')
-> ['*', '*', '*', '*', '*']
>>> fill(lst, '_', 2)
-> [1, 2, '_', '_', '_']
```

#### find
```
>>> lst = [{'id': 1, 'name': 'Sam'}, {'id': 2, 'name': 'Liam'}]
>>> find(lst, lambda x: x['id'] == 1)
-> {'id': 1, 'name': 'Sam'}
```

#### find_all
```
>>> lst = [{'id': 1, 'name': 'Sam', 'age': 22}, {'id': 2, 'name': 'Liam', 'age': 12}, {'id': 3, 'name': 'John', 'age': 22}]
>>> find_all(lst, lambda x: x['age'] == 22)
-> [{'id': 0, 'name': 'Sam', 'age': 22}, {'id': 3, 'name': 'John', 'age': 22}] # python2 list - python3 generator
```

#### find_index
```
>>> lst = [{'id': 1, 'name': 'Sam', 'age': 22}, {'id': 2, 'name': 'Liam', 'age': 12}, {'id': 3, 'name': 'John', 'age': 22}]
>>> find_index(lst, lambda x: x['id'] == 2)
>>> 1
```

#### groupby
```
>>> lst = [{'id': 1, 'name': 'Sam', 'age': 22}, {'id': 2, 'name': 'Liam', 'age': 12}, {'id': 3, 'name': 'John', 'age': 22}]
>>> groupby(lst, 'age')
-> {22: [{'id': 1, 'name': 'Sam', 'age': 22}, {'id': 3, 'name': 'John', 'age': 22}], 12: [{'id': 2, 'name': 'Liam', 'age': 12}]}
```

#### head
```
>>> lst = [1, 2, 3, 4, 5]
>>> head(lst)
-> 1
```

#### index_of
```
>>> lst = [1, 2, 3, 4, 5]
>>> index_of(lst, 4)
-> 3
```

#### initial
```
>>> lst = [1, 2, 3, 4, 5]
>>> initial(lst)
-> [1, 2, 3, 4] # generator
```

#### intersection
```
>>> intersection([1, 2, 3], (2, 3, 4, 5), {1, 2, 3, 4, 5})
-> [2, 3] # generator
```

#### join
```
>>> lst = [1, 2, 3, 4, 5]
>>> join(lst)
-> '1,2,3,4,5'
>>> join(lst, '-')
-> '1-2-3-4-5'
```

#### last
```
>>> lst = [1, 2, 3, 4, 5]
>>> last(lst)
-> 5
```

#### merge
```
>>> lst = [1, 2, 3, 4, 5]
>>> merge(lst, {1, 2, 3, 4, 5, 6, 7}, (4, 5, 6, 7, 8, 9))
-> [1, 2, 3, 4, 5, 6, 7, 8, 9] # generator
```

#### pipe
```
>>> pipe(100, lambda x: x*2, lambda x: x + 10, str)
-> '210'
```

#### pull
```
>>> lst = [1, 2, 3, 4, 5]
>>> pull(lst, 2, 4)
>>> lst
-> [1, 3, 5]
```

#### pull_all
```
>>> lst = [1, 2, 3, 4, 5]
>>> pull_all(lst, [2, 4])
>>> lst
-> [1, 3, 5]
```

#### pull_at
```
>>> lst = [1, 2, 3, 4, 5]
>>> pull_at(lst, 0, 2)
>>> lst
-> [2, 4, 5]
```

#### pull_all_at
```
>>> lst = [1, 2, 3, 4, 5]
>>> pull_all_at(lst, [0, 2])
>>> lst
-> [2, 4, 5]
```

#### remove
```
>>> lst = [1, 2, 3, 4, 5]
>>> remove(lst, 1, 3, 5)
-> [2, 4] # generator
```

#### remove_all
```
>>> lst = [1, 2, 3, 4, 5]
>>> remove_all(lst, [1, 3, 5])
-> [2, 4] # generator
```

#### remove_at
```
>>> lst = [1, 2, 3, 4, 5]
>>> remove_at(lst, 0, 2, 4)
-> [2, 4] # generator
```

#### remove_all_at
```
>>> lst = [1, 2, 3, 4, 5]
>>> remove_all_at(lst, [0, 2, 4])
-> [2, 4] # generator
```

#### subset
```
>>> lst = [1, 2, 3, 4, 5]
>>> subset(lst, 1, 3)
-> [2, 3]
```

#### some
```
>>> lst = [1, 2, 3, 4, 5]
>>> every(lst, lambda x: x <> 0)
-> False
>>> every(lst, lambda x: x % 2 == 0)
-> True
```

#### tail
```
>>> lst = [1, 2, 3, 4, 5]
>>> tail(lst)
-> [2, 3, 4, 5]
```

#### assign
```
>>> assign({}, {'a': 1, 'b': 2}, {'c': 3})
-> {'a': 1, 'b': 2, 'c': 3}
```

#### entries
```
>>> entries({'a': 1, 'b': 2, 'c': 3})
-> [('a', 1), ('b', 2), ('c', 3)] # generator
```

#### str_count
```
>>> str = 'abc-def-abc-def'
>>> str_count(str, 'abc')
-> 2
>>> str_count(str, 'abc', 3)
-> 1
```

#### endswith
```
>>> endswith('This is a sentence', 'e')
-> True
>>> endswith('This is a sentence', 'tence')
-> True
```

#### repeat
```
>>> repeat('abc', 3)
-> 'abcabcabc'
```

#### replace
```
>>> str = 'This is a test string.'
>>> replace(str, 'i', 'X')
-> 'ThXs Xs a test strXng.'
>>> replace(str, 'i', 'X', 2)
-> 'ThXs Xs a test string.'
```

#### str_remove
```
>>> str = 'Another string to test.'
>>> str_remove(str, 'string')
-> 'Another  to test.'
>>> str_remove(str, 'string', 3, 6)
-> 'Another string to test.'
```

#### words
```
>>> str = 'This is a sentence with some words.'
>>> words(str)
-> ['This', 'is', 'a', 'sentence', 'with', 'some', 'words'] # generator
```

## Authors

* **Samuel Souik** - *Initial work* - [SSouik](https://github.com/SSouik)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
### Inspiration

* JavaScript library [lodash](https://lodash.com/docs/4.17.15)
* Python module [itertools](https://docs.python.org/2/library/itertools.html)
* Python module [toolz](https://github.com/pytoolz/toolz)


## Todo

* Support regex in string functions
* Add more support for dictionaries
* Make functions more efficient
