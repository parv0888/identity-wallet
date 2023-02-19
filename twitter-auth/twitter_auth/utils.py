import tweepy
import environ
from djangotweepy.settings import CONSUMER_KEY, CONSUMER_SECRET

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)


#Application key

def get_api(request):
	# set up and return a twitter api object
	oauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	access_key = request.session['access_key_tw']
	access_secret = request.session['access_secret_tw']
	oauth.set_access_token(access_key, access_secret)
	api = tweepy.API(oauth, wait_on_rate_limit=True)
	return api
