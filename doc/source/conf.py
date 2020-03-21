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

# sys.path.insert(0, os.path.abspath('.'))

if os.getenv("USE_DOXYREST"):
    # path for doxyrest sphinx extensions
    sys.path.insert(
        1, "{:s}/share/doxyrest/sphinx".format(os.getenv("DOXYREST_PREFIX"))
    )

    import doxyrest

import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = "CTP7 Modules"
copyright = "2020, CMS GEM DAQ Project"
author = "CMS GEM DAQ Project"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
try:
    print(
        "Version is ",
        os.popen("git describe --abbrev=6 --dirty --always --tags").read().strip(),
    )
    release = re.sub(
        "^v",
        "",
        os.popen("git describe --abbrev=6 --dirty --always --tags").read().strip(),
    )  #'1.0.0'
except:
    release = "0.0.0"

# The short X.Y version.
version = "{0}.{1}".format(*release.split("."))  #'1.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinxcontrib.srclinks",
    "sphinx_rtd_theme",
]

if os.getenv("USE_DOXYREST"):
    extensions += ["doxyrest", "cpplexer"]
else:
    extensions += ["breathe", "exhale"]
    breathe_projects = {
        "CTP7 Modules": "../exhalebuild/xml/",
    }

    breathe_default_project = "CTP7 Modules"

    # Setup the exhale extension
    exhale_args = {
        # These arguments are required
        "containmentFolder": "./exhale-api",
        "rootFileName": "api.rst",
        "rootFileTitle": "CTP7 modules API documentation",
        "doxygenStripFromPath": "..",
        # Suggested optional arguments
        "createTreeView": True,
        # TIP: if using the sphinx-bootstrap-theme, you need
        "treeViewIsBootstrap": True,
        "exhaleExecutesDoxygen": True,
        "exhaleDoxygenStdin": """
PROJECT_NAME = CTP7 Modules
PROJECT_NUMBER = {}
INPUT = ../../include \
        ../../src
PREDEFINED+= DOXYGEN_IGNORE_THIS
""".format(
            os.popen("git describe --abbrev=6 --dirty --always --tags").read().strip()
        ),
    }

# Tell sphinx what the primary language being documented is.
primary_domain = "cpp"

# Tell sphinx what the pygments highlight language should be.
highlight_language = "cpp"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output -------------------------------------------------

html_context = {
    "display_gitlab": True,
    "gitlab_host": "gitlab.cern.ch",
    "gitlab_user": "cms-gem-daq-project",
    "gitlab_repo": "ctp7_modules",
    "gitlab_version": "release/legacy-1.1",  ## grab this dynamically
    "conf_py_path": "/doc/source/",
}

html_show_sourcelink = True

## Set an image file to be used as a logo at the top of the sidebar
# html_logo

## Show only the logo at the top of the sidebar
# logo_only

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom CSS
# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    "css/custom.css",
]

# Custom JavaScript
# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_js_files = [
    # 'js/custom.js',
]
