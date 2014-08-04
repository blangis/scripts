def tech_books_and_fiction(tech_books, fiction):
    print "You have %d tech books" % tech_books
    print "You have %d fiction books" % fiction
    print "That's a lot of books"
    print "You better start reading."

print "This is a boring count:"
tech_books_and_fiction(35,55)

print "Using variables:"
tech_books = 35
fiction = 45

tech_books_and_fiction(tech_books, fiction)

print "I want to sell at least ten of each type, so I will have less to read:"
tech_books = 35 - 10
fiction = 45 - 10

tech_books_and_fiction(tech_books, fiction)


