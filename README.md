### Tests and linter status:
[![Actions Status](https://github.com/NNbaur/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/NNbaur/python-project-lvl2/actions) [![Actions Status](https://github.com/NNbaur/python-project-lvl2/actions/workflows/GithubActions1.yml/badge.svg)](https://github.com/NNbaur/python-project-lvl2/actions) <a href="https://codeclimate.com/github/NNbaur/python-project-lvl2/maintainability"><img src="https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability" /></a> <a href="https://codeclimate.com/github/NNbaur/python-project-lvl2/test_coverage"><img src="https://api.codeclimate.com/v1/badges/fd01772ef88bb39aa186/test_coverage" /></a>

### Description
______
A difference generator is a program that determines the difference between two data structures.

Utility features:
- Support for different input formats: yaml, json 
- Report generation in the form of plain text, stylish and json
### How to install
______
```
pip install git+https://github.com/NNbaur/python-project-lvl2.git
```

or

```
$ git clone https://github.com/NNbaur/python-project-lvl2 
$ cd ProjectDirectory
$ make install
$ make build
$ make package-install
```
### Usage
______

#### As external library
```
from gendiff.diff_builder.generate_diff import generate_diff

diff = generate_diff(filepath1, filepath2, style)

# style: stylish - default, plain, json
```
#### As CLI tool
```
gendiff -h
usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```

#### Formats
```
--format stylish - default
--format plain
--format json
```

### How to work gendiff function
__________

    Comparing of two json files:
[![asciicast](https://asciinema.org/a/488465.svg)](https://asciinema.org/a/488465)

    Comparing of two YAML files:
[![asciicast](https://asciinema.org/a/489649.svg)](https://asciinema.org/a/489649)

    Complicated tree structure(format - stylish):
[![asciicast](https://asciinema.org/a/502483.svg)](https://asciinema.org/a/502483)

    Complicated tree structure(format - plain):
[![asciicast](https://asciinema.org/a/502486.svg)](https://asciinema.org/a/502486)

    Complicated tree structure(format - json):
[![asciicast](https://asciinema.org/a/502494.svg)](https://asciinema.org/a/502494)


