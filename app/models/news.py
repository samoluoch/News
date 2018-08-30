class News:
    '''
    News class to define News Objects
    '''
    def __init__(self, source, author, title, description,url):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url