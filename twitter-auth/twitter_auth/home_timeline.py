from . import models
import json

class home_timeline():
    def get_domain(self,str):
        for x in range(0, len(str)):
            if (str[x] == '/'):
                return str[0:x]

    def insert_db(self,public_tweet, url):
        tweet_model = models.Tweets()
        tweet_model.id = str(public_tweet.id) + str(public_tweet.user.id)
        tweet_model.tweet_id = public_tweet.id
        tweet_model.name = public_tweet.user.name
        tweet_model.text = public_tweet.text
        tweet_model.user = public_tweet.user.id
        tweet_model.domain = self.get_domain(url[0]['display_url'])
        tweet_model.profile_image = public_tweet.user.profile_image_url
        tweet_model.save()

    def pretty_print(self,public_tweet):
        json_str = json.dumps(public_tweet._json)
        parsed = json.loads(json_str)
        print(json.dumps(parsed, indent=4, sort_keys=True))
