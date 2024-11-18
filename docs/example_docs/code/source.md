# Source Code

## Adding Your Code

All source code (i.e. your various modules, functions, classes, and so on) should be placed in the `/src/<MyPackageName>` directory. A sample file named `examples/sample.py` is included here as a representative example, which you should replace.

All the code in the `src` directory can be imported now that you have installed your package.

!!! Tip

    As an example, you can import and use the demonstration [template.examples.sample][] functions as follows:

    ```python
    from MyPackageName.examples.sample import add, make_array

    print(add(1, 2))  # 3
    print(make_array(3, length=4))  # [3, 3, 3, 3]
    ```

!!! Note

    For any subfolder within `src/<MyPackageName>` containing Python code, you must have an `__init__.py` file, which will tell Python that this is a module you can import.

## Docstrings

The code comments beneath each function are called docstrings. They should provide an overview of the purpose of the function, the various parameters, and the return values (if any). Here, we are using the [NumPy style](https://numpydoc.readthedocs.io/en/latest/format.html) docstrings, but you can pick a different style if you like later on.

## Linting and Formatting

When you installed the `[dev]` dependencies, you also installed [`ruff`](https://docs.astral.sh/ruff/), which is a versatile Python linter to clean up your code. To run `ruff`, use the following command in the base directory: `ruff check --fix`. This will also be done automatically on pull requests via the pre-commit CI tool.
