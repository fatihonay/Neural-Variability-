# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Neural Variability'
copyright = '2026, Fatih Onay, PhD'
author = 'Fatih Onay, PhD'
release = 'v1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme' #'alabaster'
html_static_path = ['_static']


# docs/source/conf.py

extensions = [
    'myst_parser',        # For Markdown support
    'nbsphinx',           # For Jupyter Notebooks
    'sphinx.ext.mathjax', # <--- REQUIRED: Renders the math
]

# <--- ADD THIS BLOCK TO ENABLE $$$ MATH
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
]
