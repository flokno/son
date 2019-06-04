import pathlib

__all__ = [
    "__title__",
    "__summary__",
    "__url__",
    "__version__",
    "__commit__",
    "__author__",
    "__license__",
    "__copyright__",
]

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The root directory
ROOT = HERE.parent

# The text of the README file
__readme__ = (ROOT / "README.md").read_text()


__title__ = "son"
__summary__ = "Tools to read and write .son file"
__url__ = "https://github.com/flokno/son"

__version__ = "0.1.2"
__short_version__ = "0.1"

__author__ = "Florian Knoop"

__license__ = "ISC"
__copyright__ = "2019 %s" % __author__
