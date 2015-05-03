#!/usr/bin/env python
# -*- coding: utf8 -*-fr
"""
setup script to install python-itop-api
"""
from distutils.core import setup
from setuptools import find_packages

setup(name='python-itop-api',
      version='1.0',
      description='Set of python script to interact with iTop',
      author='Guillaume Philippon',
      author_email='guillaume.philippon@lal.in2p3.fr',
      url='https://github.com/guillaume-philippon/python-itop-api',
      license='FreeBSD License',
      data_files=[('/usr/share/itop-cli', ['itop-cli.cfg.example'])],
      scripts=["itop-cli"],
      packages=find_packages())
