# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name = 'wikiquotes',
    version = '0.1.0',
    description = 'Wikiquotes python API',
    long_description = readme,
    author = 'Francisco Depascuali',
    author_email = 'francisco.depascuali@gmail.com',
    url = 'https://github.com/FranDepascuali/wikiquotes-python-api',
    license = license,
    test_suite="tests"
    # packages = find_packages(exclude=('tests'))
)
