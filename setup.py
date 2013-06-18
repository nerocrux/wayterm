#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='wayterm',
    version='0.1.0',
    description='Weibo client for terminal',
    author='peichao.yu',
    author_email='nerocrux@gmail.com',
    py_modules=['wayterm', ],
    package_data={'': ['LICENSE'], },
    url='http://wayterm.nerocrux.org/',
    license=open('LICENSE').read(),
    long_description=open('README.rdoc').read(),
    install_requires=[
        "weibo >= 0.2.0",
        "pyyaml",
    ],
)
