
#this is my own thing
if __name__ == "__main__":
    print("This was executed directly")
else:
    print("This was imported as a module")


#import argv from sys module
from sys import argv

#assign command line variables to variables
script, input_file = argv

f = open('test.txt', 'w')
f.write("This is line 1\nThis is line 2\nThis is line 3\n")
f.close()

# this will read the file/ print the contents in the file
def print_all(f):
    print(f.read())

# this will move the cursor to the start of first line in the file/ rewinds our file to the original position
def rewind(f):
    f.seek(0)

# print out a line number followed by a line of the file
def print_a_line(line_count, f):
    print(line_count, f.readline())

#open a file and assign it to a variable
current_file = open(input_file)
print("First let's print the whole file:\n")

# print out the content of the file
print_all(current_file)
print("Now let's rewind, kind of like a tape.")

#rewind the file to the original position
rewind(current_file)
print("Let's print three lines:")

#set the current line, print each line of the file with the number and increase the current number by 1
current_line = 1
print_a_line(current_line, current_file)

#set the current line, print each line of the file with the number and increase the current number by 1
current_line += 1
print_a_line(current_line, current_file)

#set the current line, print each line of the file with the number and increase the current number by 1

current_line += 1
print_a_line(current_line, current_file)