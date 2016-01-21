calc = input('What operator do you want to use? ')

if calc == 'multiplication':
    multiply()
elif calc == 'subtraction':
    subtract()

def multiply():
    print "Multiplication"
    x = input('Enter first number: ')
    y = input('Enter second number: ')
    sum = int(x) * int(y)
    print sum
    return

