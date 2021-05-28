import unittest
from credentialsClass import CredentialsClass
from userClass import UserClass
import run

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
  
  def test_save_user(self):
    '''
    checks if function saves user
    '''
    self.new_user.save_user()

    self.assertEqual(len(UserClass.userList),1)

  def test_create_credentials(self):
    '''
    checks if function creates credential
    '''
    self.new_credential = CredentialsClass('twitter','email@test.com','1234password')

    self.assertEqual(self.new_credential.account,'twitter')
    self.assertEqual(self.new_credential.username,'email@test.com')
    self.assertEqual(self.new_credential.password,'1234password')




if __name__=='__main__':
  unittest.main()