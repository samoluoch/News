from app import app
import urllib.request,json
from .models import news

News = news.News

api_key = app.config['NEWS_API_KEY']
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(category):
        '''
        Function that gets json response to url request
        '''
        get_news_url = base_url.format(category, api_key)

        with urllib.request.urlopen(get_news_url) as url:
            get_news_data = url.read()
            get_news_response = json.loads(get_news_data)

            news_results = None

            if get_news_response['sources']:
                news_results_list = get_news_response['sources']
                news_results = process_news(news_results_list)

        return news_results 

def process_news(news_list):
    '''
    Function to process news result and transform to a list of Objects
    
    Args:
        news_list: List of dictionaries that contain news details
    Results:
        news_results: List of news Objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        category = news_item.get('category')
        description = news_item.get('description')
        url = news_item.get('url')

        if url:
            news_object = News(id, name, description, url, category)

            news_results.append(news_object)

    return news_results

def get_news_object(id):
    '''
    Function that gets news item by taking in the news id and returning the news object details
    '''
    get_news_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            name = news_details_response.get('name')
            category = news_details_response.get('category')
            description = news_details_response.get('description')
            url = news_details_response.get('url')

            news_object = News(id,name,category,description,url)

    return news_object

def search_news(category):
    '''
    Function that allows users to search for news
    '''
    search_news_category_url = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}.format(category,api_key)'
    with urllib.request.urlopen(search_news_category_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['results']:
            search_news_list = search_news_response['results']
            search_news_results = process_results(search_news_list)


    return search_news_results

    