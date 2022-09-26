
#run this script using cmd

#import argv from sys module
from sys import argv

#Get argv command line arguments (when running the file) and assign it 2 variables
script, filename = argv

#Open file using the file ame
txt = open(filename)

#print out the content inthe file
print("Here's your file {}: ".format(filename))

#calls read function with no params
print(txt.read())

#close txt file
txt.close()
#print out instructions and ask user input using input()
print("Type the filename again: ")
file_again = input(" > ")

#open the file using the filename and assign it to the variable
txt_again = open(file_again)

#print out the content of the opened file
print(txt_again.read())

#close txt_again
txt_again.close()



#this is my own thing
if __name__ == "__main__":
    print("This was executed directly")
else:
    print("This was imported as a module")