import unittest
from app.models import newss
Newss = newss.Newss

class NewssTest(unittest.TestCase):

    def setUp(self):
        self.new_Newss = Newss('https://s.yimg.com/os/creatr-uploaded-images/2022-01/11d8ecc0-8054-11ec-b7fb-dadff007f52b','We got our first good look at the EV6 last March and, nearly a year later, finally got to sit in it, drive it, and push every button in the cabin last week during a day-long press event in Northern California. It’s the first Kia vehicle to be produced under t…','2022-01-31T05:01:18Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_newss,Newss))

if __name__ == '__main__':
    unittest.main()        

         