# template

A template for Python packages. **Check out the corresponding ⭐[YouTube tutorial](https://www.youtube.com/watch?v=th2CqJ6oBuM)⭐ for full details!**

## Instructions

1. [Create a new repository](https://github.com/new?template_name=template&template_owner=Quantum-Accelerators) using this template.
2. [Clone the repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to your local machine.
3. Update the [`README.md`](README.md) as desired.
4. Replace all instances of the word "template" with your package name, including the name of the [`src/template`](src/template) folder and all entries of "template" in the various files (e.g. by using `Ctrl+Shift+H` to find-and-replalce in [VS Code](https://code.visualstudio.com/)).
5. Update the [`pyproject.toml`](pyproject.toml) file to suit your package, most notably specifying any necessary `dependencies` (which is set to `["numpy"]` by default). You can always edit this later if you're not sure yet.
6. Install the package in editable mode, including the development and documentation dependencies so you can run unit tests and build the documentation. This is done by running `pip install -e .[dev,docs]` in the base directory, ideally in a fresh Python environment.
7. Put any source code in the `src/<package name>` directory. A sample file named [`sample.py`](src/template/sample.py) is included here as a representative example.
8. Put any unit tests in [`tests`](tests). A [sample test](tests/sample/test_sample.py) is included as a representative example, along with a [`requirements.txt`](tests/requirements.txt) file that the GitHub actions continuous integration testing suite will use. To run the unit tests locally, run `pytest .` in the base directory.
9. Put any documentation in [`docs`](docs) with the desired layout specified in the `nav` secction of the [`mkdocs.yml`](mkdocs.yml) file in the base directory. To build the documentation locally, run `mkdocs serve` in the base directory.
10. Commit any changes you've made and push them to your repository, ideally using a program like [GitKraken](https://www.gitkraken.com/) or [GitHub Desktop](https://desktop.github.com/).

You now have everything you need to make a robust and sustainable Python package!
