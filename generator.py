import random 
import time

letters=['a','b','c','w','r','y','q','e','t','y','u','i','o','p','s','d','f','g','h','j','k','l', 'z', 'x', 'v', 'b', 'n', 'm']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','£','$','%','&','/','(']

print('Welcome to Password Generator')
time.sleep(1)
print('\n')
nr_letters=int(input('How many letter do you want to use?\n'))
time.sleep(1)
nr_numbers=int(input('How many numbers would you want to use?\n'))
time.sleep(1)
nr_symbols=int(input('How many symbols would you want to use?\n'))
time.sleep(1)
password=[]
for char in range(1,nr_letters+1):
  password.append(random.choice(letters))
  
for number in range(1,nr_numbers+1):
  password.append(random.choice(numbers))
  
for symbol in range(1,nr_symbols+1):
  password.append(random.choice(symbols))

random.shuffle(password)

print('wait for few seconds...')
time.sleep(1)
for i in range(10,0,-1):
  print(f"{i} seconds remaining.")
  time.sleep(1)
print("\n")
print(f"Your password is {''.join(password)}")
