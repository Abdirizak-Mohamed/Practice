
name = raw_input("Hi there sir! What is your name  ------->  ") 
age = raw_input("Can I also ask how old you are sir ------->  ")
year = raw_input("Out of interest what year is it? -------->   ")
bday = 100 - int(age) 
year_of_100 = bday + int(year)
print "Oh cangrats, On %s it will be your centenary" % year_of_100