"""Sphinx configuration."""
project = "Todo Cli"
author = "Kinervaaa"
copyright = "2026, Kinervaaa"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
