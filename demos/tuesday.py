"""
What kinds of linked list things might we make?
- Stack?
- Doubly-Linked List?
- Skip-List?
- n-connections?!
now we can design a little bit about how to build these classes (reusability is great!)
Where and what should we abstract? Lead to a talk about different ways of sharing code Inheritance vs Interfaces. Python doesn't do interfaces. lol. Multiple inheritance!
Different implementations of the same things Encapsulation + Polymorphism! method overriding.
"""










# Building a web server from scratch
# What is a socket?How is my computer connected to the web? How does it know what it is working with?
# How does my computer connect to the internet?
# Computer connects to the internet by receiving signals, either wirelessly or through a cable. Some kind of hardware receives this information. A port is a communication endpoint in an OS. It is an interface for the OS to interact with different network services or processes. A port typically has a method or PROTOCOL of communication it adheres to and an IP Address (16-bit number). About 1024 well known port numbers are reserved by convention for certain services. The key idea here is that we can use python to connect to a port and listen for information to hit it!

# So we just have to build a class that listens to a port, and responds to it!
# So how does python talk to ports? SOCKETS! 2way pipes of insanity!
# baiscally, we have two versions: client and server sockets. A client socket interaction typically 
# to the docs!
import socket

HOST = ''
PORT = 9000
# create a socket specifying family, type, and IP(default 0)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind it to port and host
s.bind((HOST, PORT))
# listen to the port, specify number of connections to keep open
s.listen(1)
# store some information connection to port
conn, addr = s.accept()
print('Connected By,' addr)
# while the connection exists
While 1:
    # accept connections from the outside
    
    if not data: break
    conn.sendall(data)