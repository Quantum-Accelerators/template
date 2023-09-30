# template

A template for Python packages. Developed by the [@quantum-accelerators](https://github.com/Quantum-Accelerators)

Check out the [YouTube tutorial](https://www.youtube.com/watch?v=th2CqJ6oBuM)!

## Instructions

1. [Create a new repository](https://github.com/new?template_name=template&template_owner=Quantum-Accelerators) using this template.
2. Update the [`README.md`](README.md) as desired.
3. Replace all instances of the word "template" with your package name, including the [`src/template`](src/template) folder and all entries of `template` in the various files (e.g. by using `Ctrl+Shift+H` to find-and-replalce in VS Code).
4. Update the [`pyproject.toml`](pyproject.toml) file to suit your package, such as specifying any necessary `dependencies` (which is set to `["numpy"]` by default). You can always edit this later if you're not sure.
5. Install the package in editable mode, including the development and documentation dependencies so you can run unit tests and build the documentation. This is done by running `pip install -e .[dev,docs]` in the base directory, ideally in a fresh Python environment.
6. Put any source code in the `src/<package name>` directory. A sample file named [`sample.py`](src/template/sample.py) is included here as a representative example.
7. Put any unit tests in [`tests`](tests). A [sample test](tests/sample/test_sample.py) is included as a representative example, along with a [`requirements.txt`](tests/requirements.txt) file that the GitHub actions continuous integration testing suite will use. To run the unit tests locally, run `pytest .` in the base directory.
8. Put any documentation in [`docs`](docs) with the desired layout specified in the `nav` secction of the [`mkdocs.yml`](mkdocs.yml) file in the base directory. To build the documentation, run `mkdocs serve` in the base directory.

You now have everything you need to make a robust and sustainable Python package!
