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
    self.new_credential = CredentialsClass('twitter','email@test.com','1234password')
  
  def tearDown(self):
    '''
    tearDown funtion that cleans up the credentials list after test setup is done
    '''
    CredentialsClass.credentialsList=[]
  
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

  def test_save_credentials(self):
    '''
    checks if save fuction saves the created credentials
    '''
    self.new_credential.save_credential()

    self.assertEqual(len(CredentialsClass.credentialsList),1)

  def test_save_multiple_credentials(self):
    '''
    test to check that save credential method saves multiple credentials
    '''
    self.new_credential.save_credential()
    second_credential= CredentialsClass('linkedIn', 'Adongo254', 'adongo2021')
    second_credential.save_credential()

    self.assertEqual(len(CredentialsClass.credentialsList),2)

  def test_delete_credential(self):
    '''
    test to check that delete credential method deletes a credential instance
    '''
    self.new_credential.save_credential()
    second_credential= CredentialsClass('linkedIn', 'Adongo254', 'adongo2021')
    second_credential.save_credential()

    second_credential.delete_credential()

    self.assertEqual(len(CredentialsClass.credentialsList),1)





       

if __name__=='__main__':
  unittest.main()