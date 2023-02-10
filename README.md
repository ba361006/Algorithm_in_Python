# Algorithm_in_Python

# Intro:
To make both task itself and its test workable, I put the following code to every file's head to avoid ImportError
```python
import os
import sys

sys.path.append(os.path.abspath("."))
```

# linter check
- Mac OS user
    > run `chmod +x ./linter_check.sh` at the root directory to solve `permission denied` error
    - run `./linter_check.sh` at root directory, it will execute both `mypy` and `pylint`

# unit test
- Mac OS user
    > run `chmod +x ./tests.sh` at the root directory to solve `permission denied` error
    > run `./tests.sh` at root directory to run all the unit tests