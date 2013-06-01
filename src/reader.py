#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

class Reader(object):
    def __init__(self):
        pass

    def _get_file(self, filename):
        __dir__ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(__dir__, filename)

    def printfile(self, filename):
        f = open(self._get_file(filename),'r')
        for line in f:
            print line,

