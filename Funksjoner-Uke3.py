
import math

def multiply():
    print "Multiplication"
    x = input('Enter first number: ')
    y = input('Enter second number: ')
    sum = int(x) * int(y)
    print sum
    return


def pluss():
    print "addition"
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


def squareroot(): 
    print "squareroot"
    x = input('Enter number: ')
    sum = math.sqrt(x)
    print sum
    return


def divide():
    print "divide"
    x = input('Enter first number: ')
    y = input('Enter second number: ')
    sum = int(x) / int(y)
    print sum
    return

def plusminus2():
    print "plus - 2"
    x = input ('Enter first number: ')
    y = input ('Enter second number: ')
    z = 2
    sum = (int(x) + int(y)) - int(z)
    print sum
    return



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
elif calc == 'plusminus2':
    plusminus2()
    


