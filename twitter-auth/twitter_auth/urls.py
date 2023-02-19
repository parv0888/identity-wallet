from django.conf.urls import *
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'), 				#goto views.py -> main()
    url(r'^callback/$', views.callback, name='auth_return'), 		#after Oauth to Twitter it will redirect response to views.py -> callable()
    url(r'^logout/$', views.unauth, name='oauth_unauth'), 		#delete the session and logout views.py -> logout()
    url(r'^auth/$', views.auth, name='oauth_auth'), 			#Authenticate the user views.py -> auth()
    url(r'^info/$', views.info, name='info'), 				#show general info of user after Oauth.
    url(r'^home_timeline/$',views.home_timeline, name='home_timeline'), #show top recent 100 tweets
    url(r'^achievements_profile/$',views.achievements_profile, name='achievements_profile'), 		#profile which shared most domain
    url(r'^achievements_domain/$',views.achievements_domain, name='achievements_domain'), 		#most shared domain
    url(r'^view_tweets/$',views.view_tweets, name='view_tweets'), 		#view all tweets
]
