import os.path

__all__ = [
    "__title__",
    "__summary__",
    "__uri__",
    "__version__",
    "__commit__",
    "__author__",
    "__license__",
    "__copyright__",
]


try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    base_dir = None


__title__ = "son"
__summary__ = "Tools to read and write .son file"
__uri__ = "https://github.com/flokno/son"

__version__ = "0.1.0"
__short_version__ = "0.1"

if base_dir is not None and os.path.exists(os.path.join(base_dir, ".commit")):
    with open(os.path.join(base_dir, ".commit")) as fp:
        __commit__ = fp.read().strip()
else:
    __commit__ = None

__author__ = "Florian Knoop"

__license__ = "ISC License"
__copyright__ = "2019 %s" % __author__
