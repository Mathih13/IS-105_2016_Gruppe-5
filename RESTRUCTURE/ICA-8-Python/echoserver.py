import socket
import sys
from Model.river import *



class Server():

    river = River(['boat isat left','chicken isat left','fox isat left','man isat left', 'grain isat left'])
    
    def __init__(self, host, port):
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Bind the socket to the port
        server_address = (host, port)
        print >>sys.stderr, 'starting up on %s port %s' % server_address
        sock.bind(server_address)
        
        # Listen for incoming connections
        sock.listen(1)

        while True:
            # Wait for a connection
            print >>sys.stderr, 'waiting for a connection'
            connection, client_address = sock.accept()
            
            try:
                print >>sys.stderr, 'connection from', client_address
            
                # Receive the data in small chunks and retransmit it
                while True:
                    self.data = connection.recv(1024)
                    print >>sys.stderr, 'received "%s"' % self.data
                    checkMsg()
                    if self.data:
                        print >>sys.stderr, 'sending data back to the client'
                        connection.sendall('Message Recieved!')
                    else:
                        print >>sys.stderr, 'no more data from', client_address
                        break
            
            except:
                # Clean up the connection
                connection.close()
    
    
    def checkMsg(self):
        if data == 'db':
            connection.sendall(self.checkDB())
        if data == 'getin':
            self.river.getIn()


    def checkDB(self):
        return ' ,'.join(self.river.river_db)
