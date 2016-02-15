# -*- coding: utf-8 -*-

import random
import itertools
import collections
import sys

#Klover instead of kløver. Something weird happening when trying to use æøå in lists even after utf-8 has been specified. Contact janis if there is time?
SUITS = ("Hjerter", "Spar", "Ruter", "Klover")
RANKS = "2", "3", "4", "5", "6", "7", "8", "9", "10", "knekt", "dame", "konge", "ess"

DECK = list(''.join(card) for card in itertools.product(SUITS, RANKS))

#Dict(Dictionary) (zip) creates a list with a specified range. In this case the range is a deck of 52 cards. 
#In this deck there is a range of 13 cards, the value that the cards can hold.

ORDER_LOOKUP = dict(zip(DECK, range(52)))
RANKS_LOOKUP = dict(zip(RANKS, range(13)))
SUITS_LOOKUP = dict(zip(SUITS, range (4)))


#Config/Setup variables to be used
pairplayer = 0  #What player has gotten pairs

#Booleans to determine if any player has been dealt pair, straight or flush
haspair = False
hasstraight = False
hasflush = False

#Lists containing the number of the players that have been dealt pair, straight or flush
playerswithpairs = {}
op = {}
playerswithstraight = []
playerswithflush = []

#Empty string to be filled with card information for winner print
pairs = ''

#All posibilities for straights based on the card value organized in lists.
#If time, look into creating a dict based solution as with the checkCards function. Note to self: Might interfere with combo_collection?
combo= {}

'''This method should be a lot cleaner and more efficient in the long run than having several predetermined lists.s
This method (not the exact code) was shamelessly copied from user unutbu at stackoverflow.com : Refer to that user account for further reading or if anything goes horribly wrong.'''

for i in range (1, 11):
    combo['combo_straight%s'%i]= [i, i+1, i+2, i+3, i+4]


#Collection of all the possibilities of straights for easier use.
combo_collection = combo['combo_straight1'], combo['combo_straight2'], combo['combo_straight3'], combo['combo_straight4'], combo['combo_straight5'], combo['combo_straight6'], combo['combo_straight7'], combo['combo_straight9'], combo['combo_straight10']





def shuffle():
    #Get global variables from other functions.
    global haspair
    global hasstraight
    global hasflush
    #Request input of number of players. If number is invalid, terminate program.
    '\n''NOTE: Not inputting anything still results in a crash. Look into possible solution if we have the time'''
    
    players = int(input("How many players?(1-5) "))
    if (players > 5 or players == 0):
	print "Warning: The game cannot hold more than 5 players. Shutting down..."
	sys.exit()
	
    #Shuffle the deck of cards!
    random.shuffle(DECK)
    
    #These have to be reset out of the loop as they are supposed to be calculated after the loop!   
    playerswithpairs = []
    playerswithstraight = [] 
    
    #Grant each player different cards from the shuffled deck:
    for i in range(0, players):
	i = i+1
	if (i == 1):
	    cardstart = 2
	    cardfinish = 7
	elif (i == 2):
	    cardstart = 8
	    cardfinish = 13
	elif (i == 3):
	    cardstart = 14
	    cardfinish = 19	
	elif (i == 4):
	    cardstart = 20
	    cardfinish = 25
	elif (i == 4):
	    cardstart = 26
	    cardfinish = 31
	elif (i == 5):
	    cardstart = 32
	    cardfinish = 37	
	    
	#Reset the "Has combos" boolean variables in between creating and checking each players hands
	hasstraight = False
	haspair = False	
	hasflush = False
	 	  	    
	#Insert the appropriate cards from the randomly shuffled deck
	hand = DECK[(cardstart):(cardfinish)]
	
	#Input the cards from the shuffle to the checkCards function.
	#Variable i is still the number of the player
	checkCards(hand, i)      
	
	#In the name of modulation, check the players results in a different function.
    playerCheck()
    
  
    #Send the user back to the reset function in order to be able to start a new round.
    resetRound()



