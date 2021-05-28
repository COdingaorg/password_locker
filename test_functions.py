import unittest
from credentialsClass import CredentialsClass
from userClass import UserClass

class TestClass(unittest.TestCase):
  '''
  creates a class for testing functions in the application
  '''
  def setUp(self):
    '''
    set up functions that runs after each test function
    '''
    self.new_user=UserClass('Benard','Kibet','benard.kibet@student.motingaschool.com','password')