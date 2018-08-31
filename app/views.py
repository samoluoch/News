from flask import render_template
from app import app
from .request import get_news

@app.route('/')
def index():
    '''
    A function for the root page that will return the index page and its data
    '''
    top_headlines = get_news('sports')
    technology = get_news('technology')

    print(top_headlines)
    print(technology)
     
    
    title = 'Home- Welcome to News Highlights'
    return render_template('index.html', title=title, top_headlines=top_headlines, technology=technology)

@app.route('/news/<news_id>')
def news(news_id):
    '''
    A function that returns the news details page and more information
    '''
    return render_template('news.html', id=news_id)







