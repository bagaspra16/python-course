import random

opening = "WELCOME TO PYTHON'S HIDING GAME"
closing = "THANK YOU FOR PLAYING!"
python_position = random.randint(1,4)

print("|------------------------------------------------------------|")
print(f"|---------------{opening}--------------|")
print("|------------------------------------------------------------|")
print("\n")
username = input("Input Username : ")
print("\n")
print("|------------------------------------------------------------|")
print("\n")
print(f'''Hello {username}! Come looking at the cave!!!
              
_-1-_  _-2-_  _-3-_  _-4-_
      ''')
guess = int(input(f'''In which cave is the python hiding? '''))
print("\n")
confirm = input(f'''Are you sure the python's hiding in {python_position} cave [yes/no]? ''')
print("\n")
print("|------------------------------------------------------------|")
print("\n")
if confirm == "yes":
    if guess == python_position:
        print(f'''You're right {username}!, The python's position is in 
that number {python_position} cave and you choose that number {guess} cave.
             ''')
    else:
        print(f'''You're wrong {username}!, The python's position is in 
that number {python_position} cave and you choose that number {guess} cave.
             ''')
else:
        guess = int(input(f'''Okay {username}, In which cave is the python hiding? '''))
        print("\n")
        print("|------------------------------------------------------------|")
        print("\n")
        if guess == python_position:
            print(f'''You're right {username}!, The python's position is in 
that number {python_position} cave and you choose that number {guess} cave.
             ''')
        else:
            print(f'''You're wrong {username}!, The python's position is in 
that number {python_position} cave and you choose that number {guess} cave.
             ''')
print("|------------------------------------------------------------|")
print(f"|-------------------{closing}-------------------|")
print("|------------------------------------------------------------|")
