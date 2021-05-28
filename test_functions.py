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
    self.new_user = UserClass('Benard','Kibet','benard.kibet@student.motingaschool.com','password')
  
  def test_user_creation(self):
    '''
    checks if a function creates a user
    '''
    self.assertEqual(self.new_user.first_name,'Benard')
    self.assertEqual(self.new_user.last_name,'Kibet')
    self.assertEqual(self.new_user.email,'benard.kibet@student.motingaschool.com')
    self.assertEqual(self.new_user.password,'password')

if __name__=='__main__':
  unittest.main()