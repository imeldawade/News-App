# from distutils.debug import DEBUG
from os import environ

# from instance.config import NEWS_API_KEY
NEWS_API_KEY = environ.get('NEWS_API_KEY')


class Config:

    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines/sources?apiKey=1779feda50ed4fc09523cd8838d8dc3f'

class ProdConfig(Config): 
    pass 

class DevConfig(Config):

    DEBUG= True    