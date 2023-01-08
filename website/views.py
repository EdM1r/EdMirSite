from flask import Blueprint, render_template, redirect, url_for

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home')
def home():
    return render_template('home.html')

@views.route('/about-me')
def about_me():
    return render_template('about-me.html')

