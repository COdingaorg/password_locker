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

def credential_creator(usernameInput, passwordInput):
  '''
  creates a credential  new class intatance
  '''
  


def main():
  print('Welcome to PASSWORD lOCKER command Line application')
  print('To able to work with he application, Please create your account')
  
  shortCodes = input('Type ca to create your account')
  while shortCodes == 'ca':
    nameFirst = input("Enter your First name: ")
    nameLast = input('Enter your last Name: ')
    holderemail = input("enter your email: ")
    print('finally...')
    passW = input('Enter the password to set for you password locker account')

    create_user(nameFirst, nameLast, holderemail, passW)

    print(f'Hello {nameFirst}.Your Password Locker account was created succeffully')

    
  else:
    print('sorry, we did not catch that.')
    shortCodeinput(' Please enter ca to create your account')

if __name__=='__main__':
  main()