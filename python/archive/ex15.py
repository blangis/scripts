from sys import argv

print "What is the name of your file?"
filename = raw_input(">")

txt = open(filename)

print "Here is your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = filename
#file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()


