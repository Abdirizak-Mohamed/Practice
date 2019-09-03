print "Input the name of doc you want to open."
file_name = raw_input(">")
txt = open(file_name) 
print "Here is the text for %s." % file_name

print txt.read()

print "Now input the filename again" 
txt_again = raw_input()
read_again = open(txt_again)

print read_again.read()

