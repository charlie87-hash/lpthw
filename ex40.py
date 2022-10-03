'''
#class lets you structure your code in a particular way

mystuff = {'apple':"I AM APPLES"}
print(mystuff['apple'])

import mystuff
mystuff.apple()
print(mystuff.tangerine)


mystuff['apple'] # get apple from dict
mystuff.apple() # get apple from the module
mystuff.tangerine # same thing, it's just a variable

Classes Are Like Modules, we can create many objects out of classes, works as a factory lol
What is an object - comes out of the class by instatiate

class mystuff(object):
    def __init__(self): # empty object Python made for me, and I can set variables on it just like you would with a module, dictionary, or other object.
        self.tangerine = "And now a thousand years between" # set a variable ^^^

    def apple(self):
        print("I AM CLASSY APPLES")

thing = mystuff() #this an object created - instatiate
thing.apple() #now it can be used to call other functions on it after creation
print(thing.tangerine)


# dict style
mystuff['apples']

# module style
mystuff.apples()
print(mystuff.tangerine)

# class style
thing = mystuff()
thing.apples()
print(thing.tangerine)
'''

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song([ "Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()