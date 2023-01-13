# Subsonic Connector

## Status

This software is in its early development phase.

## Instructions

Create your own `.env` file. Use `.sample.env` as a reference for the format of the file.

### Initialization

From a terminal, type

```text
poetry shell
poetry install
```

### Test execution

Then you can run the simple test using the following command:

```text
python subsonic_connector/test-cn.py
```

Make sure to load the variables specified in the `.env` file.  
The test is currently just a `main`.
