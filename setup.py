from setuptools import setup

with open("son/__about__.py") as f:
    exec(f.read())

setup(
    name=__title__,
    version=__version__,
    description=__summary__,
    long_description=__readme__,
    long_description_content_type="text/markdown",
    url=__url__,
    author=__author__,
    license=__license__,
    packages=["son"],
)
