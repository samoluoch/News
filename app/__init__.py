from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap




'''
Initializing applicarion
'''
app = Flask(__name__,instance_relative_config= True)


'''
Setting up configuration
'''
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


'''
Initializing flask extensions by passing in the app instance
'''
Bootstrap = Bootstrap(app)


from app import views
