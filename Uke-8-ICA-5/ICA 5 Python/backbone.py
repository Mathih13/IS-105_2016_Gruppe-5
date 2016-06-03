import re


#Create list of numbers
def createList(a, b):
    randlist = []
    for i in range (a, b):
        randlist.insert(i, i)    
    return randlist


#Create list of words
def readList(text):
    file = open(text, 'r')
    # .lower() returns a version with all upper case characters replaced with lower case characters.
    text = file.read().lower()
    file.close()
    # replaces anything that is not a lowercase letter, a space, or an apostrophe with a space:
    text = re.sub('[^a-z\ \']+', " ", text)
    words = list(text.split())
    return words
