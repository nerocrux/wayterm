#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Color:
    PLAIN   = '\033[0m'
    NAME    = '\033[94m'
    LABEL   = '\033[95m'
    VALUE   = '\033[96m'
    AT_NAME = '\033[92m'
    TIME    = '\033[93m'
    DARK    = '\033[90m'
    RETWEET = '\033[1;32m'

    def disable(self):
        self.PLAIN = ''
        self.NAME = ''
        self.LABEL = ''
        self.VALUE = ''
        self.AT_NAME = ''
        self.TIME = ''
        self.DARK = ''
        self.RETWEET = ''
