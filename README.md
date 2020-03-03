son | sequential object notation
===

![python](https://img.shields.io/badge/python-3.5--3.7-lightgrey.svg?style=flat-square)
[![pypi](https://img.shields.io/pypi/v/son.svg?style=flat-square)](https://pypi.org/project/son/)
![license](https://img.shields.io/pypi/l/son.svg?color=red&style=flat-square)
[![code style](https://img.shields.io/badge/code%20style-black-202020.svg?style=flat-square)](https://github.com/ambv/black)

_son_ is a data format that builds on [JSON](https://www.json.org/) and adds one 
feature inspired by [YAML](https://yaml.org/): concatenation of objects with 
`---`.  Optionally, the delimiter `===` can be used once per _son_ file to delimit 
metadata.

---

## Motivation

### Why _son_?

While JSON is perfect for storing structured data, it is inherently impossible
to add new portions of data to a file without reading it first. YAML files on 
the other hand are self extensible by the `---` delimiter, but the flexibility 
YAML offers makes the files inefficient to parse. They are thus unsuited to 
store significant amounts of data.

_son_ fills the gap by allowing JSON objects to be concatenated with `---`. It
thus combines the speed and efficiency of JSON with the sequential extensibility
of YAML, see [example](README.md#example). It further adds to discern metadata from 
actual data by using `===`.

_son_ does **not** allow to overwrite data. In order to avoid accidental data loss,
metada can only be written to fresh files, whereas data can only be appended to files.

### Who needs this?

_son_ originated from the need to store computational data that is produced
portion by portion on a computer. The requirements were:

- Possible to be read by a human,
- possible to store arbitrary data structures _including_ metadata,
- easy to write and parse by a computer,
- efficient to parse to allow files of up to GB size (takes forever to parse with YAML),
- sequential and incorruptible,
- resilient to data loss.

_son_ is targeted at users who would like to store their data in a format meeting these requirements.

---

## Installation

_son_ can be installed from [pypi](https://pypi.org/) via
```
pip install son
```

---


## Example

This is a valid _son_ string:

```yaml
{
  "purpose": "store biography data",
  "version": 0.1
}
===
{
  "first name": "Hildegard",
  "second name": "Kneef",
  "age": 93
}
---
{
  "first name": "Wiglaf",
  "second name": "Droste",
  "age": 57
}
```

It will be parsed into the metadata object, and a list containing the data objects with

```python
>>> import son
>>> metadata, data = son.load('test.son')
>>> print(metadata)
{'purpose': 'store biography data', 'version': 0.1}
>>> print(data)
[{'first name': 'Hildegard', 'second name': 'Kneef', 'age': 93}, {'first name': 'Wiglaf', 'second name': 'Droste', 'age': 57}]
```

--- 

## Changelog

v0.3.3: Add documentation via [`mkdocs`](https://www.mkdocs.org/) and [`mkdocs-material`](https://squidfunk.github.io/mkdocs-material/)

v0.3.2: fix for interactively working in `ipython` console

v0.3.1: inform _before_ file is read, makes more sense when that takes some time

v0.3.0: support for reading compressed `.bz2` and `.gz` files

v0.2.5: progressbar is only shown when a terminal is attached (`.isatty()`)

v0.2.4: progressbar without external dependency

v0.2.3: `progress.bar` prints to `stdout` instead of `stderr`

v0.2.2: optionally be verbose and show progressbar with `progress` package (optional dependency, install with `pip install son[progress]`)
