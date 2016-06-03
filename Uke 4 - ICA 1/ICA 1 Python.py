
# Dictionaries translating back and forth from the binary to the letters.
letterToBinary = {'X':'0', 'Y':'10', 'Z':'11'}
binaryToLetter = dict((v, k) for k, v in letterToBinary.iteritems()) # Inverse version




def decode():
    inp = ''
    output = '' # The variable storing everything we have decoded as a string.
    
    # Ask for code to decode.
    inp = raw_input("Input to decode: ")
    
    
    # Iterate through each number, add them to a temp
    # variable and check the "collection" so far for any matches
    # in the dictionary
    total = ''
    
    for character in inp:
        total += character # Add current to total "chunk" of characters so far
        
        # Does the dictionary contain any matches for what we have so far?
        if binaryToLetter.has_key(total):
            output += binaryToLetter[total]
            total = '' # Reset the "total" for the next "chunk" of characters
    return output
            
    
print decode()