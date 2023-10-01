# Testing

Writing effective tests for your code is a crucial part of the programming process. It is the best way to ensure that changes you make to your codebase throughout the development process do not break the core functionality of your code. This may be your first time writing tests, but trust me that it is essential.

8. Put any unit tests in [`tests`](tests). A [sample test](tests/sample/test_sample.py) is included as a representative example, along with a [`requirements.txt`](tests/requirements.txt) file that the GitHub actions continuous integration testing suite will use. To run the unit tests locally, run `pytest .` in the base directory.
