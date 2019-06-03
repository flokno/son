from setuptools import setup

with open("son/__about__.py") as f:
    exec(f.read())

setup(name="son", version=__version__, packages=["son"])
