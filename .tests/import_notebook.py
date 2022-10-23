#!/usr/bin/env python3


"""Load the code-cells of a jupyter notebook."""


import pathlib
import types

import nbformat


NOTEBOOK_PATH = pathlib.Path(__file__).absolute().parent.parent


def import_notebook(path):
    path = pathlib.Path(path)
    if not path.exists():
        # see if path is relative?
        path = NOTEBOOK_PATH / path

    notebook = nbformat.read(str(path), as_version=nbformat.NO_CONVERT)

    namespace = {}
    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            try:
                exec(cell["source"], namespace)
            except Exception as exception:  # ignore any cell that has any error
                with open("/tmp/import-error.debug", "a") as f:
                    print(cell["source"], file=f)
                pass

    del namespace["__builtins__"]
    namespace = types.SimpleNamespace(**namespace)
    with open("/tmp/namespace.debug", "a") as f:
        print(namespace, file=f)
    return namespace
