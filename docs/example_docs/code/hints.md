# Type Hinting

## Overview

In the sample functions provided with the template repository, you will see something like:

```
def make_array(val: float, length: int = 3) -> NDArray:
```

If you aren't familiar with [type-hinting](https://docs.python.org/3/library/typing.html), that's what the `: float`, `: int`, and `-> NDArray` are indicating. They tell the user what the expected types are for each parameter and return. They are not enforced in any way; they are merely hints (as the name suggests). It is always advisable to use type hints in your code, so get in the habit of doing so!

!!! Tip

    If you have to import a given function solely for type-hinting purposes, you should put it within an [`if TYPE_CHECKING` block](https://docs.python.org/3/library/typing.html#typing.TYPE_CHECKING) (as demonstrated in `/src/template/examples/sample.py`). It will then only be imported when using a type-checking utility, reducing the overall import time of your module.

!!! Note

    You do not need to touch the `py.typed` file. It is a marker that Python uses to indicate that type-hinting should be used in any programs that depend on your code.

## Type Checking

As mentioned, the type hints are just that: hints. If you want to ensure that the types are strictly adhered to across your codebase, you can use [mypy](https://mypy-lang.org/) to do so. This is a slightly more advanced tool, however, so is not something you need to worry about right now.
