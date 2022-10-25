#!/usr/bin/env python3


"""Load the code-cells of a jupyter notebook."""


import types

import nbformat


def import_notebook(path):
    notebook = nbformat.read(str(path), as_version=nbformat.NO_CONVERT)

    namespace = {}
    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            try:
                exec(cell["source"], namespace)
            except Exception:  # ignore any cell that has any error
                pass

    del namespace["__builtins__"]
    namespace = types.SimpleNamespace(**namespace)
    return namespace
