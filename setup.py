# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages
import subprocess

# TODO: Automate README generation
# # Try to create an rst long_description from README.md
# try:
#     args = 'pandoc', '--to', 'rst', 'README.md'
#     long_description = subprocess.check_output(args)
#     long_description = long_description.decode()
# except Exception as error:
#     print('README.md conversion to reStructuredText failed. Error:')
#     print(error)
#     print('Setting long_description to None.')
#     long_description = None

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

version = '1.4'

setup(
    name = 'wikiquotes',
    packages= find_packages(),
    version = version,
    description = 'Wikiquotes python API',
    long_description = readme,
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'
    ],
    install_requires = ['bs4', 'requests', 'lxml', 'unidecode', 'slacker'],
    author = 'Francisco Depascuali',
    author_email = 'francisco.depascuali@gmail.com',
    url = 'https://github.com/FranDepascuali/wikiquotes-python-api',
    download_url = 'https://github.com/FranDepascuali/wikiquotes-python-api/archive/{}.tar.gz'.format(version),
    license = license,
    test_suite="tests"
)
