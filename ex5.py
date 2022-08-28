name = 'Charles Ongom'
age = 60 #think about it
height = 7.1 # inches
height_in_cm = height * 2.54

weight = 180 #lmbs

eyes = 'brown'
teeth = 'white'
hair = 'Brown'

print(f"let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"Hs teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + height + weight
print(f"if I add {age}, {height}, and {weight} I get {total}.")


#my own thing
if __name__ == "__main__":
    print ("Executed when invoked directly")
else:
    print ("Executed when imported")