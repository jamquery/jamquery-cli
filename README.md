# Jamquery CLI

Command line interface for Jamquery.
Pretty unstable for now.

The program is fully written in Python.

## Installation

Install from the releases.

```
$ curl -sSLO https://github.com/jamquery/jamquery-cli/releases/download/0.1.0/jamquery && chmod a+x jamquery
```

You can also download it from https://github.com/jamquery/jamquery-cli/releases


## Build

Install [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/) in your computer and type in your terminal:

```
pyinstaller -F jamquery.py
```

This will create executable `dist/jamquery` file in the project root.


## Use

Copy the `jamquery` executable to your path that you like. (e.g. /Users/your-name/bin)

Make sure that those directories are properly listed in $PATH variable.

```
jamquery --help       # See help
jamquery -t android   # Search links that have 'android' tag
jamquery -d 2019      # Search links created in 2019
```
