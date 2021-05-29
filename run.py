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

def find_credential_by_account(account):
  '''
  implementing finding credential using account argument
  '''
  return CredentialsClass.find_credential_by_account(account)

def display_credentals_created():
  '''
  implementing display_credentials 
  '''
  return CredentialsClass.displays_credentials()

def generates_password():
  '''
  implementing password generator function in the Credentials Class
  '''
  return CredentialsClass.password_generator()

#main function
def main():
  print(f'Welcome to PASSWORD lOCKER command Line application \n')
  print('To able to work with the application, Please create your account')
  
  shortCodes = input(f'Type ca to create your account: ')
  print(f'You have entered {shortCodes}')
  while shortCodes != 'ca':
    print('sorry, we did not catch that.Try using small leters')
    shortCodes=input(' Please enter ca to create your account :')

  else:  
    nameFirst = input("Enter your First name: ")
    nameLast = input('Enter your last Name: ')
    holderemail = input("enter your email: ")
    print('finally...')
    passW = input('Enter the password to set for you password locker account: ')

    new_user = create_user(nameFirst, nameLast, holderemail, passW)

    print(f'Hello {new_user.first_name}.Your Password Locker account was created succeffully: \n')

    #save user account
    save_created_user(new_user)
    

    def create_credential_repeat():
      print('Time to store your credentials. Create Credential to store')
      #Creating credentials

      accountInput = input('Enter Account name whose credentials you want to save: ')
      usernameInput = input(f"what is the username of your {accountInput} account?:  ")
      passWInput = input(f'Enter your the password of your {accountInput} account: ')
      #creating a credential
      print(f'\n')
      new_credential = credential_creator(accountInput, usernameInput, passWInput)
      #save the credential created
      credential_saver(new_credential)

      print(f'Your {new_credential.account} account credentials have been saved successfully ')
      print(f'Account Name : {new_credential.account} \n Username: {new_credential.username} \n password: {new_credential.password}')

      #save another credential
      print('Do you want to save another account credential')
      answer= input('Y/N : ')
      if answer == 'Y' or answer == 'y':
        create_credential_repeat()
      else:
        print('Thank you for using PASSWORD LOCKER')
        print(f'To view you credentials type: view \n to find a credential type: find')
        conti = input()
        while True:
          if conti == 'view' or conti == 'VIEW' or conti == 'View':
            display_credentals_created()
            break
          if conti == 'find' or conti == 'FIND' or conti == 'Find':
            print('Enter account Name you are serching...')
            accountName = input('Account Name: ')

            find_credential_by_account(accountName)
            break
        print('sorry we did not catch that, kindly check your spelling')


    create_credential_repeat()
    

if __name__=='__main__':
  main()