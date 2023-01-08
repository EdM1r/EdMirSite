from flask import Blueprint, render_template, redirect, url_for
from .env import twi_api_key, twi_api_secret, twi_access_token, twi_access_secret
import tweepy


views = Blueprint('views', __name__)

# Authenticate with Twitter
auth_twi = tweepy.OAuthHandler(twi_api_key, twi_api_secret)
auth_twi.set_access_token(twi_access_token, twi_access_secret)
twi_api = tweepy.API(auth_twi)

#test connection to twitter API 
try:
    twi_api.verify_credentials()
    print('Successful Authentication Twitter')
except:
    print('Failed Twitter authentication')



@views.route('/')
@views.route('/home')
def home():
    tweets = twi_api.user_timeline(count=3)
    return render_template('home.html', tweets=tweets)

@views.route('/about-me')
def about_me():
    return render_template('about-me.html')

