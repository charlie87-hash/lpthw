
## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

##Dog is a Animal
class Dog(Animal):
    def __init__(self, name):
        ##? self.name has a name
        self.name = name

# Cat is a Animal
class Cat(Animal):
    def __init__(self, name):
        ##? self.name has a name
        self.name = name

#Person is a object
class Person(object):
    def __init__(self, name):
        #self.name is a name
        self.name = name
        #self.name is a None
        self.pet = None

#Employee is a person
class Employee(Person):
    def __init__(self, name, salary):
        ##employee has a name
        super(Employee, self).__init__(name)
        ##self.salary has a salary
        self.salary = salary

# Fish is a object
class Fish(object):
    pass

#Salmon is a Fish
class Salmon(Fish):
    pass

#Halibut is a Fish
class Halibut(Fish):
    pass

## rover is a Dog
rover = Dog("Rover")

## satan is a Cat
satan = Cat("Satan")

## Mary is a person
mary = Person("Mary")

# mary has a pet called satan
mary.pet = satan

#frank has a salary of 120000
#frank is a employee
frank = Employee("Frank", 120000)

#frank has a pet called rover
frank.pet = rover

#flipper is a fish
flipper = Fish()

#crouse is a salmon
crouse = Salmon()

#harry is a halibut
harry = Halibut()