# Miscellaneous

## Code Formatting

When you installed the `[dev]` dependencies, you installed several code-formatting tools, including:

1. [`black`](https://black.readthedocs.io/en/stable/): A very useful and opinionated code formatter, which you can use by running `black .` in the base directory.
2. [`isort`](https://pycqa.github.io/isort/): A utility that will sort your import statements for you, which you can use by running `isort .` in the base directory.
3. [`ruff`](https://docs.astral.sh/ruff/): A versatile Python linter to clean up your code, which you can use by running `ruff . --fix` in the base directory.

Modifications to the rules these formatters use can be defined in the `pyproject.toml` file, and we have chosen some useful defaults.

## Optional Apps

There are also several configuration files for popular third-party applications that can be quite useful:

1. The [`.deepsource.toml`](../../.deepsource.toml) file is a configuration file for the web platform [DeepSource](https://deepsource.com/), which has a useful GitHub extension for cleaning up your code and spotting common errors.
2. The `[.sourcery.yaml]`(../../.sourcery.yaml) file is a configuration file for [Sourcery](https://sourcery.ai/), which can automatically refactor your code.
3. The `[.codecov.yml]`(../../.codecov.yml) file is a configuration file for [Codecov](https://codecov.io/), which will tell you the fraction of lines covered by your test suite if the GitHub integration is enabled.
