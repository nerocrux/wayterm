#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from color import Color

class Profile(object):

    def __init__(self, response, shortener, method = 'get'):
        self.response = response
        self.method = method
        self.shortener = shortener
        self.color = Color()

    def _name(self, screen_name, name):
        return self.color.NAME + screen_name + ' (' + name + ')'

    def _follower(self, followers_count):
        return self.color.LABEL + ' [follower] ' + self.color.VALUE + str(followers_count)

    def _following(self, friends_count):
        return self.color.LABEL + ' [following] ' + self.color.VALUE + str(friends_count)

    def _posts(self, statuses_count):
        return self.color.LABEL + ' [posts] ' + self.color.VALUE + str(statuses_count)

    def _location(self, location):
        return self.color.LABEL + ' [location] ' + self.color.VALUE + location

    def _url(self, url):
        return self.color.LABEL + ' [url] ' + self.color.VALUE + url

    def _description(self, description):
        return self.color.VALUE + description

    def _created_at(self, created_at):
        return self.color.LABEL + created_at

    def _text(self, text):
        return self.color.PLAIN + text

    def _eof(self):
        return self.color.PLAIN

    def get_text(self):
        return self._name(self.response['screen_name'], self.response['name']) + \
               self._follower(self.response['followers_count']) + \
               self._following(self.response['friends_count']) + \
               self._posts(self.response['statuses_count']) + \
               self._location(self.response['location']) + \
               self._url(self.response['url']) + '\n' + \
               self._description(self.response['description']) + '\n' + \
               self._created_at(self.response['status']['created_at']) + ' - ' + \
               self._text(self.response['status']['text']) + \
               self._eof()

