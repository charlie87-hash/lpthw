
# variables assigned to integers
people = 30
cars = 40
trucks = 15

# conditional statements to execute a block of code if an expression is met or not
#check if cars are greater than people or if trucks are lesser than cars
if cars > people or trucks < cars:
    print("We should take the cars.")

#otherwise, check if cars are lesser than people
elif cars < people:
    print("We should not take cars")

#if neither if and elif condtion is true
else:
    print("We can't decide")
# check if trucks are greater than cars and if people are lesser than trucks
if trucks > cars and people < trucks:
    print("That's too many trucks.")

#check if trucks are lesser than cars
elif trucks < cars:
    print("Maybe we could take the trucks.")
#if neither if and elif condtion is true
else:
    print("We still can't decide.")

#check if people are greater than trucks
if people > trucks:
    print("Alright, let's just take the trucks.")
#if not true
else:
    print("Fine, let's stay home then.")