from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = '827213481048956928-OzDz1dtcqfCl2qGMgnmMSRNuwHU6Xn0'
access_token_secret = 'sV9XuE9tdfIb6idIVtDyjKB0x9LMWqVtioYyiC5V5rwEC'
consumer_key = 'ho2DsflKj8dp234df53Xy0t4Y'
consumer_secret = '9s1fWY9nlmBGeHcAZxUgkyAbcfhHU2zbpheMWuSwFLL2XGxSLA'

class YouthListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)

if __name__ == '__main__':
    l = YouthListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['Youthleadership','Youth'])
