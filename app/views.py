from flask import render_template,request,redirect,url_for
from app import app
from .request import get_news,get_news_object,search_news

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

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search',category=search_news))
    else:

        return render_template('index.html', title=title, top_headlines=top_headlines, technology=technology)

@app.route('/news/<int:id>')
def news(news_id):
    '''
    A function that returns the news details page and more information
    '''
    news = get_news_object(id)
    name = f'{news.name}'
    description = f'{news.description}'
    return render_template('news.html', id=id, name=name, news=news, description=description)

@app.route('/search/<category>')
def search(category):
    '''
    Views function that displays the news search results
    '''
    category_name_list = category.name.split(" ")
    category_name_format = "+".join(category_name_list)
    searched_categories = search_news(category_name_format)

    title = f'search results for {category}'

    return render_template('search.html',category = searched_categories)
