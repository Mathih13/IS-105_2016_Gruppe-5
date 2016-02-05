# -*- coding: utf-8 -*-


def code():
    '''
    Implements a code: ASCII mapping from binary string to ASCII string
    and the other way around. Load the tables in memory. 
    '''

    

    convert = {'101':'Helse- og Idrett', '100':'Humaniora og Pedagogikk', '010':'Kunstfag', '00':'Teknologi og Realfag', '011':'Lærerutdanning', '11':'Økonomi og Samfunnsvitenskap'}
    
    return (convert) # Load table into memory

inp = raw_input('Input message to be decoded: ')

for letter in inp:
    
    print letter
    print test
        