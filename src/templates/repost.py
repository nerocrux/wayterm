#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from color import Color

class Repost(object):

    def __init__(self, response, method = 'post'):
        self.response = response
        self.method = method
        self.color = Color()

    def _connector(self):
        return self.color.LABEL + ' L '

    def _name(self, screen_name):
        return self.color.NAME + '[' + screen_name + '] '

    def _text(self, text):
        return self.color.VALUE + text

    def _source_text(self, text):
        return self.color.PLAIN + text

    def _reposted_label(self):
        return self.color.LABEL + '[REPOSTED]'

    def _created_at(self, created_at):
        return self.color.DARK + created_at

    def _eof(self):
        return self.color.PLAIN

    def post_text(self):
        return self._reposted_label() + \
               self._text(self.response['text']) + ' - ' + \
               self._created_at(self.response['created_at']) + '\n' + \
               self._connector() + \
               self._name(self.response['user']['screen_name']) + ' ' + \
               self._source_text(self.response['retweeted_status']['text']) + \
               self._eof()
