import random

opening = "WELCOME"
main = "MAIN CONTENT"
closing = "THANK YOU"
python_position = random.randint(1,4)

print("|-------------------------------------------------------|")
print(f"|------------------------{opening}------------------------|")
print("|-------------------------------------------------------|")
print("\n")
username = input("Input Username : ")
print("\n")
print("|-------------------------------------------------------|")
print("\n")
print(f'''
        Hello {username}! Come looking at the cave!!!
              
              _-1-_  _-2-_  _-3-_  _-4-_
      ''')
guess = int(input(f'''
         In which cave is the python hiding? '''))
print("\n")
print("|-------------------------------------------------------|")
print("\n")
if guess == python_position:
    print(f'''You're right {username}!, The python's position is in 
that number {python_position} cave and you choose that number {guess} cave
         ''')
else:
    print(f'''You're wrong {username}!, The python's position is in 
that number {python_position} cave and you choose that number {guess} cave
         ''')