

def checkPlayer():
    if playerChoice == "rock":
        p = 1
        
    
    elif playerChoice == "paper":
        p = 2 
        
       
    elif playerChoice == "scissors":
        p = 3

    return 

#Welcome Text and Call to Action
print "Welcome to Rock, Paper, Scissors!"
print "#####################################"
print "To play, type either rock, paper or scissors."
print ""

playerChoice = raw_input("Your Choice: ")
checkPlayer()

import random

def randomNr():   
    print(random.randint(1,3))
    return
randomNr()




 
