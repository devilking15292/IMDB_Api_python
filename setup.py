#!/usr/bin/env python
# -*- coding: utf-8 -*

from __future__ import absolute_import

import os

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(name='IMDBAPI',
    version='1.0.1.6',
    description='API for IMDB, to search for movie and get the details like rating, summary, director, cast etc',
	long_description=long_description,
    packages=['IMDBAPI'],
    url='https://github.com/devilking15292/IMDB_Api_python.git',
    author='devilking15292',
    author_email='p.hari15292@gmail.com',
    license='MIT',
    install_requires=install_requires,
	keywords='imdb, imdbapi, movie, movies',
    zip_safe=False,
    classifiers=[
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Internet :: WWW/HTTP',
    ]
    )