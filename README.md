# Mock Scenario

## Example 1

```
./run.sh example1_test.py

```

```
=================== test session starts =========
platform darwin -- Python 3.8.12, pytest-7.2.0, pluggy-1.0.0 -- /Users/jason-kuan/miniconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/astra-jason-kuan/workspace/temp
plugins: cov-4.0.0
collected 2 items

example1_test.py::test_main_good program start.
I will run very long.
PASSED
example1_test.py::test_main_bad program start.
I will run very long.
PASSED

=================== 2 passed in 10.06s ==========
```

## Example 2

```
./run.sh example2_test.py

```

```
=================== test session starts =========
platform darwin -- Python 3.8.12, pytest-7.2.0, pluggy-1.0.0 -- /Users/jason-kuan/miniconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/astra-jason-kuan/workspace/temp
plugins: cov-4.0.0
collected 2 items

example2_test.py::test_main_good program start.
PASSED
example2_test.py::test_main_bad program start.
PASSED

=================== 2 passed in 0.06s ===========
```
