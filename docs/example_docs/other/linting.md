# Linting and Formatting

## Overview

When you installed the `[dev]` dependencies, you installed several code-formatting and linting tools, including:

1. [`black`](https://black.readthedocs.io/en/stable/): A very useful and opinionated code formatter, which you can use by running `black .` in the base directory.
2. [`isort`](https://pycqa.github.io/isort/): A utility that will sort your import statements for you, which you can use by running `isort .` in the base directory.
3. [`ruff`](https://docs.astral.sh/ruff/): A versatile Python linter to clean up your code, which you can use by running `ruff . --fix` in the base directory.
4. [`docformatter`](https://github.com/PyCQA/docformatter): A simple docstring formatter, which you can use by running `docformatter . -r -i` in the base directory.

Modifications to the rules these formatters use can be defined in the `pyproject.toml` file, and we have chosen some useful defaults.
