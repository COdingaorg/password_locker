from userClass import UserClass
from credentialsClass import CredentialsClass

def create_user(nameFirst, nameLast, holderemail, passW):
  '''
  creates a user class instance
  '''
  new_user = UserClass(nameFirst, nameLast, holderemail, passW)
  
  return new_user

def credential_creator(usernameInput, passwordInput):
  '''
  creates a credential  new class intatance
  '''
  new_credential = CredentialsClass(usernameInput,passwordInput)
  return new_credential

