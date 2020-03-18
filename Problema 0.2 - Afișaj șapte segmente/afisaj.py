#from __future__ import print_function
import sys

numbers = []

while True:
    line = sys.stdin.readline()
    if not line: break
    numbers.append(line.rstrip())   #here reading input
 # End here

for number in numbers:
    currentNumber = number
    if currentNumber == '0,1,1,0,0,0,0,0':
        print("1", sep='', end='')
    elif currentNumber == '0,1,1,0,0,0,0,1':
        print("1.", sep='', end='')
    elif currentNumber == '1,1,0,1,1,0,1,0':
        print("2", sep='', end='')
    elif currentNumber == '1,1,0,1,1,0,1,1':
        print("2.", sep='', end='')
    elif currentNumber == '1,1,1,1,0,0,1,0':
        print("3", sep='', end='')
    elif currentNumber == '1,1,1,1,0,0,1,1':
        print("3.", sep='', end='')
    elif currentNumber == '0,1,1,0,0,1,1,0':
        print("4", sep='', end='')
    elif currentNumber == '0,1,1,0,0,1,1,1':
        print("4.", sep='', end='')
    elif currentNumber == '1,0,1,1,0,1,1,0':
        print("5", sep='', end='')
    elif currentNumber == '1,0,1,1,0,1,1,1':
        print("5.", sep='', end='')
    elif currentNumber == '1,0,1,1,1,1,1,0':
        print("6", sep='', end='')
    elif currentNumber == '1,0,1,1,1,1,1,1':
        print("6.", sep='', end='')
    elif currentNumber == '1,1,1,0,0,0,0,0':
        print("7", sep='', end='')
    elif currentNumber == '1,1,1,0,0,0,0,1':
        print("7.", sep='', end='')
    elif currentNumber == '1,1,1,1,1,1,1,0':
        print("8", sep='', end='')
    elif currentNumber == '1,1,1,1,1,1,1,1':
        print("8.", sep='', end='')
    elif currentNumber == '1,1,1,1,0,1,1,0':
        print("9", sep='', end='')
    elif currentNumber == '1,1,1,1,0,1,1,1':
        print("9.", sep='', end='')
    elif currentNumber == '1,1,1,1,1,1,0,0':
        print("0", sep='', end='')
    elif currentNumber == '1,1,1,1,1,1,0,1':
        print("0.", sep='', end='')
    else:
        break
