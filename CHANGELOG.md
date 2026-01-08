# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.5] - 2026-01-07

### Added
- Modern `pyproject.toml` for PEP 517/518 compliant packaging
- GitHub Actions CI/CD workflow for automated testing across Python 3.10-3.13
- `__version__` attribute in `__init__.py` for programmatic version access
- `.pytest_cache/` to `.gitignore`

### Changed
- **BREAKING**: Minimum Python version increased from 3.6 to 3.10
- Modernized packaging: removed `setup.py` in favor of `pyproject.toml`
- Removed `requirements.txt` - all dependencies now in `pyproject.toml`
- Updated installation instructions to use `pip install -e ".[dev]"`
- Migrated from `%` string formatting to f-strings in `file_manager.py`
- Standardized code formatting in `setup.py` (before removal)
- Updated tox configuration to test Python 3.10-3.13

### Fixed
- **Critical**: Fixed logging configuration that prevented users from configuring their own logging
  - Library now uses `NullHandler()` following Python logging best practices
  - Users can now call `logging.basicConfig()` after importing wikiquotes
- Fixed bug in `html_manager.py` `is_title()` function that incorrectly compared Tag objects
- Fixed bug in `logging_manager.py` `log_method_call()` decorator that called the task function twice

### Removed
- Dropped support for end-of-life Python versions 3.6, 3.7, 3.8, and 3.9
- Removed `setup.py` (replaced by `pyproject.toml`)
- Removed `requirements.txt` (dependencies now in `pyproject.toml`)
- Removed unused `wikiquotes/directory.py` file (all code was commented out)

## [1.4] - Previous Release

Earlier changes not documented in this changelog.
