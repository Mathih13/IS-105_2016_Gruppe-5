# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


from pylab import *

terje = {'Slow_Search': 0.623, 'Fast_Search' : 0.088}
mathias = {'Slow_Search': 0.651, 'Fast_Search': 0.111}
erik = {'Slow_Search' : 2.666, 'Fast_Search' : 0.402}
eirik = {'Slow_Search' : 0.546, 'Fast_Search' : 0.079}



objects = ('Terje', 'Mathias', 'Erik', 'Eirik')
y_pos = np.arange(len(objects))

def slowSearch():
    performance = [terje['Slow_Search'],mathias ['Slow_Search'], erik ['Slow_Search'], eirik ['Slow_Search']]
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Sekunder')
    plt.title('Slow Search etter et tall mellom 1 og 1million')
    
    plt.show()
    
def fastSearch():
    performance = [terje['Fast_Search'], mathias['Fast_Search'], erik['Fast_Search'], eirik['Fast_Search']]
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Sekunder')
    plt.title('Fast Search etter et tall mellom 1 og 1million')
    
    plt.show()    
    
    
def nmbrStart():    
    i = raw_input('Fast eller Slow: ')
    if i == 'Fast':
        fastSearch()
    elif i == 'Slow':
        slowSearch()
        
        