from backbone import createList, readList 
import time

#Config
texttoread = 'text.txt'
first = 1
to = 1000000


def number():
    p = createList(first, to)
    return p

def words():
    r = readList(texttoread)
    return r


def search_fast(haystack, needle): 
    for item in haystack:
        if item == needle:
            return True
    return False
    
    
def search_slow(haystack, needle): 
    return_value = False
    for item in haystack:
        if item == needle: 
            return_value = True
    return return_value




def pront():
    print "Completion Time:"
    print("--- %s seconds ---" % (time.time() - start_time))
    

def start(l, k):
    print search_fast(l, k)

l = number()
i = raw_input("Ord man skal finne: ")

start_time = time.time()
start(l, i)
pront()