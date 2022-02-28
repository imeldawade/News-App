import unittest
from app.models import newss
News = newss.News

class NewsTest(unittest.TestCase):

    def setUp(self):
        self.new_News = News()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_newss,News))

if __name__ == '__main__':
    unittest.main()        

         