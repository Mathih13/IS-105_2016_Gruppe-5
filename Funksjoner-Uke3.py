
import math

def multiply():
    print "Multiplication"
    x = input('Enter first number: ')
    y = input('Enter second number: ')
    sum = int(x) * int(y)
    print sum
    return


def pluss():   
    x = input('Enter first number: ')
    y = input('Enter second number: ')
    sum = int(x) + int(y)
    print sum
    return


def subtract(): 
    print "subtract"
    x = input('Enter first number: ')
    y = input('Enter second number: ')
    sum = int(x) - int(y)
    print sum
    return

<<<<<<< HEAD
def squareroot(): 
    print "squareroot"
    x = input('Enter number: ')
    sum = math.sqrt(x)
    print sum
    return

def divide():
=======
<<<<<<< HEAD
def divide():   
=======

def divide():
>>>>>>> origin/develop
>>>>>>> 5cb5994778537593a4458db745c78eb56ec483fe
    print "divide"
    x = input('Enter first number: ')
    y = input('Enter second number: ')
    sum = int(x) / int(y)
    print sum
    return

<<<<<<< HEAD
divide()
=======
def plus - 2 ():
    print "plus - 2"
    x = input ('Enter first number')
    y = input ('Enter second number')
    z = 2
    print sum (int x + int y - int z)
    return

>>>>>>> origin/develop



calc = raw_input('What operator do you want to use? ')

if calc == 'multiplication':
    multiply()
elif calc == 'subtraction':
    subtract()
elif calc == 'addition':
        pluss()  
elif calc == 'divide':
    divide()
elif calc == 'squareroot':
    squareroot()
    


