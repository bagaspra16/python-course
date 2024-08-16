import random

opening = "WELCOME TO PYTHON'S HIDING GAME"
closing = "THANK YOU FOR PLAYING!"
python_position = random.randint(1,5)

print("|------------------------------------------------------------|")
print(f"|---------------{opening}--------------|")
print("|------------------------------------------------------------|")
print("\n")
username = input("Input Username : ")
print("\n")
print("|------------------------------------------------------------|")
print("\n")
cave_shape = "_---_"
empty_cave = [cave_shape] * 5

cave = empty_cave.copy()
cave[python_position - 1] = "_-|`-`|-_"

print(f'''Hello {username}! Come looking at the cave!!!
              
{empty_cave}
      ''')
guess = int(input(f'''In which cave is the python hiding(1/2/3/4/5)? '''))
print("\n")
confirm = input(f'''Are you sure the python's hiding in {guess} cave [yes/no]? ''')
print("\n")
print("|------------------------------------------------------------|")
print("\n")
if confirm == "yes":
    if guess == python_position:
        print(f'''{cave}

You're right {username}!, The python's position is in 
that number {python_position} cave and you choose that number {guess} cave.
             ''')
    else:
        print(f'''{cave}
              
You're wrong {username}!, The python's position is in 
that number {python_position} cave and you choose that number {guess} cave.
             ''')
else:
        guess = int(input(f'''Okay {username}, In which cave is the python hiding? '''))
        print("\n")
        print("|------------------------------------------------------------|")
        print("\n")
        if guess == python_position:
            print(f'''{cave}
                  
You're right {username}!, The python's position is in 
that number {python_position} cave and you choose that number {guess} cave.
             ''')
        else:
            print(f'''{cave}
                  
You're wrong {username}!, The python's position is in 
that number {python_position} cave and you choose that number {guess} cave.
             ''')
print("|------------------------------------------------------------|")
print(f"|-------------------{closing}-------------------|")
print("|------------------------------------------------------------|")
