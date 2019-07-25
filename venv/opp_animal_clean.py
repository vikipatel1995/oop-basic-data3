class Animal():

    def __init__(self, name, age):
        self.name =name
        self.age =age
        self.alive = True

    def sleep(self):
        return 'zzzzz'

    def eat(self,food):
        return 'nom nom nom on ' + food

    def potty(self):
        return "uuhhhh"

    def shout_its_name(self):
        return 'MY name is ' + self.name.upper()

    