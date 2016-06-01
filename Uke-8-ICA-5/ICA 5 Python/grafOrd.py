# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


from pylab import *

terje = {'Slow_Search': 0.021, 'Fast_Search' : 0.016}
mathias = {'Slow_Search': 0.028, 'Fast_Search': 0.014}
erik = {'Slow_Search' : 0.082, 'Fast_Search' : 0.065}
eirik = {'Slow_Search' : 0.017, 'Fast_Search' : 0.018}



objects = ('Terje', 'Mathias', 'Erik', 'Eirik')
y_pos = np.arange(len(objects))

def slowSearch():
    performance = [terje['Slow_Search'],mathias ['Slow_Search'], erik ['Slow_Search'], eirik ['Slow_Search']]
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Sekunder')
    plt.title('Slow Search etter et ord i Hamlet.txt')
    
    plt.show()
    
def fastSearch():
    performance = [terje['Fast_Search'], mathias['Fast_Search'], erik['Fast_Search'], eirik['Fast_Search']]
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Sekunder')
    plt.title('Fast Search etter et ord i Hamlet.txt')
    
    plt.show()    
    
def wordStart():    
    i = raw_input('Fast eller Slow: ')
    if i == 'Fast':
        fastSearch()
    elif i == 'Slow':
        slowSearch()