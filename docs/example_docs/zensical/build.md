# Building the Docs

!!! Note

    This documentation refers to `zensical.toml` at several places. You may find that this repository has a `_zensical.toml` file instead. This is because Zensical is a very new project and still evolving. Before it matures into a fully-functional product, we'll be running a couple of scripts in the `.github/scripts` folder to convert this `_zensical.toml` to a final `zensical.toml` file. This extra manual step will go away soon (as will this note!). For the time being, you can assume that anything you read here in the context of `zensical.toml` applies to `_zensical.toml` interchangeably.

## The `zensical.toml` File

Once you have added your documentation, you will need to update the `/zensical.toml` file with information about how you want to arrange the files. Specifically, you will need to update the `nav` secction of the `zensical.toml` file to point to all your individual `.md` files, organizing them by category.

!!! Note

    Keep the `- Code Documentation: reference/` line in the `nav` section of `zensical.toml`. It will automatically transform your docstrings into beautiful documentation! The rest of the `nav` items you can replace.

## The Build Process

To see how your documentation will look in advance, you can build it locally by running the following command in the base directory:

```bash
python .github/scripts/gen_ref_pages.py
python .github/scripts/gen_zensical_toml.py
zensical serve
```

A URL will be printed out that you can open in your browser.

## Deploying the Docs

To allow your documentation to be visible via GitHub Pages, go to "Settings > Pages" in your repository's settings and make sure "Branch" is set to "gh-pages" instead of "main".
