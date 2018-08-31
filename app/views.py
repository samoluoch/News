from flask import render_template
from app import app
from .request import get_news

@app.route('/')
def index():
    '''
    A function for the root page that will return the index page and its data
    '''
    top_headlines = get_news('sports')
    name = get_news('name')
    source = get_news('source')
    author = get_news('author')
    title = get_news('title')
    url = get_news('url')
    print(top_headlines)
    print(name)
    print(source)
    print(author)
    print(title)
    print(url)
    title = 'Home- Welcome to News Highlights'
    return render_template('index.html', name=name, title=title, author=author, source=source, top_headlines=top_headlines, url=url)

@app.route('/news/<news_id>')
def news(news_id):
    '''
    A function that returns the news details page and more information
    '''
    return render_template('news.html', id=news_id)







