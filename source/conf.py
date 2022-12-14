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

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

html_theme_options = {
  "github_url": "https://github.com/Jon-Pham",
  "icon_links": [
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/in/jonathan-pham-9a553b22a/",
            "icon": "fa-brands fa-linkedin",
        },        
        ],
  "search_bar_text": "Search this site...",
}

# -- Sidebar Options for HTML output -------------------------------------------------
html_sidebars = {'index': ['sidebar.html'],
                 'about': ['sidebar.html'],
                 'publications': ['sidebar.html'],
                 'blog': ['tagcloud.html', 'archives.html'],
}


# -- Blog -------------------------------------------------
extensions += ['ablog']
blog_title = "Mon Blog"
blog_path = "blog"
fontawesome_included = True
blog_post_pattern = "posts/*/*"
