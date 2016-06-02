from Display.mainFrame import *
from Server import clientController
from Tkinter import *

'''THIS PYTHON FILE "STARTS" THE PROGRAM!'''








# Create the Tkinter frame, give it a title
# then enter mainloop.
root = Tk()
frame = ourFrame(2000, 1500, root)
rc = riverController(frame.master, frame.canvasData)
root.title('River Crossing')
root.mainloop()
