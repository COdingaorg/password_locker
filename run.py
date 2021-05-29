#!/usr/bin/env python3.8
from userClass import UserClass
from credentialsClass import CredentialsClass

def create_user(nameFirst, nameLast, holderemail, passW):
  '''
  creates a user class instance
  '''
  new_user = UserClass(nameFirst, nameLast, holderemail, passW)
  
  return new_user

def save_created_user(user):
  '''
  method that saves user created
  '''
  user.save_user()

def credential_creator(account, username, password):
  '''
  creates a credential  new class intatance
  '''
  new_credential = CredentialsClass(account, username, password)
  return new_credential

def credential_saver(new_credential):
  '''
  method that implements saving og the credential created
  '''
  new_credential.save_credential()

def credential_delete(new_credential):
  '''
  implementing the delete credential
  '''
  new_credential.delete_credential()

  
  


def main():
  print('Welcome to PASSWORD lOCKER command Line application')
  print('To able to work with he application, Please create your account')
  
  shortCodes = input('Type ca to create your account')
  while shortCodes != 'ca':
    print('sorry, we did not catch that.')
    shortCodes=input(' Please enter ca to create your account').lower

  else:  
    nameFirst = input("Enter your First name: ")
    nameLast = input('Enter your last Name: ')
    holderemail = input("enter your email: ")
    print('finally...')
    passW = input('Enter the password to set for you password locker account')

    create_user(nameFirst, nameLast, holderemail, passW)

    print(f'Hello {nameFirst}.Your Password Locker account was created succeffully')

    
if __name__=='__main__':
  main()