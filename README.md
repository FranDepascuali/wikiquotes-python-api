[![GitHub release](https://img.shields.io/github/release/FranDepascuali/wikiquotes-python-api.svg)](https://github.com/FranDepascuali/wikiquotes-python-api/releases)
![Python](https://img.shields.io/badge/python-2.x%2F3.x-blue.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)


# wikiquote-python-api

This library is intended to be a python API for wikiquotes (inspired by [python-wikiquotes](https://github.com/federicotdn/python-wikiquotes/)).

## Table of Contents
  * [Usage](#usage)
  * [Motivation](#motivation)
  * [Languages](#languages)
  * [Credits](#credits)

## Usage
```python
TODO
```

## Motivation
There seems to be two options for retrieving quotes from WikiQuotes using python: To implement it yourself or to use this other project [python-wikiquotes](https://github.com/federicotdn/python-wikiquotes/).
While the first approach wasn't to reinvent the wheel, usage and code inspection over [python-wikiquotes](https://github.com/federicotdn/python-wikiquotes/) lead me to develop a new library.

The main reasons for developing a new library were:
1. Quotes retrieved weren't all the quotes in wikiquotes API.
2. It doesn't work for python 2.x 
2. The code was too complex for what it was achieving. The choice in that project was to use urllib to retrieve the quotes, and lxml to parse the html.

This project:
1. Adds tests for retrieving all the quotes from every author (Though this point is difficult to satisfy, because quotes don't respect a format for all authors). 
2. Works for python 2.x and 3.x
3. Uses requests and BeautifulSoup, which abstract a lot of complexity which is present in [python-wikiquotes](https://github.com/federicotdn/python-wikiquotes/).

Anyway, the correct approach would be to try both and stick with the one that gives you the best results!

## Languages
Wikiquotes currently support English and Spanish.

## Credits
This project uses code from several open source packages:
<TODO>: LIST

## TODO

(Need to be open source, still missing features for going open source though) 
add code coverage (https://codecov.io/)
add travis(https://travis-ci.org/)
make it available via pip (https://marthall.github.io/blog/how-to-package-a-python-app/)
