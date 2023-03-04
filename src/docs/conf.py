import sys
import platform
from pathlib import Path

sys.path.insert(0, str(Path("../../src").absolute()))
platform_name = platform.system()  # Windows, Darwin, Linux

project = "My memo"
copyright = "Shunya Sasaki"
author = "Shunya Sasaki"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.imgmath",
    "sphinx.ext.ifconfig",
    "sphinx.ext.imgconverter",
    "sphinxcontrib.blockdiag",
    "sphinxcontrib.mermaid",
    "sphinx_copybutton",
]
language = "en"
html_theme = "sphinx_material"
html_static_path = ["_static"]
templates_path = ["_templates"]
exclude_patterns = []
pygments_style = "monokai"
pygments_dark_style = "monokai"
html_style = 'custom.css'

# internationalize
locale_dirs = ['locale/']
gettext_compact = False

# theme setting for sphinx-rtd-theme
if html_theme == "sphinx_rtd":
    html_theme_options = {
        "logo_only": False,
        "display_version": True,
        "prev_next_buttons_location": "border",
        "style_external_links": False,
        "vcs_pageview_mode": "",
        "collapse_navigation": False,
        "sticky_navigation": True,
        "navigation_depth": 4,
        "includehidden": True,
        "titles_only": False,
    }
elif html_theme == "sphinx_material":
    html_theme_options = {
        # Set the name of the project to appear in the navigation.
        "nav_title": project,
        "html_minify": True,
        "css_minify": True,
        # 'google_analytics_account': 'UA-XXXXX',
        # 'base_url': 'https://project.github.io/project',
        # 'color_primary': 'blue',
        # 'color_accent': 'light-blue',
        # Set the repo location to get a badge with stats
        "repo_url": "https://github.com/shunya-sasaki/my-note",
        "repo_name": project,
        "globaltoc_depth": 2,
        "globaltoc_collapse": False,
        "globaltoc_includehidden": False,
    }
    html_sidebars = {
        "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
    }

# mermaid
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
mathjax3_config = {"chtml": {"displayAlign": "left"}}
mermaid_init_js = (
    "mermaid.initialize({ startOnLoad: true,"
    + "'theme': 'base', "
    + "'flowchart': {'curve': 'linear'}, "
    + "'themeVariables': {'primaryColor': '#82A0AA', "
    + " 'primaryTextColor': '#ffffff', "
    + " 'primaryBorderColor': '#82A0AA', "
    + " 'lineColor': '#E31F26', "
    + " 'secondaryColor': '#223F4B', "
    + " 'tertiaryColor': '#C8DDE6', "
    + " }, "
    + "});"
)

# blockdiag and actdiag
blockdiag_html_image_format = "SVG"
blockdiag_html_image_format = "SVG"
if platform_name == "Darwin":
    blockdiag_fontpath = "/System/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc"
    actdiag_fontpath = "/System/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc"
elif platform_name == "Linux":
    blockdiag_fontpath = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
    actdiag_fontpath = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
else:
    blockdiag_fontpath = r"C:\Windows\Fonts\meiryo.ttc"
    actdiag_fontpath = r"C:\Windows\Fonts\meiryo.ttc"

# Latex
latex_docclass = {"mymanual": "jsreport"}
latex_domain_indices = False
latex_elements = {
    "papersize": "a4paper",
    "extraclassoptions": "openany",
    "fncychap": r"\usepackage[Sonny]{funcychap}",
    "preamble": r"""
    \usepackage{graphicx}
    """,
    "sphinxsetup": r"""
    noteBorderColor={HTML}{006487},
    warningBorderColor={HTML}{dc6914},
    warningBgColor={HTML}{fbe0cc}
    """,
}
