from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    A function for the root page that will return the index page and its data
    '''

    title = 'Home- Welcome to News Highlights'
    return render_template('index.html', title=title)

@app.route('/news/<news_id>')
def news(news_id):
    '''
    A function that returns the news details page and more information
    '''
    return render_template('news.html', id=news_id)