def checkCards(hand, player):
    #This function uses a lot of variables from outside. Please add or remove global variables with care
    global haspair
    global hasstraight
    global hasflush
    global playerswithpairs
    global playerswithflush
    global pairplayer
    global pairs
    global op
    
    #Present the player number
    print "CARDS FOR PLAYER ",player,":\n"
    
    
    '''Create a dictionary containing 14 lists. These lists will contain the amount of with equal value among the cards in the players hand.
    I.E if dct['value5'] has at least 2 items, the player has at least a pair of fives.
    
    This method should be a lot cleaner and more efficient in the long run than having a long "list of manual lists" in the middle of the function.
    
    This method (not the exact code) was shamelessly copied from user unutbu at stackoverflow.com : Refer to that user account for further reading or if anything goes horribly wrong.'''
    
    dct = {}
    for i in range (1, 15):
	dct['value%s'%i] = []
		
		
    #Reset the pairs string, straight list and flush to make sure there is nothing left of the previous hand.
    #NOTE: The straight list will be appended throughout the loop below. It will then be ordered in ascending order(int value) and used to detect if the player has been dealt a straight. 
    pairs = ''
    straight = []
    flush = []
    pairscore = 0
    
    
    #Loop throughout the players hand
    for i in hand:
	#Check if the card found ends with corresponding number value
	if i.endswith('2'):
	    #Attach to the appropriate list in the dct created above
	    dct['value2'].append(i)
	    #Check if there are currently at least 2 items in the list. If true, set the global haspair to true and add the corresponding "wintext" to the pairs string.
	    if (len(dct['value2']) == 2):
		pairs += 'Par i 2, \n'
		haspair = True
		pairscore = 2
	    #Append the int value to the straight list. Purpose explained above
	    straight.append(2)
	    
	    
