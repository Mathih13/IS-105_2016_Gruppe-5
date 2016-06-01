
# Dictionaries translating back and forth from the binary to the letters.
letterToBinary = {'A':'110', 'B':'111', 'C':'010', 'D':'00', 'E':'011', 'F':'10'}
binaryToLetter = dict((v, k) for k, v in letterToBinary.iteritems()) # Inverse version



def encode():
    inp = '' # The variable storing the input.
    output = '' # The variable storing everything we have decoded as a string.
    
    # Ask for code to encode.
    inp = raw_input("Input to encode: ")    
    inp.upper() # Force the input to be upper case since the dictionary is case sensitive
    
    # Iterate through each number, add them to a temp
    # variable and check the "collection" so far for any matches
    # in the dictionary
    total = ''
        
    for character in inp:
        total += character 
        
        if letterToBinary.has_key(total):
            output += letterToBinary[total]
            total = ''
            
    return output


def decode():
    inp = '' # The variable storing the input.
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
            
    
# Choose which mode should be used.
def selectMode():
    inp = raw_input('Type "encode" or "decode" to select mode: ')
    if inp == 'encode':
        print encode()
    if inp == 'decode':
        print decode()
    

selectMode()
    