import unittest
from app import app
class FlaskAppTests(unittest.TestCase):
  def setUp(self):
   self.client = app.test_client()
 
if __name__ == '__main__':
 unittest.main()
