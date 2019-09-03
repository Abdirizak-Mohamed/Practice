from sys import argv 
#from command line import script and filename
script, filename = argv 
#open filename and save it as text 
txt = open(filename)
#First display filename then print it as text
print "Here's your file %r:" % filename 
print txt.readline(10)
#save second input of filename as again then
print "Type the filename again:" 
file_again = raw_input(">")
#open and save as 
txt_again = open(file_again)
#print saved text 
print txt_again.readline(2)
