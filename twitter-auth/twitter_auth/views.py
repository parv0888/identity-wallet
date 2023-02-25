from datetime import date, timedelta
import tweepy  # API for twitter
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import logout
from django.db.models import Count
from django.template import Context, Template
from twitter_auth.utils import CONSUMER_KEY, CONSUMER_SECRET, get_api
from . import models
from .home_timeline import home_timeline as home


def main(request):
    """
    main view of app, either login page or info page
    """
    # if we haven't authorised yet, direct to login page
    if check_key(request):
        return HttpResponseRedirect(reverse('info'))
    return render(request, 'twitter_auth/login.html')


def unauth(request):
    """
    logout and remove all session data
    """
    if check_key(request):
        request.session.clear()
        logout(request)
    return HttpResponseRedirect(reverse('main'))  # goto main()


def info(request):
    """
    display some user info to show we have authenticated successfully
    """
    if check_key(request):
        api = get_api(request)
        user = api.me()
        html = render(request, 'twitter_auth/attribute_form.html', {'user': user}).content
        html = str(html, 'UTF-8')  
        print(user)

        f = open("/html/attribute_form.html", "a")
        f.write(html)
        f.close()

        return render(request, 'twitter_auth/info.html', {'username': user.name})
    
    return HttpResponseRedirect(reverse('main'))


def auth(request):
    """
    twitter oauth
    """
    oauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth_url = oauth.get_authorization_url(True)
    response = HttpResponseRedirect(auth_url)
    request.session['request_token'] = oauth.request_token
    return response


def callback(request):
    verifier = request.GET.get('oauth_verifier')
    oauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    token = request.session.get('request_token')
    request.session.delete('request_token')
    oauth.request_token = token
    try:
        oauth.get_access_token(verifier)
    except tweepy.TweepError:
        print('Error, failed to get access token')

    request.session['access_key_tw'] = oauth.access_token
    request.session['access_secret_tw'] = oauth.access_token_secret
    response = HttpResponseRedirect(reverse('info'))
    return response


def check_key(request):
    """
    Check to see if we already have an access_key stored, if we do then we have already gone through
    OAuth. If not then we haven't and we probably need to.
    """
    try:
        access_key = request.session.get('access_key_tw', None)
        if not access_key:
            return False
    except KeyError:
        return False
    return True


def home_timeline(request):
    """
    This function fetches tweets from a user home time line and filter the tweets containing
    url.
    """
    if check_key(request):
        api = get_api(request)
        user = api.me()
        refined_tweets = []
        today = date.today()
        week_back = today - timedelta(days=7)

        for public_tweet in tweepy.Cursor(api.home_timeline, since_id=week_back).items(100):
            url = public_tweet.entities['urls']
            if len(url) != 0:
                if url[0]['display_url'][0:7] != 'twitter':
                    refined_tweets.append(public_tweet)
                    try:
                        home().insert_db(public_tweet, url)
                    except:
                        continue
        return render(request, 'twitter_auth/public_tweets.html',
                      {'public_tweets': refined_tweets, 'username': user.name})
    return render(request, 'twitter_auth/login.html')  # goto login


def achievements_profile(request):
    """
    This function finds the profile which have shared maximum number of tweets.
    """

    if check_key(request):
        query = models.Tweets.objects.values(
            'user').order_by().annotate(user_count=Count('user'))
        userid = max(query, key=lambda x: x['user_count'])
        api = get_api(request)
        user = api.me()
        profile_detail = api.get_user(userid['user'])
        return render(request, 'twitter_auth/achievements.html',
                      {'user': profile_detail, 'username': user.name})
    return render(request, 'twitter_auth/login.html')  # goto login


def achievements_domain(request):
    """
    This function returns the top 3 domains which have been shared stored in database.
    """
    if check_key(request):
        query = models.Tweets.objects.values(
            'domain').order_by().annotate(domain_count=Count('domain'))
        query = sorted(query, key=lambda x: x['domain_count'], reverse=True)
        api = get_api(request)
        user = api.me()
        filter_domain = []
        count = []
        for i in range(0, 3):
            filter_domain.append(query[i]['domain'])
            count.append(query[i]['domain_count'])
        return render(request, 'twitter_auth/achievements_domain.html',
                      {'query': filter_domain, 'count': count, 'username': user.name})
    return render(request, 'twitter_auth/login.html')  # goto login


def view_tweets(request):
    """
    This function returns all the the tweets stored in the database.
    """
    if check_key(request):
        api = get_api(request)
        user = api.me()
        query = models.Tweets.objects.all()
        return render(request, 'twitter_auth/view_tweets.html',
                      {'public_tweets': query, 'username': user.name})
    return render(request, 'twitter_auth/login.html')  # goto login
