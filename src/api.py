#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from template import Template
from settings import Settings

class Api(object):
    def __init__(self, client, uid):
        self.client = client
        self.uid = uid
        self.template = Template()
        self.settings = Settings()

    def get_profile(self, params):
        """
        wayterm > profile\[screen_name]
        wayterm > p\[screen_name]
            - get user's profile
        """
        try:
            screen_name = params[0]
        except IndexError:
            screen_name = None
        try:
            if screen_name == None:
                response = self.client.get('users/show', uid = self.uid)
            else:
                response = self.client.get('users/show', screen_name = screen_name)
        except RuntimeError:
            print 'Error.'
            return
        print self.template.build('Profile', 'get', response)
        self.get_user_updates(screen_name, self.settings.PROFILE_STATUS_CNT)


    def get_user_updates(self, screen_name, count):
        """
        private
        """
        try:
            response = self.client.get('statuses/user_timeline', screen_name = screen_name, count = count)
        except RuntimeError:
            print 'Error.'
            return
        for status in response['statuses']:
            print self.template.build('Update', 'get', status)


    def get_updates(self, params):
        """
        wayterm > list\[limit]
        wayterm > l\[limit]
            - get user's newest updates
            - default limit = 10
        """
        try:
            limit = params[0]
        except IndexError:
            limit = self.settings.DEFAULT_LIST_STATUS_CNT
        try:
            response = self.client.get('statuses/home_timeline', uid=self.uid, count=limit)
        except RuntimeError:
            print 'Error.'
            return
        for status in response['statuses']:
            print self.template.build('Update', 'get', status)


    def post_tweet(self, params):
        """
        wayterm > tweet\[message]
        wayterm > t\[message]
            - post weibo
        """
        try:
            tweet = params[0]
        except IndexError:
            print 'Tweet can not be empty!'
            return
        if len(tweet) > 140:
            print 'Tweet is over max length! [Input Words] = ' + len(tweet)
            return
        try:
            response = self.client.post('statuses/update', status=tweet)
            mid = self.client.get('statuses/querymid', id=response['id'], type=1)
            weibo_url = self.settings.WEIBO_ROOT_URL + str(response['user']['id']) + '/' + mid["mid"]
            response.update({"weibo_url":weibo_url})
            print self.template.build('Update', 'post', response)
        except RuntimeError:
            print 'Error.'


    def get_comments(self, params):
        """
        wayterm > comment\[tweet_id]
        wayterm > c\[tweet_id]
            - read comments of a certain tweet
            - list latest 10 comments to me if [tweet_id] is omitted
        """
        try:
            tweet_id = params[0]
        except IndexError:
            tweet_id = None
        try:
            if tweet_id == None:
                response = self.client.get('comments/to_me', count=10)
            else:
                response = self.client.get('comments/show', id=tweet_id)

            for comment in response['comments']:
                print self.template.build('Comment', 'get', comment)
        except RuntimeError:
            print 'Error.'


    def post_comments(self, params):
        """
        wayterm > wcomment\[tweet_id]\foobar
        wayterm > wc\[tweet_id]\foobar
        """
        try:
            tweet_id = params[0]
            comment  = params[1]
        except IndexError:
            print 'Error. Tweet id or comment iss not correct'
            return
        try:
            response = self.client.post('comments/create', id=tweet_id, comment=comment)
            print self.template.build('Comment', 'post', response)

        except RuntimeError:
            print 'Error.'


    def repost(self, params):
        """
        wayterm > repost\[tweet_id]\[comment]
        wayterm > r\[tweet_id]\[comment]
            - repost weibo
        """
        try:
            tweet_id = params[0]
        except IndexError:
            print 'Error. Tweet id or comment is invalid'
            return
        try:
            comment = params[1]
        except IndexError:
            comment = 'Repost'
        try:
            response = self.client.post('statuses/repost', id=tweet_id, status=comment)
            print self.template.build('Repost', 'post', response)

        except RuntimeError:
            print 'Error.'


    def delete(self, params):
        """
        wayterm > delete\[tweet_id]\
        wayterm > d\[tweet_id]\
            - delete weibo
        """
        try:
            tweet_id = params[0]
        except IndexError:
            print 'Error. Tweet id is invalid'
            return
        try:
            response = self.client.post('statuses/destroy', id=tweet_id)
            print self.template.build('Update', 'delete', response)

        except RuntimeError:
            print 'Error.'


    def call(self, command):
        cmd = command[0].lower()
        options = {
            'list'     : self.get_updates,
            'l'        : self.get_updates,
            'profile'  : self.get_profile,
            'p'        : self.get_profile,
            'tweet'    : self.post_tweet,
            't'        : self.post_tweet,
            'comment'  : self.get_comments,
            'c'        : self.get_comments,
            'wcomment' : self.post_comments,
            'wc'       : self.post_comments,
            'repost'   : self.repost,
            'r'        : self.repost,
            'delete'   : self.delete,
            'd'        : self.delete,
        }
        try:
            params = []
            for item in command[1:]:
                params.append(item)
            options[cmd](params)
        except KeyError:
            print 'Command error. Get command list by type help.'

