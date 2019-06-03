son | sequential object notation
===

## What is this?
_son_ is a data format that builds on [JSON](https://www.json.org/) and adds one 
feature inspired by [YAML](https://yaml.org/): concatenation of objects with 
`---`.  Optionally, the delimiter `===` can be used once per _son_ file to delimit 
metadata.

## Why _son_?
While JSON is perfect for storing structured data, it is inherently impossible
to add new portions of data to a file without reading it first. YAML files on 
the other hand are self extensible by the `---` delimiter, but the flexibility 
YAML offers makes the files inefficient to parse. They are thus unsuited to 
store significant amounts of data.

_son_ fills the gap by allowing JSON objects to be concatenated with `---`. It
thus combines the speed and efficiency of JSON with the sequential extensibility
of YAML, see [example](#Example). It further adds to discern metadata from 
actual data by using `===`.

## Who needs this?
_son_ originated from the need to store computational data that is produced
portion by portion on a computer. The requirements were:
- Possible to be read by a human,
- possible to store arbitrary data structures _including_ metadata,
- easy to write and parse by a computer,
- efficient to parse to allow files of up to GB size (takes forever to parse with YAML),
- 100% sequential and incorruptible.


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
import son

metadata, data = son.load('file.son')
```
