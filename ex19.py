
#this is my own thing
if __name__ == "__main__":
    print("This was executed directly")
else:
    print("This was imported as a module")

# cheese_and_crackers function takes in 2 params (cheese_count, boxes_of_crackers)
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #prints the number of cheese_count
    print("You have {} cheeses!".format(cheese_count))
    #prints the number of boxes_of_crakcers
    print(f"You have {boxes_of_crackers} boxes of crackers!")

    #normal print statement
    print("Man that's enough for a party!")
    #normal print statement, nothing fancy
    print("Get a blanket.\n")

# this will print and the function calls with assigned numbers to  (cheese_count, boxes_of_crackers)
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#3. Write at least one more function of your own design, and run it 10 different ways.

def add_two_numbers(number1, number2):
    print(f"{int(number1)} + {int(number2)} equals {int(number1) + int(number2)}")

number1 = input("Enter a number1: " )
number2 = input("Enter a number2: ")
add_two_numbers(number1, number2)