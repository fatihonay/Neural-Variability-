# conf.py
import os
import sys

# Basic project information
project = 'Neural Variability Research'
copyright = '2026, Fatih Onay, PhD'
author = 'Fatih Onay'

# Extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'myst_parser',  # for markdown support
]

# Theme
html_theme = 'pydata_sphinx_theme'

# Minimal theme options for instant style
html_theme_options = {
    "logo": {
        "text": "Neural Variability",
    },
    "github_url": "https://github.com/fatihonay/Neural-Variability-",
    "show_toc_level": 2,
    "navigation_with_keys": True,
    "navbar_align": "left",  # Better for doc-heavy sites
}

# Source and build directories
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_static_path = ['_static']

