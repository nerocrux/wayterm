#!/usr/bin/env python
# -*- coding: utf-8 -*-

from color import Color

class Trend(object):

    def __init__(self, response, shortener, method = 'get'):
        self.response = response
        self.method = method
        self.color = Color()

    def _text(self, text):
        return self.color.PLAIN + text

    def _time(self, created_at):
        return self.color.DARK + created_at + ' - '

    def _eof(self):
        return self.color.PLAIN

    def get_text(self):
        return self.response['name'] + ' (' + self.response['amount'] + ')'
