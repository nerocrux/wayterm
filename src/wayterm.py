#!/usr/bin/env python
# -*- coding: utf-8 -*-

from api import Api
from reader import Reader
from template import Template
from weibo import Client
from lib.url import Url
import sys
import os
import json
import yaml

class Wayterm(object):
    def __init__(self):
        self.app_key = '1746312660'
        self.app_secret = 'a113b12f49266b12125f6df1f9808045'
        self.callback_url = 'http://wayterm.nerocrux.org/done'
        self.template = Template()
        self.url = Url()
        self.reader = Reader()
        self.token = {}

        if self._read_access_token():
            self.client = Client(self.app_key, self.app_secret, self.callback_url, self.token)
        else:
            self.client = Client(self.app_key, self.app_secret, self.callback_url)
            self.auth_url = self.url.shorten(self.client.authorize_url)
            print '[1] Open this url in your browser: ' + self.auth_url
            self.auth_code = raw_input('[2] Enter authorization code: ')
            self.client.set_code(self.auth_code)
            token = {
                'access_token':self.client.token['access_token'],
                'expires_at':self.client.token['expires_at'],
                'uid':self.client.token['uid'],
            }
            self._write_access_token(token)
            print 'Authorization done. Enjoy!'


    def _read_access_token(self):
        try:
            self.token = yaml.load(open(os.path.join(os.getenv('HOME'), '.wayterm.yaml')).read())
        except:
            return False
        return True


    def _write_access_token(self, token):
        stream = file(os.path.join(os.getenv('HOME'), '.wayterm.yaml'), 'w')
        yaml.dump(token, stream)


    def _init_print(self):
        self.reader.printfile('logo')


    def call(self, command):
        if command[0].lower() == 'exit':
            exit()
        if command[0].lower() == 'help':
            self.reader.printfile('help')
            return
        api = Api(self.client)
        api.call(command)


