# wikiquote-python-api

This library is intended to be a python API for wikiquotes (inspired by [python-wikiquotes](https://github.com/federicotdn/python-wikiquotes/)).

## Table of Contents

  * [Motivation](#motivation)
  * [Usage](#usage)
  * [Languages](#bootstrap)
  * [About](#about)

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

## Usage
```python
TODO
```

## Languages
Wikiquotes currently support English and Spanish.
