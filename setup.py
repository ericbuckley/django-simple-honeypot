#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='django-simple-honeypot',
      version='1.0',
      description='Django honeypot field that you can add to your forms to reduce the chance of bot spam',
      author='Eric Buckley',
      author_email='eric.buckley@gmail.com',
      url='http://github.com/ericbuckley/django-simple-honeypot',
      packages = find_packages(exclude=['tests']),
     )