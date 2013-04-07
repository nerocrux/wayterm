#!/usr/bin/env python
# -*- coding: utf-8 -*-

from weiterm_api import Weiterm_api
from weibo import Client
import sys
import json
import yaml

class Weiterm(object):
    def __init__(self):
        self.app_key = '1746312660'
        self.app_secret = 'a113b12f49266b12125f6df1f9808045'
        self.callback_url = 'http://weiterm.nerocrux.org/done'
        self.uid = '1792779680'
        self.color = Weiterm_color()

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
                #'uid':self.client.token_info['uid'], # FIXME this bugs, but should do this way
                'uid':self._get_uid(),
            }
            self._write_access_token(token)


    def _read_access_token(self):
        token = yaml.load(open('config.yaml').read())
        try:
            self.access_token = token['access_token']
            self.expire_at = token['expires_at']
            self.uid= token['uid']
        except (TypeError, NameError):
            return False
        return True


    def _write_access_token(self, token):
        stream = file('config.yaml', 'w')
        yaml.dump(token, stream)


    def _get_uid(self):
        response = self.client.get('account/get_uid')
        return response['uid']


    def _init_print(self):
        f = open('logo','r')
        for line in f:
            print line,


    def call(self, command):
        if command[0].lower() == 'exit':
            exit()
        if command[0].lower() == 'help':
            f = open('help','r')
            for line in f:
                print line,
            return
        api = Weiterm_api(self.client, self.uid)
        api.call(command)


if __name__ == "__main__":
    weiterm = Weiterm()
    weiterm._init_print()
    while True:
        try:
            command = raw_input('weiterm > ')
            if len(command) == 0:
                pass
            else:
                weiterm.call(command.split('/'))
        except:
            print 'exiting...'
            exit()
