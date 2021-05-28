class UserClass:
  '''
  creates a class for generating new instance of a user
  '''
  userList = []
  def __init__(self,fname,lname, email_address, password):
      '''
      creates instance variables
      arguments:
              first_name : first name of the user
              last_name : last name of the user
              email : email of the user
              password : password of the user
      '''
      self.first_name = fname
      self.last_name = lname
      self.email = email_address
      self.password = password

  def save_user(self):
    '''
    saves a user instance created
    '''
    UserClass.userList.append(self)