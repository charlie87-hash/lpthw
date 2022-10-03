'''
1. Actions on the child imply an action on the parent.
2. Actions on the child override the action on the parent.
3. Actions on the child alter the action on the parent.
'''

class Parent(object):
    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

class Parent(object):
    def override(self):
        print("PARENT override()")

class Child(Parent):
    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()

# Alter Before or After
class Parent(object):
    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered")

dad = Parent()
son = Child()

dad.altered()
son.altered()

# MRO- Method Resolution Order and C3 - super()

class Child(Parent):
    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self). __init__()
## This is pretty much the same as the Child.altered example above, except I’m setting some variables in the __init__ before having the Parent initialize with its Parent.__init__.


class Other(object):
    def override(self):
        print("OTHER override()")
    def implicit(self):
        print("OTHER implicit()")
    def altered(self):
        print("OTHER altered()")

class Child(object):
    def __init__(self):
        self.other = Other()
    def implicit(self):
        self.other.implicit()
    def override(self):
        print("CHILD override()")
    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()
son.implicit()
son.override()
son.altered()