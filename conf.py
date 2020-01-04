# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Showcuts'
copyright = '2019, MIGI'
author = 'MIGI'

# The full version, including alpha/beta/rc tags
release = '2020.0.0'


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc', 
    'recommonmark',
    'sphinx_paramlinks',
]



# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store',
    'staticfiles', # Static Files
    '.pytest_cache', # pyc
    'oe_sphinx', # theme
    'README',
]

# Theme Override
# html_theme = 'alabaster'
html_theme = 'classic'
html_theme_path = ['.']


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# custom master doc
master_doc = 'index'

# turn off module names
add_module_names = False
