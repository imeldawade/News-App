import unittest
from app.models import newss
Newss = newss.Newss

class NewssTest(unittest.TestCase):

    def setUp(self):
        self.new_Newss = Newss()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_newss,Newss))

if __name__ == '__main__':
    unittest.main()        

         