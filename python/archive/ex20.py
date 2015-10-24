# import argv from sys

from sys import argv

# define the imput file with argv

script, input_file = argv

# funtion "print_all"
def print_all(f):
    print f.read()

# function "rewind"
def rewind(f):
    f.seek(0)

# function print_a_line.
def print_a_line(line_count, f):
    print line_count, f.readline()

# open current file:
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all (current_file)

print "now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

