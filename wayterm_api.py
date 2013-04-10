import sys
from wayterm_color import Wayterm_color

class Wayterm_api(object):
    def __init__(self, client, uid):
        self.client = client
        self.uid = uid
        self.color =  Wayterm_color()

    def get_profile(self, params):
        """
        wayterm > profile/[screen_name]
        wayterm > p/[screen_name]
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
        print self.color.NAME + response['screen_name'] + ' (' + response['name'] + ')' + \
              self.color.LABEL + ' [follower] '    + self.color.VALUE + str(response['followers_count']) + \
              self.color.LABEL + ' [following] '   + self.color.VALUE + str(response['friends_count']) + \
              self.color.LABEL + ' [posts] '       + self.color.VALUE + str(response['statuses_count']) + \
              self.color.LABEL + ' [location] '    + self.color.VALUE + response['location'] + \
              self.color.LABEL + ' [url] '         + self.color.VALUE + response['url']
        print self.color.LABEL + ' [description] ' + self.color.VALUE + response['description']
        print self.color.LABEL + response['status']['created_at'] + ' - ' + \
              self.color.PLAIN + response['status']['text']


    def get_updates(self, params):
        """
        wayterm > list/[limit]
        wayterm > l/[limit]
            - get user's newest updates
            - default limit = 20
        """
        try:
            limit = params[0]
        except IndexError:
            limit = 20
        try:
            response = self.client.get('statuses/home_timeline', uid=self.uid, count=limit)
        except RuntimeError:
            print 'Error.'
            return
        for status in response['statuses']:
            print self.color.NAME + '[' + status['user']['screen_name'] + '] ' + \
                  self.color.PLAIN + status['text'] + ' ' + \
                  self.color.DARK + status['created_at'] + ' [id] ' + str(status['id']) + self.color.PLAIN


    def post_tweet(self, params):
        """
        wayterm > tweet/[message]
        wayterm > t/[message]
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
            weibo_url = 'http://www.weibo.com/' + str(response['user']['id']) + '/' + mid["mid"]
            print self.color.LABEL + '[POSTED] ' + \
                  self.color.VALUE + response['created_at'] + ' - ' + \
                  self.color.PLAIN + weibo_url
        except RuntimeError:
            print 'Error.'


    def get_comments(self, params):
        """
        wayterm > rcomment/[tweet_id]
        wayterm > rc/[message]
            - read comments of a certain tweet
        """
        tweet_id = params[0]
        if tweet_id == None:
            print 'Tweet Id can not be empty!'
            return
        if not isinstance(tweet_id, (int,long)):
            print 'Tweet Id is invalid!'
            return
        try:
            response = self.client.get('comments/show', id=tweet_id)
            print self.color.LABEL + '[POSTED] ' + \
                  self.color.VALUE + response['created_at'] + ' - ' + \
                  self.color.PLAIN + weibo_url
        except RuntimeError:
            print 'Error.'


    def call(self, command):
        cmd = command[0].lower()
        options = {
            'list'   : self.get_updates,
            'l'      : self.get_updates,
            'profile': self.get_profile,
            'p'      : self.get_profile,
            'tweet'  : self.post_tweet,
            't'      : self.post_tweet,
        }
        try:
            params = []
            for item in command[1:]:
                params.append(item)
            options[cmd](params)
        except KeyError:
            print 'Command error. Get command list by type help.'


