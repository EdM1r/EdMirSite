from flask import Blueprint, render_template, redirect, url_for
from .env import twi_api_key, twi_api_secret, twi_access_token, twi_access_secret, ig_client_id, ig_client_secret, ig_access_token, medium_access_token, rapid_api_key
import tweepy
import requests
import json

#Set Views and vars
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


# Get instagram posts 
def get_instagram_posts(ig_access_token):
    url_ig = f"https://graph.instagram.com/me/media?fields=id,media_type,media_url,username,timestamp,permalink&access_token={ig_access_token}"
    response_ig = requests.get(url_ig)
    data_ig = response_ig.json()
    posts_ig = data_ig['data'][0:3]
    return posts_ig


#get medium posts
def get_medium_posts(rapid_api_key):
    username = 'edmir'
    # Make a request to the Medium API to get the user's ID
    url = f"https://medium2.p.rapidapi.com/user/id_for/{username}"
    headers = {
        "Content-Type": "application/json",
        "X-RapidAPI-Key": rapid_api_key
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    user_id = data['id']

    # Make a request to the Medium API to get the user's top posts
    url = f"https://medium2.p.rapidapi.com/user/{user_id}/top_articles"
    response = requests.get(url, headers=headers)
    data = response.json()

    top_3_posts = data['top_articles'][0:3]

    #fetching title and subtitle of each article 
    posts_list = []

    for post in top_3_posts:
        url = f'https://medium2.p.rapidapi.com/article/{post}'
        response = requests.get(url, headers=headers)
        data = response.json()
        posts_list.append(data)
    
    return posts_list

@views.route('/')
@views.route('/home')
def home():
    #Get Twitter post
    tweets = twi_api.user_timeline(count=3)

    #Get Instagram Posts
    posts_ig = get_instagram_posts(ig_access_token)

    #get medium posts
    medium_posts = get_medium_posts(rapid_api_key)

    return render_template('home.html', tweets=tweets, posts_ig=posts_ig, medium_posts=medium_posts)

@views.route('/about-me')
def about_me():
    return render_template('about-me.html')

