[![Lint](https://github.com/SSouik/pyutil/actions/workflows/lint.yml/badge.svg?branch=main)](https://github.com/SSouik/pyutil/actions/workflows/lint.yml)
[![Unit Tests](https://github.com/SSouik/pyutil/actions/workflows/unit-tests.yml/badge.svg?branch=main)](https://github.com/SSouik/pyutil/actions/workflows/unit-tests.yml)
[![Coverage](https://github.com/SSouik/pyutil/actions/workflows/coverage.yml/badge.svg?branch=main)](https://github.com/SSouik/pyutil/actions/workflows/coverage.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
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
    * [Diff Coverage](#diff-coverage)
* [How To Use](#how-to-use)
    * [Importing](#importing)
    * [Methods](#methods)

<br/>

## Getting Started
Local development can be done with any version of Python3 after `3.4` but the preferred version is `3.10`
1. Set up Python3 virtual environment
    ```bash
    python3 -m venv .venv
    ```

2. Configure `pip` to use the AWS CodeArtifact Repository for Python packages
    * Create a `pip.conf` file at `.venv/pip.conf`
        ```bash
        touch .venv/pip.conf
        ```
    * Add the repository url
        ```bash
        echo "[global]" >> .venv/pip.conf
        echo "index-url = https://aws:{auth-token}@ss-480277082058.d.codeartifact.us-east-2.amazonaws.com/pypi/python/simple" >> .venv/pip.conf
        ```
    * Replace `{auth-token}` with your AWS CodeArtifact bearer token
        ```bash
        aws codeartifact get-authorization-token --domain ss --domain-owner 480277082058 --query authorizationToken --output text
        ```
        This will output your bearer token into the terminal. Copy it and replace `{auth-token}` in `.venv/pip.conf` with the token.
    > This assumes that you have the AWS CLI configured and set up locally already


3. Activate the virtual environment

    Linux/macOS
    ```bash
    source .venv/bin/activate
    ```
    Windows
    ```powershell
    .venv/Scripts/activate
    ```

4. Install dependencies
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

Coverage report HTML
```bash
coverage html
```
> The HTML report can be found at `tests/coverage/html`

Coverage report XML
```bash
coverage xml
```
> The XML report can be found at `tests/coverage/coverage.xml`

Coverage report JSON
```bash
coverage json
```
> The JSON report can be found at `tests/coverage/coverage.json`

**Coverage configuration is found at `.coveragerc`**

<br/>

### Diff Coverage
If you would like to test the coverage on just your changes compared to `origin/main`, you can use the package [diff_cover](https://pypi.org/project/diff-cover/) to do so.

1. First install `tomli` if you do not already have it
    ```bash
    python -m pip install tomli
    ```

2. Run the coverage tests then generate an XML report
    * Both commands are shown above in the [Coverage](#coverage) section

3. Run coverage on the diff
    ```bash
    diff-cover tests/coverage/coverage.xml --config-file diff.coverage.toml
    ```

You can also write the report to a **.html**, **.json**, or **.md** file by adding one of the following:
* `--html-report <html-file>`
* `--json-report <json-file>`
* `--markdown-report <md-file>`

<br/>

## How To Use
### Importing
Import the entire module
```python
import pyutil
```
> Methods will be accessible via the `.` operator. Example - `pyutil.chunk`

Import specific method
```python
from pyutil import chunk
```

Import multiple methods
```python
from pyutil import chunk, drop, groupby
```

### Methods

| Method  | Parameters                 | Returns     | Description |
|:-------:|:--------------------------:|:-----------:|:------------|
| chunk | seq, n | generator | Create a generator of values split into groups of length n. If the list cannot be split evenly, the final chunk will be the remaining values. |
| compact | seq | python2 - list python3 - generator| Remove all Falsey values from the sequence |
| concat  | *values | generator | Creates a generator concatenating all the lists and/or values. |
| contains | seq, value | bool | Check to see if a specific value is in the sequence or dictionary. |
| countby | seq, key | dict | Create a dictionary with keys composed of the return value of the funcion/key applied to each item in the sequence. The value for each key is the number of times each key was returned. |
| difference | seq, *exclude_seqs | generator | Create a generator with all the values in the sequence that are unique. |
| drop | lst, n = 1 | None | Drop 'n' number of values in the list starting at the beginning. Mutates the list. |
drop_right | lst, n = 1 | None | Drop 'n' number of values in the list starting at the end. Mutates the list. |
| drop_right_while | lst, func | None | Drop values from the list as long as the predicate function is satisfied. Starts at the end of the list. Mutates the list. |
| drop_while | lst, func | None | Drop values from the list as long as the predicate function is satisfied. Starts at the beginning of the list. Mutates the list.|
| every | seq, func | bool | Apply callable on each value in the sequence and return True if all values satisfy the predicate function. Return False otherwise. |
| fill | seq, value, start = 0, end = None | generator | Fill the sequence with a value. |
| find | seq, func, start = 0, end = None | any | Find and return the first value in the sequence that satisfies the predicate function. |
| find_all | seq, func, start = 0, end = None | python2 - list python3 - generator | Find all the values in the sequence that satisfy the predicate function. |
| find_index | seq, func, from_index = 0 | int | Find the index of the first value that satisfies the predicate function. Returns -1 if no value was found. |
| groupby | seq, key | dict | Create a dictionary with keys composed of the return value of the funcion/key applied to each item in the sequence. The value for each key is a list of values that produced the key. |
| head | seq | any | Return the first value in the sequence. |
| index_of | seq, value, from_index = 0 | int | Return the index of a value in a sequence. Returns -1 if the value was not found. |
| initial | seq | generator | Create a generator of all the values in a sequence except the last. |
| intersection | *seqs | generator | Creates a generator containing values found in all sequences. |
| join | seq, separator = ',' | str | Concatenate all values in a sequence into a string separated by the separator value. |
| last | seq | any | Return the last value in the sequence. |
| merge | *seqs | generator | Create a generator that contains one instance of all values from the sequences. |
| pipe | data, *funcs | any | Pipe data through a series of functions. |
| pull | lst, *pull_vals | None |  Remove values from the list. Mutates the list. |
| pull_all | lst, pull_vals | None | Remove values from the list. Mutates the list. |
| pull_at | lst, *pull_indices | None | Remove all values at specified indices. Mutates the list. |
| pull_all_at | lst, pull_indices | None | Remove values at all specified indices. Mutates the list. |
| remove | seq, *remove_values | generator | Remove values from the sequence. |
| remove_all | seq remove_values | generator | Remove values from the sequence. |
| remove_at | seq, *remove_indices | generator | Remove values at specified indices from the sequence. |
| remove_all_at | seq, remove_indices | generator |Remove values at specified indices from the sequence. |
| subset | seq, start = 0, end = None | generator | Create a subset of the sequence. |
| some | seq, func | bool | Return True if some value in the sequence satisfies the predicate function. Returns False otherwise. |
| tail | seq | generator | Return all values in the sequence except the first. |
| assign | target, *sources | dict | Assign all values from the sources into the target dictioanary. Mutates target dictionary. |
| entries | dct | generator | Creates a generator of all key value pairs in the dictionary. |
| str_count | string, target, start = 0, end = None | int | Count the number of times a target string appears in a string. |
| endswith | string, target | bool | Check to see if the target string is the end of the string. |
| repeat | string, n | str | Repeat a string 'n' number of times. |
| replace | string, target, replacement, n = None | str | Replace a target string with a replacement string 'n' number of times. |

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
