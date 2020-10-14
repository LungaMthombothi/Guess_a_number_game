from random import *
from time import *

try:
    secretNumber = randint(1, 7)
    print('The Computer is thinking of a number between 1 and 7...')
    sleep(1.5)
    print('...')
    sleep(1.5)

    # This will ask for user input 7 times
    for guessTaken in range(1, 8):
        print('...Please take a guess which number the Computer has chosen...')
        sleep(1.5)
        guess = int(input('...Please enter your choice now...'))
        sleep(1)

        if guess < secretNumber:
            print('You"ve guessed a lower amount to what the Computer has chosen...')
    
        elif guess > secretNumber:
            print('You"ve guessed a higher amount to what the Computer has chosen...')
        else:
            break

    if guess == secretNumber:
        print('Bazinga!!! You guessed the "Secret Nnumber" in ' +  str(guessTaken) + ' guesses!')
    else:
        print('Nope! The number I chose hilena...' + str(secretNumber))
except ValueError:
        print('Please enter a numeric value...')

