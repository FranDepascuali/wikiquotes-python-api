# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A Python API library for retrieving quotes from WikiQuotes. Supports both Python 2.x and 3.x, with multi-language support (currently English and Spanish).

## Common Commands

### Testing
```bash
# Run all tests using tox (tests both Python 2.7 and 3.6)
tox

# Run specific test file directly
python tests/test_suite/author_test.py
python tests/test_suite/encoding_test.py

# Run tests with pytest
pytest
```

### Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Install package in development mode
pip install -e .
```

## Architecture

### Core API Flow (wikiquotes_api.py)
All public API functions follow this pattern:
1. Accept `raw_language` string parameter (e.g., "english", "español")
2. Convert to language module via `language_manager.from_string()`
3. Make API request via `api_manager`
4. Parse HTML response via `HTMLManager`
5. Return unicode strings regardless of Python version

### Language System
Languages are implemented as modules (not classes) in `wikiquotes/languages/`:
- Each language module defines: `base_url`, `quote_of_the_day_url`, `quote_of_the_day_parser()`, `non_quote_sections`
- `non_quote_sections` are section titles to exclude when parsing (e.g., "about", "misattributed")
- Language detection in `language_manager.py` normalizes input (strips accents, lowercases)

### Managers (wikiquotes/managers/)
- `api_manager.py`: Makes requests to WikiQuotes API
- `html_manager.py`: Parses HTML using BeautifulSoup, extracts quotes from list structures
- `language_manager.py`: Converts language strings to language modules, handles unicode
- `python_version_manager.py`: Python 2/3 compatibility checks
- `custom_exceptions.py`: Custom exceptions (TitleNotFound, UnsupportedLanguageException)

### Quote Parsing Strategy
Quotes are extracted from HTML list structures:
```html
<ul>
  <li>Quote text</li>
  <ul><li>author or reference</li></ul>
</ul>
```
The parser removes nested `<ul>` sublists (which contain metadata) and extracts only top-level `<li>` elements.

### Search Flow
When fetching quotes, the API first searches for the author name to handle typos/variations:
1. User input → `api_manager.request_titles()` → suggestion list
2. Take first suggestion
3. Request quotes page for that author
4. Parse and return quotes

This means `get_quotes("shakspare", "english")` makes ~4 API calls total.

## Adding New Language Support

1. Create new language module in `wikiquotes/languages/<language>.py` with required fields
2. Add language detection logic to `language_manager.from_string()`
3. Update `supported_languages()` in `wikiquotes_api.py`

## Testing System

Tests use a unique parametrized approach:
- Each author has a `.txt` file in `tests/authors/`
- Format: Line 1 = author name/page suffix, Line 2 = language, Line 3 = empty, Lines 4+ = one quote per line
- `Author.py` reads all `.txt` files and creates Author objects
- `author_test.py` dynamically generates test cases for each author
- Tests verify: all quotes retrieved, no duplicates, random quote functionality

Note: Cannot run with pytest directly; use `python tests/test_suite/author_test.py`

## Python 2/3 Compatibility

- All output is unicode strings (use `language_manager.transform_to_unicode()`)
- Python 2 encoding setup happens in `wikiquotes/__init__.py`
- Use `python_version_manager.is_python_2()` / `is_python_3()` for version checks
