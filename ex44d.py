class Parent(object):
    
    def override(self):
        print "PARENT override()"
    
    def implicit (self):
        print "Parent implicit"
    
    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    
    def override(self):
        print "CHILD override()"
    
    def altered(self):
        print "CHILD BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT ALTERED"
    
dad = Parent()
son = Child()




print "\n ---------\n"

dad.override()
dad.implicit()
dad.altered()

print "\n ---------\n"

son.implicit()
son.override()
son.altered()