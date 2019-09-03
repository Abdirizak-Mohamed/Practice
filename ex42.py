## Animal is-a object yes, sort of confusing look at the extra credit 
class Animal(object):
    pass

#make a class dog that is-a
class Dog(Animal):

    def __init__(self, name):
    #from self get name set it to name 
        self.name = name 
        print name 
        
#make a class cat is-a animal 
class Cat(Animal): 

    def __init__(self, name):
    #from self get name set it to name
        self.name = name 

#make a class person is-a object 
class Person(object):
    
    def __init__(self, name):
        
        self.name = name       
        
        #from self get PET set it to none 
        self.pet = None 
        
        print "Name: %s" % name
    
#make a class Employee is-a person
class Employee(Person): 

    def __init__(self, name, salary):
    ##?? DaFuq 
        super(Employee, self).__init__(name)
    #from self get att salary assign to salary 
        self.salary = salary 

    
#make a class Fish hat is-a object 
class Fish(object):
    pass 

#make class salmon that is a fish
class Salmon(Fish): 
    pass 
    
# do it 
class Halibut(Fish):
    pass 


## ROver is-a dog 
rover = Dog("Rover")

#Satan is-a cat
satan = Cat("Satan")

#Mary is-a person
mary = Person("Mary")

#From mary get the pet att set it to satan 
mary.pet = satan 

#set fran to an instance of class Employee with FRANK and 120000 as parammeters 
frank = Employee("Frank", 120000)

#From frank take pet att and set to rover 
frank.pet = rover 

#set fipper to an instance of fish 
flipper = Fish()

#set crouse to an instance of salmon
crouse = Salmon()

#set harry to an instance of Halibut 
harry = Halibut()








