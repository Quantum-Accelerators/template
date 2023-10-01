# Documentation

## Mkdocs

Now it's time to write some documentation! This isn't very difficult, and of course you're reading some documentation right now. The documentation is written using markdown, which is the same way GitHub comments are formatted.

!!! Tip

    Check out the [Markdown Guide](https://www.markdownguide.org/basic-syntax/) for an overview of the basic syntax.

This template repository uses a documentation format called mkdocs, specifically a useful theme called [Material for Mkdocs](https://squidfunk.github.io/mkdocs-material/). This enables many wonderful goodies like the "tip" callout you see above and much more.

## Adding Markdown Files

Your documentation will live in the [`/docs`](../../docs/) folder. You can think of each markdown (`.md`) file as being a specific page in the documentation, and each folder as being a related collection of pages. The markdown page you are reading right now is found at `/docs/example_docs/mkdocs/docs.md`, for instance. Of course, you will want to replce the `/docs/example_docs` folder with your own documentation.

!!! Note

    You typically do not need to touch the `/docs/gen_ref_pages.py` script. It is used to automatically build the documentation for your code from its docstrings.

## The `mkdocs.yml` File

Once you have added your documentation, you will need to update the [`mkdocs.yml`](../../../mkdocs.yml) file with information about how you want to arrange the files. Specifically, you will need to update the `nav` secction of the `mkdocs.yml` file to point to all your individual `.md` files, organizing them by category.

!!! Note

    Keep the `- Code Documentation: reference/` line in the `nav` section of `mkdocs.yml`. It will automatically transform your docstrings into beautiful documentation! The rest of the `nav` items you can replace.

## Building the Documentation Locally

To see how your documentation will look in advance, you can build it locally by running the following command in the base directory:

```bash
mkdocs serve
```

A URL will be printed out that you can open in your browser.
