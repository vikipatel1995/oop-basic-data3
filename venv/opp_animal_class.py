class Animal():
# Classes are the base of OOP- OBJECT ORIENTATED PROGRAMMING
#***They were cookie cutters for objects***
#SYNTAX:
#From classes you initialize indvidual instances of this class
#Classes hold method (methods: are function which depend on...
# ...instance of classes they can only be called on instances of a class)

    def __init__(self):  #constructor method runs whenever an instance is created
        self.name = 'Ringo' #property of the animals
        self.species = 'Lizard'
        self.age = 7

    #method of class objects - instances
    def sleep(self):    # self refers to the instances if get classed upon - self
                        #populates tbe self with the instance.
        return "zzzz"

    def eat(self, food):
        return 'nom nom nom this was some good ' + food

    def potty(self):
        return "uuhhhh"

animal_1 = Animal() #creating one instance of CLass Animal
# print(animal_1)
# print(type(animal_1))

#Calling method on instance of animal
print(animal_1.sleep())
print(animal_1.eat('meat salad'))
print(animal_1.potty())

#Calling method on instances if animals
print("Animal Name:", animal_1.name , "Age:", animal_1.age)
print(animal_1.age)