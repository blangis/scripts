#!/usr/bin/env python

two_packs = 6
four_packs = 1
price_per_gummy = 5.50
discount = 20.00

print "I have this many gummies in two packs:", 2 * two_packs
print "I have this many gummies in four packs", 4 * four_packs
print "The price per gummy is", price_per_gummy
print "The total number of gummies that I got is", 2 * two_packs + 4 * four_packs
print "The actual price I paid would have been", (2 * two_packs + 4 * four_packs) * price_per_gummy
print "I had a discount though, which was", discount
print "So I paid", (2 * two_packs + 4 * four_packs) * price_per_gummy - 20
