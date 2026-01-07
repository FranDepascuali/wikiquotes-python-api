# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
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
    long_description_content_type = 'text/markdown',
    platforms='any',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ],
    install_requires = ['beautifulsoup4>=4.9.0', 'requests>=2.25.0', 'lxml>=4.6.0', 'unidecode>=1.2.0'],
    author = 'Francisco Depascuali',
    author_email = 'francisco.depascuali@gmail.com',
    url = 'https://github.com/FranDepascuali/wikiquotes-python-api',
    download_url = 'https://github.com/FranDepascuali/wikiquotes-python-api/archive/{}.tar.gz'.format(version),
    license = license,
    test_suite="tests"
)
