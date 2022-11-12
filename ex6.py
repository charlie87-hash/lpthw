
# Strings and Text
#Define a variable and assign it to a value 10
types_of_people = 10

# Insetrt the variable into a new string and assign it to the variable x
x = f"There are  {types_of_people} types of people"

#Binary is a variable for binary string
binary = "binary"

#do_not is a variable for don't string
do_not = "don't"

# Embed those two strings into a new string and assign it to y
y = f"Those who know {binary} and those who {do_not}."

#outputs variable x
print(x)

#output variable y
print(y)

#outputs variable x using format method

print(f"I said: {x}")

#outputs variable y using format method
print(f"I also said: {y}")

#sets hilarious to False or hilarious is a variable for False(boolean)
hilarious = False

# joke_evaluation is a variable here for the string below
joke_evaluation = "Isn't that joke so funny?! {}"

#outputs joke_evaluation with false using format
print(joke_evaluation.format(hilarious))

# w is a defined variable
w = "This is the left side of..."

#e is a defined variable
e = "a string with a right side."

#string concatnation output
print(w + e)

if __name__ == "__main__":
    print("This was executed directly")
else:
    print("This was imported as a module")