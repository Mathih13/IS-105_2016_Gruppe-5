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
        # If player does not choose a valid option, the program will shut down.
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
    choice = raw_input("Your Choice: ")
    return choice

 
 


playerChoice = startgame()

p = checkPlayer()
c = randomNr()



def play():
    if p == 1:
        print("You chose rock.")
        if c == 1:
            print("The computer chose rock too, it's a tie.")
        elif c == 2:
            print("The computer chose paper, you lose.")
        elif c == 3:
            print("The computer chose scissor, you win!")
            
    if p == 2:
        print("You chose paper.")
        if c == 1:
            print("The computer chose rock, you win!")
        elif c == 2:
            print("The computer chose paper too, it's a tie.")
        elif c == 3:
            print("The computer chose scissor, you lose.")
            
    if p == 3:
        print("You chose scissor.")
        if c == 1:
            print("The computer chose rock, you lose.")
        elif c == 2:
            print("The computer chose paper, you win!")
        elif c == 3:
            print("The computer chose scissor too, it's a tie")

            return
        
play()