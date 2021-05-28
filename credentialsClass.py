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

  