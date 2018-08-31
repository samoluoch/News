class News:
    '''
    News class to define News Objects
    '''
    def __init__(self, name, source, author, title, description,url):
        self.name = name
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url