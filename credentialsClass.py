from random import randint
import random
class CredentialsClass:
  '''
  creates a credential class
  '''
  credentialsList = []
  def __init__(self,account, username, password):
    '''
    creates instance variables for creadential class instances
    '''
    self.account = account
    self.username = username
    self.password = password
  
  def save_credential(self):
    '''
    saves credentials instance inside credentials list
    '''
    CredentialsClass.credentialsList.append(self)

  def delete_credential(self):
    '''
    a method that deletes a credential instance
    '''
    CredentialsClass.credentialsList.remove(self)

  def find_credential_by_account(account):
    '''
    a method that finds a credential instance by using a value for account argument
    '''
    for credentiaItem in CredentialsClass.credentialsList:
      if credentiaItem.account == account:
        return credentiaItem

  def displays_credentials():
    '''
    a method that displays credentials list
    '''
    return CredentialsClass.credentialsList

#code lines that generates a password

  def password_generator():
    lettersList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    '''
    converting lettersList strings to uppercase
    '''
    lettersListUpper = []
    for item in lettersList:
      letter = item.upper()
      lettersListUpper.append(letter)

    password_generated = []
    password_generated_sliced = ''
    for range in lettersList:
      range = randint(0, 100)
      if range%2 == 0:
        password_generated.append(random.choice(lettersList))
      elif range%5==0 or range%3 == 0:
        password_generated.append(random.choice(lettersListUpper))
      else:
        password_generated.append(str(range))

    password_generated_sliced = password_generated[0:8:1]
    random_password=(''.join(password_generated_sliced))
    

    return random_password

  password = password_generator()  
  print(type(password))
  print(password+' this is it')