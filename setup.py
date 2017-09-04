# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name = 'wikiquote',
    version = '0.1.0',
    description = 'Wikiquote python API',
    long_description = readme,
    author = 'Francisco Depascuali',
    author_email = 'francisco.depascuali@gmail.com',
    url = 'https://github.com/kennethreitz/samplemod',
    license = license,
    packages = find_packages(exclude=('tests'))
)
