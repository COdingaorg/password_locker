from random import randint
import random
lettersList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
'''
converting lettersList strings to uppercase
'''
lettersListUpper = []
for item in lettersList:
  letter = item.upper()
  lettersListUpper.append(letter)

password_generated = []

def password_generator():
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
  
    
  print(f'your password is: {random_password}')

  return random_password
  
password_generator()


