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

  @classmethod
  def find_credential_by_account(cls, account):
    '''
    a method that finds a credential instance by using a value for account argument
    '''
    for credentiaItem in cls.credentialsList:
      if credentiaItem.account == account:
        return credentiaItem


  