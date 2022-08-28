

#import argv - a list in Python that contains all the command-line arguments passed to the script
from sys import argv
#these are 2 arguments
script, filename = argv

#print statement to let you know that we are going to erase the file
print(f"We're going to erase {filename}.")
#confirmation ?
print("If you don't want that, hit CTRL-C (^C).")
#are you pretty sure?
print("If you do want that, hit RETURN.")

input("?")

#open the file in write mode
print("Opening the file...")
target = open(filename, 'w')

#clears the contents in the file
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

#There’s too much repetition in this file. Use strings, formats, and escapes to print out line1,
#line2, and line3 with just one target.write() command instead of six

target.write(f'{line1} \n {line2}\n {line3}\n')
"""
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
"""
print("And finally, we close it.")

#close file object
target.close()

#2. Write a script similar to the last exercise(ex15.py) that uses read and argv to read the file you just created.

txt = open(filename)

print(txt.read())

txt.close()