#!/usr/bin/env python
# -*- coding: utf-8 -*-

from api import Api
from reader import Reader
from template import Template
from weibo import Client
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
        self.reader = Reader()

        if self._read_access_token():
            self.client = Client(self.app_key, self.app_secret, self.callback_url, self.uid, self.access_token, self.expire_at)
        else:
            self.client = Client(self.app_key, self.app_secret, self.callback_url)
            self.auth_url = self.client.authorize_url
            print '[1] Open this url in your browser: ' + self.auth_url
            self.auth_code = raw_input('[2] Enter authorization code: ')
            self.client.set_code(self.auth_code)
            token = {
                'access_token':self.client.token_info['access_token'],
                'expires_at':self.client.token_info['expires_at'],
                'uid':self.client.token_info['uid'],
            }
            print self.client.token_info
            self._write_access_token(token)


    def _read_access_token(self):
        try:
            token = yaml.load(open(os.path.join(os.getenv('HOME'), '.wayterm.yaml')).read())
            self.access_token = token['access_token']
            self.expire_at = token['expires_at']
            self.uid= token['uid']
        except:
            return False
        return True


    def _write_access_token(self, token):
        stream = file(os.path.join(os.getenv('HOME'), '.wayterm.yaml'), 'w')
        yaml.dump(token, stream)


    def _get_uid(self):
        response = self.client.get('account/get_uid')
        return response['uid']


    def _init_print(self):
        self.reader.printfile('logo')


    def call(self, command):
        if command[0].lower() == 'exit':
            exit()
        if command[0].lower() == 'help':
            self.reader.printfile('help')
            return
        api = Api(self.client, self.uid)
        api.call(command)


