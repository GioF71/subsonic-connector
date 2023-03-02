# Subsonic Connector

## Reference

This library relies on the [py-sonic](https://github.com/crustymonkey/py-sonic) project.  
The current version I use in this project is [`1.0.0`](https://github.com/crustymonkey/py-sonic/releases/tag/0.8.0).

## Status

This software is in its early development phase.

## Links

Type|Link
:---|:---
Source Code|[GitHub](https://github.com/GioF71/subsonic-connector)
Python Library|[PiPy](https://pypi.org/project/subsonic-connector/)

## Instructions

Create your own `.env` file. Use `.sample.env` as a reference for the format of the file.

### Initialization

From a terminal, type

```text
poetry shell
poetry install
```

#### Test execution

Then you can run the simple test using the following command:

```text
python subsonic_connector/test-cn.py
```

Make sure to load the variables specified in the `.env` file.  
The test is currently just a `main` and it requires a running subsonic server. I am currently using [Navidrome](https://github.com/navidrome/navidrome).
