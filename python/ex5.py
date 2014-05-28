myname = "Mark R. Vasquez"
myage = 44
my_height = 74 #Height in inches. approx.
my_weight = 225 #shockingly high, I know. 
my_eyes = 'brown'
my_teeth = 'Normal'
my_hair = 'brown'
my_height_cent = 74 * 2.54
my_weight_kilos = 225 / 2.20


print "Let's talk about %s." % myname
print "he's %r centimeters tall." % my_height_cent
print "he's about %r kilos" % my_weight_kilos
print "that makes him a little fat."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the amount of coffee." % my_teeth

# the tricky line:

print "If I  add %r, %r, %r and %r I get %r" % (myage, my_height, my_weight, myage, my_height + my_weight)

