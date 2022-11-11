# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'my portfolio'
copyright = '2022, Jonathan Pham'
author = 'Jonathan Pham'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser"]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']


html_theme_options = {
  "github_url": "https://github.com/vferat/",
  "icon_links": [
        {
            "name": "Twitter",
            "url": "https://twitter.com/ferat_victor",
            "icon": "fa-brands fa-twitter",
        },
        {
            "name": "ORCID",
            "url": "https://orcid.org/0000-0003-1952-7657",
            "icon": "fa-brands fa-orcid",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/in/victor-ferat/",
            "icon": "fa-brands fa-linkedin",
        },        
        ],
  "search_bar_text": "Search this site...",
}