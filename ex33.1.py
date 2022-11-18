

#Convert this while-loop to a function that you can call, and replace 6 in the test (i < 6) with a variable.

def counter(iteration):
    i = 0
    numbers = []

    while i < iteration:
        print(f"At the top i is {i}")
        numbers.append(i)
        i += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print("num:---->", num)

counter(12)