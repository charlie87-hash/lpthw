
#while loop while continue until a certain condition is met
#use while loops sparingly
#take note of infinite loops
#boolean checks help terminate the loop

i = 0
numbers = []


while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)
    i += 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print("num:---->", num)