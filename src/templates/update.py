#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
from color import Color

class Update(object):

    def __init__(self, response, shortener, method = 'get'):
        self.response = response
        self.method = method
        self.shortener = shortener
        self.color = Color()

    def _name(self, screen_name):
        return self.color.NAME + '[' + screen_name + ']'

    def _text(self, text):
        return self.color.PLAIN + text

    def _id(self, id):
        return ' [id] ' + str(id)

    def _created_at(self, created_at):
        return self.color.DARK + created_at + ' - '

    def _comments(self, comments_count):
        return ' [comments] ' + str(comments_count)


    def _reposts(self, reposts_count):
        return ' [reposts] ' + str(reposts_count)

    def _posted_label(self):
        return self.color.LABEL + '[POSTED] '

    def _deleted_label(self):
        return self.color.LABEL + '[DELETED] '

    def _weibo_url(self, url):
        return self.color.PLAIN + url

    def _pic_urls(self, pic_urls):
        result = self.color.DARK
        for url in pic_urls:
            result += '  L[pic] ' + self.shortener.shorten(self._pic_extender(url['thumbnail_pic'])) + '\n'
        return result

    def _pic_extender(self, url):
        return re.sub('/thumbnail/', '/bmiddle/', url)

    def _eof(self):
        return self.color.PLAIN

    def get_text(self):
        return self._name(self.response['user']['screen_name']) + ' ' + \
               self._text(self.response['text']) + '\n' + \
               self._pic_urls(self.response['pic_urls']) + \
               self._created_at(self.response['created_at']) + ' ' + \
               self._id(self.response['id']) + ' ' + \
               self._comments(self.response['comments_count']) + ' ' + \
               self._reposts(self.response['reposts_count']) + \
               self._eof()

    def post_text(self):
        return self._posted_label() + ' ' + \
               self._created_at(self.response['created_at']) + ' ' + \
               self._weibo_url(self.response['weibo_url']) + \
               self._eof()

    def delete_text(self):
        return self._deleted_label() + ' ' + \
               self._text(self.response['text']) + ' - ' + \
               self._created_at(self.response['created_at']) + \
               self._eof()
