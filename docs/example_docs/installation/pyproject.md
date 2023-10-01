# pyproject.toml

The `pyproject.toml` file contains all of the necessary information on how Python will install your package.

## Metadata

There are several metadata-related fields that you will likely want to update. You should have already updated the `name` of the package in a prior step when you replaced "template" everywhere, but you will also want to change the following:

- `description`
- `license` (if you changed the default `LICENSE.md` file)
- `authors`
- `keywords`

Aside from the `name`, none of the above are strictly necessary and can be left as-is (or removed) if you are unsure.

## Dependencies

The most important fields to update are related to the dependencies: the Python packages that your own code relies on. This will ensure that they are automatically installed when installing your Python package.

The required dependencies are listed under the `[project]` header in the `dependencies` field. By default, the template repository lists `["numpy"]`. Include any dependencies you want in this list, separated by commas. This should be all the packages you import in your code that are not standard Python libraries.

!!! Tip

    Not sure what dependencies you need just yet? No problem. You can come back to this later.

!!! Note

    If you know a specific minimum version is needed for your code, you should set that here as well (e.g. `["numpy>=1.23.0"]`). However, only use this when it is necessary so that users aren't restricted to a given version without a valid reason.

## Python Version

If you know your code can only run on certain Python versions, you should specify that in the `requires-python` field under the `[project]` header. When in doubt, we recommend setting it to the range of [currently supported Python versions](https://devguide.python.org/versions/#versions) (specifically those with security and bugfix statuses).

You can also update the listed versions in the `classifiers` field, although this is only for informational purposes. The list of supported Python classifier fields can be found on the corresponding [PyPI page](https://pypi.org/classifiers/).
