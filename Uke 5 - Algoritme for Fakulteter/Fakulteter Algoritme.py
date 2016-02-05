# -*- coding: utf-8 -*-


def code():


    convert = {'101':'Helse- og Idrett', '100':'Humaniora og Pedagogikk', '010':'Kunstfag', '00':'Teknologi og Realfag', '011':'Lærerutdanning', '11':'Økonomi og Samfunnsvitenskap'}
    
    inp = raw_input('Input message to be decoded: ')    
    r=''
    prev=''
    prev2=''
    t=''
    c=''
    for i in range(0, len(inp)):
        r = inp[i]
        prev = inp[i-1]
        prev2 = inp[i-2]
        
        if r == '1' and prev == '1' and prev2 == '0':
            t = '011'
            c += convert[t]
    
    print c    







code()