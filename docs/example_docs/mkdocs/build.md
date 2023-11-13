# Building the Docs

## The `mkdocs.yml` File

Once you have added your documentation, you will need to update the `/mkdocs.yml` file with information about how you want to arrange the files. Specifically, you will need to update the `nav` secction of the `mkdocs.yml` file to point to all your individual `.md` files, organizing them by category.

!!! Note

    Keep the `- Code Documentation: reference/` line in the `nav` section of `mkdocs.yml`. It will automatically transform your docstrings into beautiful documentation! The rest of the `nav` items you can replace.

## The Build Process

To see how your documentation will look in advance, you can build it locally by running the following command in the base directory:

```bash
mkdocs serve
```

A URL will be printed out that you can open in your browser.

## Deploying the Docs

To allow your documentation to be visible via GitHub Pages, go to "Settings > Pages" in your repository's settings and make sure "Branch" is set to "gh-pages" instead of "main".
