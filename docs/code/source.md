# Source Code

## Adding Your Code

All source code (i.e. your various modules, functions, classes, and so on) should be placed in the [`src/<MyPackageName>`](../../src/template/) directory. A sample file named [`sample.py`](src/template/sample.py) is included here as a representative example, which you should replace.

All the code in the `src` directory can be imported now that you have installed your package.

!!! Tip

    As an example, you can import and use the demonstration `sample.py` functions as follows:

    ```python
    from MyPackageName.sample import add, make_array

    print(add(1, 2)) # 3
    print(make_array(3, length=4)) # [3, 3, 3, 3]
    ```

!!! Note

    For any subfolder within `src/<MyPackageName>` containing Python code, you must have an `__init__.py` file, which will tell Python that this is a module you can import.

## Docstrings

The code comments beneath each function are called docstrings. They should provide an overview of the purpose of the function, the various parameters, and the return values (if any). Here, we are using the [NumPy style](https://numpydoc.readthedocs.io/en/latest/format.html) docstrings, but you can pick a different style if you like later on.

## Type Hinting

In the sample functions, you will see something like:

```python
def make_array(val: float, length: int = 3) -> NDArray:
```

If you aren't familiar with [type-hinting](https://docs.python.org/3/library/typing.html), that's what the `: float`, `: int`, and `-> NDArray` are indicating. They tell the user what the expected types are for each parameter and return. They are not enforced in any way; they are merely hints (as the name suggests). It is always advisable to use type hints in your code, so get in the habit of doing so!

!!! Tip

    If you have to import a given function solely for type-hinting purposes, you should put it within an [`if TYPE_CHECKING` block](https://docs.python.org/3/library/typing.html#typing.TYPE_CHECKING) (as demonstrated in [`sample.py`](src/template/sample.py)). It will then only be imported when using a type-checking utility, reducing the overall import time of your module.

!!! Note

    You do not need to touch the `py.typed` file. It is a marker that Python uses to indicate that type-hinting should be used in any programs that depend on your code.
