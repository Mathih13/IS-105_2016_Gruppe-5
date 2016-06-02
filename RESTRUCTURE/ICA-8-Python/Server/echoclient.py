import socket
import sys


class Client():
    
    def __init__(self, host, port):
        
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect the socket to the port where the server is listening
        server_address = (host, port)
        print >>sys.stderr, 'connecting to %s port %s' % server_address
        self.sock.connect(server_address)


    def send(self, msg):
        try:
            
            # Send data
            message = msg
            print >>sys.stderr, 'sending "%s"' % message
            self.sock.sendall(message)
        
            # Look for the response
            amount_received = 0
            amount_expected = len(message)
            
            while amount_received < amount_expected:
                data = self.sock.recv(1024)
                amount_received += len(data)
                print >>sys.stderr, 'received "%s"' % data
                return data
            
        finally:
            pass
          
            
    def close(self):
        print >>sys.stderr, 'closing socket'
        self.sock.close()
        


