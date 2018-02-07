#!/usr/bin/env python
# -*- coding: utf-8 -*

from __future__ import absolute_import

import os

from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(name='IMDBAPI',
      version='0.1 beta',
      description='API for IMDB',
	  packages=find_packages('IMDBAPI', exclude=('tests',)),
	  package_dir={'': 'IMDBAPI'},
      url='https://github.com/devilking15292/IMDB_Api_python.git',
      author='devilking15292',
      author_email='p.hari15292@gmail.com',
      license='MIT',
	  install_requires=install_requires,
      zip_safe=False,
	   classifiers=[
		'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
		]
	)