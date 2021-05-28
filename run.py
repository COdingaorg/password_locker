from userClass import UserClass
from credentialsClass import CredentialsClass

def create_user(nameFirst, nameLast, holderemail, passW):
  '''
  creates a user class instance
  '''
  new_user = UserClass(nameFirst, nameLast, holderemail, passW)
  
  return new_user
