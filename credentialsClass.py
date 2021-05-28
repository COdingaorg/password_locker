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

  