#Repeat this 13 more times:
        if i.endswith('3'):
	    dct['value3'].append(i)
	    if (len(dct['value3']) == 2):
		pairs += 'Par i 3, \n'
		haspair = True
		pairscore = 3
	    straight.append(3)
        if i.endswith('4'):
	    dct['value4'].append(i)
	    if (len(dct['value4']) == 2):
		pairs += 'Par i 4, \n' 
		haspair = True
		pairscore = 4
	    straight.append(4)
        if i.endswith('5'):
	    dct['value5'].append(i)
	    if (len(dct['value5']) == 2):
		pairs += 'Par i 5, \n'
		haspair = True
		pairscore = 5
	    straight.append(5)
        if i.endswith('6'):
	    dct['value6'].append(i)
	    if (len(dct['value6']) == 2):
		pairs += 'Par i 6, \n' 
		haspair = True
		pairscore = 6
	    straight.append(6)
        if i.endswith('7'):
	    dct['value7'].append(i)
	    if (len(dct['value7']) == 2):
		pairs += 'Par i 7, \n'
		haspair = True
		pairscore = 7
	    straight.append(7)
        if i.endswith('8'):
	    dct['value8'].append(i)
	    if (len(dct['value8']) == 2):
		pairs += 'Par i 8, \n'
		haspair = True
		pairscore = 8
	    straight.append(8)
        if i.endswith('9'):
	    dct['value9'].append(i)
	    if (len(dct['value9']) == 2):
		pairs += 'Par i 9, \n' 
		haspair = True
		pairscore = 9
	    straight.append(9)
        if i.endswith('10'):
	    dct['value10'].append(i)
	    if (len(dct['value10']) == 2):
		pairs += 'Par i 10, \n'
		haspair = True
		pairscore = 10
	    straight.append(10)
        if i.endswith('kt'):
	    dct['value11'].append(i)
	    if (len(dct['value11']) == 2):
		pairs += 'Par i knekt, \n'
		haspair = True
	    straight.append(11)
        if i.endswith('me'):
	    dct['value12'].append(i)
	    if (len(dct['value12']) == 2):
		pairs += 'Par i dame, \n'
		haspair = True
		pairscore = 11
	    straight.append(12)
        if i.endswith('ge'):
	    dct['value13'].append(i)
	    if (len(dct['value13']) == 2):
		pairs += 'Par i konge, \n'
		haspair = True
		pairscore = 12
	    straight.append(13)
        if i.endswith('ss'):
	    #Since the Ace has the possibility of being both value of 14 and one, we chose to take the "easy" route and make it a 50% chance for it to be either.
	    r = random.randint(0,100)
	    if r < 50:
		straight.append(14)
	    else: 
		straight.append(1)	    
	    dct['value14'].append(i)
	    if (len(dct['value14']) > 1):
		pairs += 'Par i ess, \n'
		haspair = True
		pairscore = 13
		
		
    #Make it look nice
	print i + '\n'
    print '-----------------------------'

    '''Checks for pairs'''
    #Have this player been dealt a pair? If so, add the players number to the pool of players that have been dealt a straight
    if haspair == True:
	playerswithpairs['Player %s'%player] = pairscore
	

	

    '''Checks for straight'''
    #Sort the straight list in ascending order, run through the combo_collection list defined at the start and check if any of it matches our current straight
    #If match, alert that there is a straight and add the players number to the pool of players that have been dealt a straight
    straight.sort()
    for combo in combo_collection:
	if straight == combo:
	    hasstraight = True
	    print 'straight!'
	    playerswithstraight.append(player)
	    
    
   
    '''Checks for flush'''
    #Reset all the variables for a recount
    h = 0
    r = 0
    s = 0
    k = 0
    #Go through all cards, add up the number of each suit in appropriate variable
    for card in hand:
	if card.startswith('H'):
	    h += 1
	if card.startswith('R'):
	    r += 1
	if card.startswith('S'):
	    s += 1
	if card.startswith('K'):
	    k += 1
	    
    #If any reach 5, lgo that there is a flush and add players number to the pool of players that have been dealt a flush
    if ((h or r or s or k) == 5):
	playerswithflush.append(player)
	hasflush = True
    
    
    
    '''WTF is this??'''
  '''  if (len(playerswithpairs)) > 0:
	for playerwithpair in playerswithpairs:
	    pairplayer = playerwithpair
    '''
   
    
    
    
    
    
def playerCheck():
    #Get global variables from other functions.
    global hasflush
    global haspair
    global hasstraight
    global pairplayer
    global pairs
    global op
    
    #1st check: If only pairs have been dealt.
    if (haspair == True and hasstraight != True and hasflush != True):
	scorelist = []
	op = dict((value, key) for key, value in playerswithpairs.iteritems())
	if (len(playerswithpairs) >= 2):
	    for i in playerswithpairs:
		scorelist.append(playerswithpairs[i])
	    t = max(scorelist)
	    if (t == 11):
		t = 'Jacks'
	    elif (t == 12):
		t = 'Queens'
	    elif (t == 13):
		'Kings'
	    elif (t == 14):
		t = 'Aces'	    
	    print 'Winner is: ' ,op[t], ' with a pair of', (t), '\n'
	    
	    #print 'Player', pairplayer, 'har',pairs,'og vinner!'    
    


    
    
    





#This function handles the reset loop of the poker game as a whole
#It should NOT contain resetting of any variables
#inp variable currently not in use. Remove?
def resetRound():
    print ''
    inp = raw_input('Trykk på returtast for å stokke på nytt')
    print ''
    
    #Restart the round/shuffle loop.
    shuffle()
    

    
#Automatically call the shuffle function on run and start the first round of poker!
shuffle()








''' value2 = []
    value3 = []
    value4 = []
    value5 = []
    value6 = []
    value7 = []
    value8 = []
    value9 = []
    value10 = []
    value11 = []
    value12 = [] 
    value13 = []
    value14 = []'''