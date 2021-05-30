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
  print('To be able to work with the application, Please create your account')
  
  shortCodes = input(f'Type ca to create your account and login: ')
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

    print(f'Hello {new_user.first_name}.Your Password Locker account was created successfully: \n')

     #save user account
    save_created_user(new_user)
    
    print('Login your account to proceed')
    logUser = input('Enter email: ')
    logpassword = input('Enter password: ')
    #Logging in using created program
    while logUser !=new_user.email or logpassword != new_user.password:
      print('Your username or password is wrong. please enter correct details')
      logUser = input('Enter email: ')
      logpassword = input('Enter password: ')

    else:
      print(f'Login successfull! Hello {new_user.first_name}')
      print('Let\'s Begin. Create or Store already existing account credentials')
      def create_credential_repeat():
        
        #Creating credentials

        accountInput = input('Enter Account name whose credentials you want to save: ')
        usernameInput = input(f"what is the username of your {accountInput} account?:  ")
        print('Do you want to Generate a password? Y/N')
        selectInput = input()
        if selectInput == 'y' or selectInput == 'Y':
          passWInput = generates_password()
        else:
          passWInput = input(f'Enter your the password of your {accountInput} account: ')
        #creating a credential
        print(f'===================================\n')
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
          def view_credentials():
            print(f'To view you credentials type: view \nTo find a credential type: find')
            conti = input()
            if conti == 'view' or conti == 'VIEW' or conti == 'View':
              print('Here are your saved credentials')
              credential = display_credentals_created()
              for items in credential:
                print(f"{items.account}\n{items.username}\n{items.password}")
                print(f'====================\n')
              view_credentials()
            
            elif conti == 'find' or conti == 'FIND' or conti == 'Find':
              print('Enter account Name you are searching...')
              accountName = input('Account Name: ')
              found = find_credential_by_account(accountName)
              print(f"Account Credential Found: \n{found.account}\n{found.username}\n{found.password}\n==============")
              option=input('Do you want to delete this item? Y/N')
              if option == 'Y' or option == 'y':
                credential_delete(found)
                print("item deleted successfully")
                view_credentials()
              else:
                view_credentials()
            else:
              print(f'sorry we did not catch that, kindly check your spelling\n')  
              view_credentials()
          view_credentials()
    create_credential_repeat()
        
if __name__=='__main__':
  main()