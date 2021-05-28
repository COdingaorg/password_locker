class CredentialsClass:
  '''
  creates a credential class
  '''
  credentialsList = []
  def __init__(self, username, password):
    '''
    creates instance variables for creadential class instances
    '''
    self.username = username
    self.password = password