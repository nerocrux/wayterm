import sys
from wayterm_color import Wayterm_color

class Wayterm_api(object):
    def __init__(self, client, uid):
        self.client = client
        self.uid = uid
        self.color =  Wayterm_color()

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
        wayterm > list\[limit]
        wayterm > l\[limit]
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
                  self.color.PLAIN + status['text'] + ' '
            print self.color.DARK + status['created_at'] + \
                  ' [id] ' + str(status['id']) +\
                  ' [comments] ' + str(status['comments_count']) + \
                  ' [reposts] ' + str(status['reposts_count']) + self.color.PLAIN


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
            weibo_url = 'http://www.weibo.com/' + str(response['user']['id']) + '/' + mid["mid"]
            print self.color.LABEL + '[POSTED] ' + \
                  self.color.VALUE + response['created_at'] + ' - ' + \
                  self.color.PLAIN + weibo_url
        except RuntimeError:
            print 'Error.'


    def get_comments(self, params):
        """
        wayterm > comment\[tweet_id]
        wayterm > c\[tweet_id]
            - read comments of a certain tweet
            - list latest 20 comments to me if [tweet_id] is omitted
        """
        try:
            tweet_id = params[0]
        except IndexError:
            tweet_id = None
        try:
            if tweet_id == None:
                response = self.client.get('comments/to_me', count=20)
            else:
                response = self.client.get('comments/show', id=tweet_id)

            for comment in response['comments']:
                print self.color.NAME + '[' + comment['user']['screen_name'] + '] ' + \
                      self.color.VALUE + comment['text'] + ' - ' + \
                      self.color.DARK + comment['created_at']
                print self.color.LABEL + ' L ' + \
                      self.color.PLAIN + comment['status']['text'] + self.color.PLAIN
        except RuntimeError:
            print 'Error.'


    def post_comments(self, params):
        """
        wayterm > wcomment\[tweet_id]\foobar
        wayterm > wc\[tweet_id]\foobar
            - read comments of a certain tweet
            - list latest 20 comments to me if [tweet_id] is omitted
        """
        try:
            tweet_id = params[0]
            comment  = params[1]
        except IndexError:
            print 'Error. Tweet id or comment iss not correct'
            return
        try:
            response = self.client.post('comments/create', id=tweet_id, comment=comment)
            print self.color.LABEL + [COMMENTED] + \
                  self.color.NAME + '[' + response['user']['screen_name'] + '] ' + \
                  self.color.VALUE + response['text'] + ' - ' + \
                  self.color.DARK + response['created_at']
            print self.color.LABEL + ' L ' + \
                  self.color.PLAIN + response['status']['text'] + self.color.PLAIN

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
        }
        try:
            params = []
            for item in command[1:]:
                params.append(item)
            options[cmd](params)
        except KeyError:
            print 'Command error. Get command list by type help.'

