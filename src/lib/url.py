#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json, sys, ast

class Url(object):
    def __init__(self):
        self.content_type = 'application/json'
        self.api_key      = 'AIzaSyDfqsLwLweHYvm1NApsJyFQKjTuTGCwW3A'
        self.endpoint     = 'https://www.googleapis.com/urlshortener/v1/url'

    def shorten(self, long_url):
        r = requests.post(
            self.endpoint,
            data=json.dumps({
                'longUrl': long_url,
                'key': self.api_key
            }),
            headers={
                'Content-type': 'application/json',
                'Accept': 'text/plain'
            }
        )
        response = ast.literal_eval(r.text.encode('ascii', 'ignore'))
        return response['id']
