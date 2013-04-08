#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='weiterm',
    version='0.0.1',
    description='Weibo client for terminal',
    author='peichao.yu',
    author_email='nerocrux@gmail.com',
    py_modules=['weiterm', ],
    package_data={'': ['LICENSE'], },
    url='http://weiterm.nerocrux.org/',
    license=open('LICENSE').read(),
    long_description=open('README.rdoc').read(),
    install_requires=[
        "weibo",
        "pyyaml",
    ],
)
