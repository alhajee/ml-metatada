# ML Metadata

[![Python](https://img.shields.io/badge/python%20-3.7%7C3.8-blue)](https://github.com/alhajee/ml-medatada)

*ML Metadata* is a library for recording and retrieving metadata
associated with ML Models.

## Getting Started

The library is a work in progress, and at the moment [03-12-2021] there aren't much features but 
I'm confident that we'll make it better:
Current features:
+ Creating unique identifier for models
+ Logging model metadata
+ Saving & Loading metadata from Disk

Future Features:
+ Deleting saved metadata from disk
+ Generating expected data schema for model
+ Saving Features that are used in the model

## Usage

The recommended way to use ML Metadata is to import the relevant packages:

```python
from metadata import Metadata
```

### Sample

When the `load` flag is not provided the library creates a new metadata file, but when initialized
with `load=True`, it loads any saved metadata from disk.

```python
metadata = Metadata(load=True)

metadata.log_model("RNN Model", version="1.0.0", path="./models/", 
                    score=93.8, inputs= [0, 0, 0])

print(metadata.metadata)
```

### Sample Output
```python
{'features': [], 'schema': [], 'models': {'c79b989619c4db2da69b5f731980a56f': {'name': 'RNN Model', 'version': '1.0.0', 'path': './models/', 'score': 93.8, 'inputs': [0, 0, 0]}}}
```
