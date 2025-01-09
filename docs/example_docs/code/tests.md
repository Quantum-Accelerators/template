# Testing

## Overview

Writing effective tests for your code is a crucial part of the programming process. It is the best way to ensure that changes you make to your codebase throughout the development process do not break the core functionality of your code. This may be your first time writing tests, but trust me that it is essential.

## Pytest

Put any unit tests in the `/tests` folder. A sample test (i.e. `/tests/sample/examples/test_sample.py`) is included as a representative example.

!!! Note

    All your testing scripts should start with `test_` in the filename.

When you installed the package with the `[dev]` extras, you installed everything you need to run your unit tests. To run the unit tests locally, run `pytest .` in the base directory. It will let you know if any tests fail and what the reason is for each failure.

## Code Coverage

The `/.codecov.yml` file is a configuration file for [Codecov](https://codecov.io/), which will tell you the fraction of lines covered by your test suite if the GitHub integration is enabled.

In order for Codecov to work properly, you will need to make a Codecov account and activate it on your newly made repository. You will also need to add the `CODECOV_TOKEN` [secret](https://docs.codecov.com/docs/adding-the-codecov-token) to your repository.
