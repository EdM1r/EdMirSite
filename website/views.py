from flask import Blueprint, render_template, url_for

#Set Views and vars
views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home')
def home():
    return render_template('home.html')

@views.route('/about-me')
def about_me():
    file_name = url_for('static', filename='img/me.jpeg')
    return render_template('about-me.html', my_photo=file_name)

