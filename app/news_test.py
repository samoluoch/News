import unittest
from app.models import news

class NewsTest(unittest.TestCase):
    '''
    Test Class that tests the behavior of the News class
    '''
    def setUp(self):
        '''
        setUp() method that runs before every test.
        '''
        self.new_news = News('cnn', 'CNN-News', 'Chinese President Arrives', 'The Chinese President came to the US today to strike a trade deal on exports', 'www.cnn.com')

