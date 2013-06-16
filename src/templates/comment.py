#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from color import Color

class Comment(object):

    def __init__(self, response, shortener, method = 'get'):
        self.response = response
        self.method = method
        self.shortener = shortener
        self.color = Color()

    def _connector(self):
        return self.color.LABEL + ' L '

    def _name(self, screen_name):
        return self.color.NAME + '[' + screen_name + '] '

    def _text(self, text):
        return self.color.VALUE + text

    def _source_text(self, text):
        return self.color.PLAIN + text

    def _commented_label(self):
        return self.color.LABEL + '[COMMENTED]'

    def _created_at(self, created_at):
        return self.color.DARK + created_at

    def _comments(self, comments_count):
        return ' [comments] ' + str(comments_count)

    def _eof(self):
        return self.color.PLAIN

    def get_text(self):
        return self._connector() + \
               self._name(self.response['user']['screen_name']) + ' ' + \
               self._text(self.response['text']) + ' ' + \
               self._created_at(self.response['created_at']) + \
               self._eof()

    def post_text(self):
        return self._connector() + \
               self._commented_label() + ' ' + \
               self._name(self.response['user']['screen_name']) + ' ' + \
               self._text(self.response['text']) + ' ' + \
               self._source_text(self.response['status']['text']) + \
               self._eof()
