from flask import Blueprint, render_template, redirect, url_for
from .env import twi_api_key, twi_api_secret, twi_access_token, twi_access_secret, ig_client_id, ig_client_secret, ig_access_token
import tweepy
import requests
import json

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
    #Get Twitter post
    tweets = twi_api.user_timeline(count=3)
    #Get Instagram Posts
    url_ig = f"https://graph.instagram.com/me/media?fields=id,media_type,media_url,username,timestamp,permalink&access_token={ig_access_token}"
    response_ig = requests.get(url_ig)
    data_ig = response_ig.json()
    posts_ig = data_ig['data'][0:3]
    return render_template('home.html', tweets=tweets, posts_ig=posts_ig)

@views.route('/about-me')
def about_me():
    return render_template('about-me.html')

