

#importing arguments
from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
usr1 = input("What is your name ?: "  )

#C:\Users\congom\Desktop\lpthw>python ex13.py first second third
#The script is called: ex13.py
#Your first variable is: stuff
#Your second variable is: things
#Your third variable is: that

#this is my own thing
if __name__ == "__main__":
    print("This was executed directly")
else:
    print("This was imported as a module")