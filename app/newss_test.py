import unittest
from app.models import newss
News = newss.News

class NewsTest(unittest.TestCase)

    def setUp(self):
        self.new_News = News()