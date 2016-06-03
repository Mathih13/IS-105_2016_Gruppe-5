from sm import *
from river import *

#Dictionary and list of possible commands and their explanation
commandexplaination = {'chicken' : 'cross with chicken', 'fox' : 'cross with a fox', 'grain' : 'cross with grain', 'none' : 'cross without any items', 'quit' : 'ends the simulation'}
possiblecommands = ['chicken', 'fox', 'grain', 'none', 'quit', 'solvePuzzle', 'db']


def db():
    r.database()
    fullLoop()

#Function to print the explanation of possible commands to the user.
def help():
    print 'List of possible commands:'
    print 'chicken: '+commandexplaination['chicken']
    print 'fox: '+commandexplaination['fox']
    print 'grain: '+commandexplaination['grain']
    print 'none: '+commandexplaination['none']
    print 'quit: '+commandexplaination['quit']
    fullLoop()
    

#
def returnInput():
    print '------------------------------------------------------------'
    print 'Which good would you like to move? Press return to step through the simulation. Type help for commands'
    inp = raw_input('')
    return inp


def skipper():
    raw_input('')

def fullCrossItem(good):
    r.putIn(good)
    skipper()
    r.getIn()
    skipper()
    r.crossriver()
    skipper()
    r.getout()
    skipper()
    r.takeOut(good)
    fullLoop()

def fullCrossNoItem():
    r.getIn()
    skipper()
    r.crossriver()
    skipper()
    r.getout()
    skipper()
    fullLoop()
    
    
    
def quickCrossItem(good): # A version that does not require return key inputs to step through the process, nor loops back to command input. Mostly used for testing/solving quickly.
    r.putIn(good)
    r.getIn()
    r.crossriver()
    r.getout()
    r.takeOut(good)
    
def quickCrossNoItem(): # A version that does not require return key inputs to step through the process, nor loops back to command input. Mostly used for testing/solving quickly.
    r.getIn()
    r.crossriver()
    r.getout()
    
def solvePuzzle(c, g, f):
    quickCrossItem(c)
    quickCrossNoItem()
    quickCrossItem(g)
    quickCrossItem(c)
    quickCrossItem(f)
    quickCrossNoItem()
    quickCrossItem(c)    
    
    
    

def fullLoop():  
    temp = returnInput()
    if (temp == 'none'):
        fullCrossNoItem()
    elif (temp == 'help'):
        help()
    elif (temp == 'quit'):
        quit()
    elif (temp not in possiblecommands):
        print '---Invalid command!---'
        help()
    # Quick solution for testing purposes
    elif (temp == 'solvePuzzle'):
        solvePuzzle('chicken', 'grain', 'fox')
    elif (temp == 'db'):
        db()
    else:
        fullCrossItem(temp)
        


# Start the river simulation, update and show state. Start Main loop
r = River([['boat isat left'],['chicken isat left'],['fox isat left'],['man isat left'], ['grain isat left']])
r.start()
r.updateWorld()
fullLoop()

# Grab the possibility to end the simulation from river.py
def quit():
    r.killWorld()
    


    
    