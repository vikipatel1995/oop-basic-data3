from opp_animal_class import *

def sleep():
    return 'Snoring'
#init. a animal, then call method sleep
# print(Animal().sleep())
# print(sleep())

#print(' hello       '.strip())

print(type('hello'))

animal_instance_ringo = Animal('Ringo', 10)
animal_instance_hugo= Animal('Hugo', 2)
animal_instance_baltazar= Animal('Baltazar', 4)

print(animal_instance_hugo)
print(animal_instance_hugo.name)
#animal_instance_hugo.name =
print('1111111111')

print(animal_instance_hugo.name)
print(animal_instance_baltazar)

animal_instance_hugo.eat('chicken')
print(animal_instance_hugo.number_animal_eaten)
animal_instance_hugo.eat('salad')
animal_instance_hugo.eat('taco')
print(animal_instance_hugo.number_animal_eaten)

