print "How high do you want to go?" 
mohamed = int(raw_input("--->")) 

print "What would you like the increment to be?"
abdi = int(raw_input("--->"))

def first_loop ():
    i = 0
    numbers = [] 
  
    while i < mohamed:
        print "At the top i is %d" % i 
        numbers.append(i)
    
        i = i + abdi 
        print "Numbers now:", numbers 
        print "At the bottom i is %d" % i 
        
        for num in numbers: 
            print num 

print first_loop()