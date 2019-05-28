son | sequential object notation
===
## What is this?
_son_ is a data format that builds on [JSON](https://www.json.org/) and adds one 
feature from [YAML](https://yaml.org/): concatenation of objects with `---`.
## Why _son_?
While JSON is perfect for storing structured data, it is inherently impossible
to add new portions of data to a file without reading it first. YAML files are
self extensible by the `---` delimiter, but the flexibility it offers makes it
inefficient to parse.

_son_ fills the gap by allowing JSON objects to be concatenated with `---`.

### Example
This is a valid _son_ string:
```yaml
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

## Advantages
- __Sequential__: _son_ extends JSON to make it perfectly sequential.
- Valid YAML: since _son_ only adds one syntactic feature from YAML to JSON, it is a minimal 
superset of JSON, and as such still valid YAML.
- __Speed__: Compared to YAML, the feature set is restricted, making _son_ as fast to parse as JSON.