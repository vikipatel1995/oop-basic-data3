class Animal():

    def __init__(self, name, age, alive = True):
        self.name =name
        self.age =age
        self.alive = alive

    def sleep(self):
        return 'zzzzz'

    def eat(self,food):
        return 'nom nom nom on ' + food

    def potty(self):
        return "uuhhhh"

    def shout_its_name(self):
        return 'MY name is ' + self.name.upper()

    def amend_name(self, new_name):
        self.name = new_name

animal_1 = Animal('Bronco', 24)
print(animal_1.alive)
animal_1.amend_name('tersa')
print(animal_1)

