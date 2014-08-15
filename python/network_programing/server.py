import socket

# create a socket object
s = socket.socket()
print "Socket successfully created."

# reserve a port: port 9999
port = 9999

# Next bind to the port
s.bind(('',port))
print "socket binded to %s" %(port)

#put the socket into listening mode:
s.listen(5)
print "socket is listening"

while True:
    # Establish connection with client. 
    c, addr = s.accept()
    print 'Got connection from', addr

    # send a thank you message to the client. 
    c.send('Thank you for connection')
    # Close the connection with the client
    c.close()


