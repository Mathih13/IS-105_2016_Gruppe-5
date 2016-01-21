# Import random functionality
import random
import sys


# Check the choice the player made and assign numeric value.
def checkPlayer():
    if playerChoice == "rock":
        x = 1
        
    
    elif playerChoice == "paper":
        x = 2 
        
       
    elif playerChoice == "scissors":
        x = 3
    else:
        x = 0
        sys.exit("No valid option chosen. Shutting down.")
    return x

# Generate a random choice for computer.
def randomNr():   
    i = (random.randint(1,3))
    return i

def startgame():
    #Welcome Text and Call to Action
    print "Welcome to Rock, Paper, Scissors!"
    print "#####################################"
    print "To play, type either rock, paper or scissors."
    print ""
    return

 
 
startgame()
playerChoice = raw_input("Your Choice: ")

p = checkPlayer()
c = randomNr()

print "Player: ", p,
print "Computer: ", c,







 
