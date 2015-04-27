#!/usr/bin/env python
# -*- coding: utf8 -*-fr
"""
setup script to install python-itop-api
"""
from distutils.core import setup

setup(name='python-itop-api',
      version='1.0',
      description='Set of python script to interact with iTop',
      author='Guillaume Philippon',
      author_email='guillaume.philippon@lal.in2p3.fr',
      scripts=["itop-cli"],
      packages=['itopapi', 'itopcli'])
