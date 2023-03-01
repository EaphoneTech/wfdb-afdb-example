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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "wfdb-afdb-example"
copyright = "2023, 广州易风健康科技股份有限公司"
author = "Xiaoyu Guo"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "nbsphinx",
    "recommonmark",
    "sphinx_rtd_theme",
    "sphinx_last_updated_by_git",
    "sphinx_markdown_tables",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "zh_CN"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# nbsphinx

nbsphinx_allow_errors = True


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# If this is not None, a ‘Last updated on:’ timestamp is inserted at every page bottom,
# using the given strftime() format. The empty string is equivalent to '%b %d, %Y' (or a locale-dependent equivalent).
html_last_updated_fmt = "(本页) %Y-%m-%d %H:%M:%S"

# If true, the reST sources are included in the HTML build as `_sources/name`. The default is True.
html_copy_source = False

# If true (and `html_copy_source` is true as well), links to the reST sources will be added to the sidebar.
# The default is True.
html_show_sourcelink = False

html_theme_options = {
    "collapse_navigation": True,
    "sticky_navigation": True,
    "display_version": True,
    "navigation_depth": 4,
    "style_external_links": True,
}

html_search_language = "zh"

# plantuml
plantuml_output_format = "svg"
plantuml_latex_output_format = "eps"

# -- Customizing static files --------------------------------------------

# Adding static files (js, css)
