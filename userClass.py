class UserClass:
  '''
  creates a class for generating new instance of a user
  '''
  userList = []
  def __init__(self,fname,lname, email_address, password):
      '''
      creates instance variables
      '''
      self.first_name = fname
      self.last_name = lname
      self.email = email_address
      self.password = password