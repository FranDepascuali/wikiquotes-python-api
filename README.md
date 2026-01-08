![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://opensource.org/licenses/MIT)

# wikiquotes-python-api

This library is intended to be a python API for wikiquotes (inspired by [python-wikiquotes](https://github.com/federicotdn/python-wikiquotes/)).

## Support This Project

<a href="https://github.com/sponsors/FranDepascuali">
  <img align="right" width="150" alt="This library helped you? Consider sponsoring!" src=".github/funding-octocat.svg">
</a>

This module is provided **as is**, and developed in my free time.

**If this library helped you**, please consider [sponsoring this project](https://github.com/sponsors/FranDepascuali) 💰. Your support helps maintain and improve this library.

**For companies**: If you use this in production, sponsorship provides enterprise support, priority bug fixes, and feature requests. [Contact me](https://github.com/sponsors/FranDepascuali) for details.

## Table of Contents
- [wikiquotes-python-api](#wikiquotes-python-api)
  - [Support This Project](#support-this-project)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
  - [Installation](#installation)
  - [Features](#features)
  - [Development](#development)
    - [Testing](#testing)
    - [Releasing New Versions](#releasing-new-versions)
  - [How It Works](#how-it-works)
    - [Search](#search)
    - [Output](#output)
  - [Motivation](#motivation)
  - [Contributing](#contributing)
  - [License](#license)

## Usage
```python
>>> import wikiquotes

>>> wikiquotes.search("gandi", "english")
['Mahatma Gandhi', 'Indira Gandhi', 'Rahul Gandhi', 'Rajiv Gandhi', 'Arun Manilal Gandhi', 'Gandhi (film)', 'Anand Gandhi', 'Virchand Gandhi', 'Maneka Gandhi', 'Blindness']

>>> wikiquotes.get_quotes('Hau Pei-tsun', "english")
# ["The slogans of 'countering back the mainland' created by Chiang Kai-shek and 'liberating Taiwan' by Mao Zedong several decades ago should be forgotten because none of them could be put into practice.",
#  'When people on both sides of the Strait reach a consensus on their political system, unification will come to fruition naturally.',
#  'Taiwanese independence is a dead end.']

>>> wikiquotes.quote_of_the_day("english")
# ('Even after killing ninety nine tigers the Maharaja should beware of the hundredth.', 'Kalki Krishnamurthy')

>>> wikiquotes.quote_of_the_day("spanish")
# ('Por San Fermín, el calor no tiene fin', 'Refrán español')

>>> wikiquotes.random_quote("Aristotle", "english")
# 'For the things we have to learn before we can do, we learn by doing.'

>>> wikiquotes.supported_languages()
# ['english', 'spanish']
```

## Installation
```sh
pip install wikiquotes
```

## Features

- 🌍 **Multi-language support**: Currently supports English and Spanish
- 🔍 **Smart search**: Handles typos and name variations (e.g., "shakspare" → "Shakespeare")
- 📚 **Multiple functions**:
  - `search()` - Find authors by name
  - `get_quotes()` - Get all quotes from an author
  - `random_quote()` - Get a random quote from an author
  - `quote_of_the_day()` - Get the quote of the day
  - `supported_languages()` - List available languages
- ✅ **Clean data**: Filters out quotes *about* the person (not *by* them)
- 🐍 **Modern Python**: Supports Python 3.10+
- ✨ **Type-friendly**: Clean API with predictable return types

## Development

To work on the project locally in development mode:

```bash
# Install package in editable/development mode (includes all dependencies)
pip install -e ".[dev]"
```

The `-e` flag installs the package in editable mode, which means any changes you make to the source code will immediately be available without needing to reinstall the package.

After installation, you can import and use it:

```python
import wikiquotes

# Test it out
quotes = wikiquotes.get_quotes("Albert Einstein", "english")
print(quotes[0])
```

### Testing

Run tests to verify everything works:

```bash
# Run all tests using tox (tests Python 3.10+)
tox

# Run tests with pytest
pytest

# Run specific test file directly
python3 tests/test_suite/author_test.py
```

The approach for testing uses parametrized tests. Each author has a `.txt` file in `tests/authors/` with their name, language, and expected quotes. This allows easy addition of new test cases. See [author_test.py](https://github.com/FranDepascuali/wikiquotes-python-api/blob/master/tests/test_suite/author_test.py) for details.

### Releasing New Versions

To release a new version:

1. **Update version number**:
   ```bash
   # Update version in pyproject.toml (line 7)
   ```

2. **Update CHANGELOG.md**:
   ```bash
   # Add new version section with changes
   # Follow Keep a Changelog format
   ```

3. **Run tests**:
   ```bash
   pytest  # Ensure all tests pass
   ```

4. **Build the package**:
   ```bash
   python -m build
   ```

5. **Create git tag**:
   ```bash
   git add .
   git commit -m "Release version X.Y.Z"
   git tag -a vX.Y.Z -m "Version X.Y.Z"
   git push origin master --tags
   ```

6. **Upload to PyPI**:
   ```bash
   python -m twine upload dist/*
   ```

7. **Create GitHub Release**:
   - Go to [Releases](https://github.com/FranDepascuali/wikiquotes-python-api/releases)
   - Click "Create a new release"
   - Select the tag you just created
   - Copy content from CHANGELOG.md
   - Publish release

## How It Works

### Search

Quotes are retrieved by searching first for the correct author. This provides robustness, allowing the library to return quotes even if the input isn't the exact author name. Note that this requires multiple API calls to WikiQuotes to fetch suggestions (see [api_manager.py](https://github.com/FranDepascuali/wikiquotes-python-api/blob/master/wikiquotes/managers/api_manager.py)).

**Example flow**:
```
"shakspare" → API search → "shakespeare" → suggestions:
['William Shakespeare', 'Last words in Shakespeare', 'Shakespeare in Love', ...]
→ get_quotes ≈ 4 API calls total
```

### Output

All string output is unicode (Python 3 strings natively support unicode). Non-ASCII characters are handled automatically:

```python
>>> wikiquotes.random_quote("borges", "español")
# '«Todos caminamos hacia el anonimato, solo que los mediocres llegan un poco antes».'
```

## Motivation
There seems to be two options for retrieving quotes from WikiQuotes using python: To implement it yourself or to use [python-wikiquotes](https://github.com/federicotdn/python-wikiquotes/).
At a first glance, I chose the second option and used that library. However, usage and code inspection over [python-wikiquotes](https://github.com/federicotdn/python-wikiquotes/) lead me to choose the first approach and develop a library.

The main reasons for this decision were that:
1. Quotes retrieved weren't all the quotes in wikiquotes API (tried with different authors).
2. The code was too complex for what it was achieving. The choice in that project was to use urllib to retrieve the quotes, and lxml to parse the html.

This project:
1. Adds tests for retrieving all the quotes from several authors (Though this point is difficult to satisfy, because quotes don't respect a format for all authors).
2. Uses requests and BeautifulSoup, which abstract great part of the complexity which is present in [python-wikiquotes](https://github.com/federicotdn/python-wikiquotes/).

Anyway, the correct approach would be to try both and stick with the one that gives you the best results.

This project also gets to avoid fetching quotes included in about section. For example, if using [python-wikiquotes](https://github.com/federicotdn/python-wikiquotes/) and not this project:
```python
import wikiquote
print(wikiquote.quotes('Ada Lovelace'))
```
will fetch *"A large, coarse-skinned young woman but with something of my friend's features, particularly the mouth."*
which wasn't said by Ada Lovelace (but said about her).

While if you use this library, that quote and quotes about someone will not appear.
```python
import wikiquotes
print(wikiquotes.get_quotes('Ada Lovelace', 'english'))
```
*"A large, coarse-skinned young woman but with something of my friend's features, particularly the mouth."* doesn't appear because it wasn't said by Ada Lovelace.

## Contributing

Contributions are welcome! Here are some ways you can contribute:

- 🌍 Add support for new languages
- 🧪 Add test cases for more authors
- 🐛 Report bugs or issues
- 💡 Suggest new features

To add a new author test:
1. Create a `.txt` file in `tests/authors/`
2. Format:
   - Line 1: Author's name (or WikiQuotes page suffix)
   - Line 2: Language
   - Line 3: Empty
   - Lines 4+: One quote per line

See [dijkstra.txt](https://github.com/FranDepascuali/wikiquotes-python-api/blob/master/tests/authors/dijkstra.txt) as an example.

## License

MIT License - see [LICENSE](LICENSE) file for details.
