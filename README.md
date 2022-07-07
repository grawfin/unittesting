# Write a test for a "fizz buzz" function, then implement it

The goal is to write a Python function

```
def fizz_buzz(n: int): -> str
```
according to:

* If n is divisible by 15, return `"fizz buzz"` (0 should be
  considered to be divisible by 15).
* If n is divisible by 5 but not 3, return `"buzz"`.
* If n is divisible by 3 but not 5, return `"fizz"`.
* If n is not divisible by 3 or 5, return a string representation of
  the integer number, e.g. `"4"`.

## Step 1: Setup unit testing

* [ ] Create a new folder `fizz_buzz_exercise` and a virtual or conda environment for this
      exercise. This is the working directory for the following exercises.
* [ ] install `pytest` in this environment.
* [ ] copy the files `setup.py` and `setup.cfg` into the working folder.
* [ ] Create an empty script `src/fizz_buzz.py`.
* [ ] Create a folder `tests`.
* [ ] Create a file `test/test_fizz_buzz.py` which only includes `import fizz_buzz`
* [ ] Run `pip install -e .` to install the package in edit mode.
* [ ] Run `pytest tests/` to check if this import works.

## Step 2: Test Driven Development of the `fizz_buzz()` function

### General Case

* [ ] In `tests/test_fizz_buzz.py`, write a test that checks that the
      method `fizz_buzz()`
      returns a string representation for all input integer numbers in
      `{1, 2, 4, 7, 8, 11, 13, 14, 16, 17, 19, 22, 23, 26, 28, 29, 31}`.
* [ ] Write a minimal implementation (`return ""`) to make this test pass.

### Fizz

* [ ] Add a new test function to `tests/test_fizz_buzz.py` which checks that
      `fizz_buzz()` returns `"fizz"` if the argument is divisibly by
      3.
      Assure this for all integers in `{3, 6, 9, 12, 18, 21, 24, 27}`.
* [ ] Make sure, that the tests run, but fail.
* [ ] Modify the implementation in
      [./src/fizz_buzz.py](src/fizz_buzz.py), so it passes the test
      (again: simplest possible solution).

### Buzz

* [ ] Add a new test function to `tests/test_fizz_buzz.py` which checks that
      `fizz_buzz()` returns `"buzz"` if the argument is divisibly by
      5 but not 3.
      Assure this for all integers in `{5, 10, 20, 25}`.
* [ ] Make sure, that the tests run, but fail.
* [ ] Modify the implementation in
      [./src/fizz_buzz.py](src/fizz_buzz.py), so it passes the test
      (again: simplest possible solution).

### Fizz Buzz

* [ ] Add a new test function to `test/test_fizz_buzz.py` which checks that
      `fizz_buzz()` returns `"fizz buzz"` if the argument is divisibly by
      15.
      Assure this for all integers in `{0, 15, 30}`.
* [ ] Make sure, that the tests run, but fail.
* [ ] Modify the implementation in
      [./src/fizz_buzz.py](src/fizz_buzz.py), so it passes the test
      (again: simplest possible solution).

### Testing Corner cases

* [ ] Add a new test function to `test/test_fizz_buzz.py` which checks that
      `fizz_buzz()` raises an error for negative or non-integer arguments.
      See also [the pytest docs](https://docs.pytest.org/en/stable/reference/reference.html?highlight=raises#pytest.raises).
* [ ] Make sure, that the tests run, but fail.
* [ ] Modify the implementation in
      [./src/fizz_buzz.py](src/fizz_buzz.py), so it passes the test
      (again: simplest possible solution).
