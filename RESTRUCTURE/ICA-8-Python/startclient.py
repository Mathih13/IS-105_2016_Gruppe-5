from Display.mainFrame import *
from Server import clientController
from Server.echoclient import Client
from Tkinter import *

'''THIS PYTHON FILE "STARTS" THE PROGRAM!'''








# Create the Tkinter frame, give it a title
# then enter mainloop.
root = Tk()
frame = ourFrame(2000, 1500, root)
rc = riverController(frame.master, frame.canvasData, Client('localhost', 5005))
root.title('River Crossing')
root.mainloop()
