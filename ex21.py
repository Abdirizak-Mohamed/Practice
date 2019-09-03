def add(a, b): 
    return a + b 
    
def subtract(a, b):    
    return a - b 
    
def multiply(a, b): 
    return a * b 
    
def divide(a, b): 
    return a / b

print "Let's do some math with just functions!\n" 

age = add(24, 34) 
height = subtract(78,4) 
weight = multiply(90, 2) 
iq = divide(100, 2) 

print "age: %d, height: %d weight: %d, iq: %d" % (age, height, weight, iq)


#a puzzle for the extra credit, type it in anyway. 
print "Here is a puzzle." 

damn = add(4, divide(multiply(65, 2), divide(25, 5)))

print "That becomes", damn, "Can you do it by hand?\n"


 