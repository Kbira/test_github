from random import randint
from sys import argv

minimum = int(argv[1])
maximum = int(argv[2])
nr_to_guess = randint(minimum, maximum)


def check_nr(x):
    if minimum > x or x > maximum:
        print('Input is not between the given range')
        play_game()
    elif nr_to_guess != x:
        print('Guess again')
        play_game()
    else:
        print('You guessed well, nice job!')


def play_game():
    while True:
        try:
            x = int(input(f'Enter a number between {minimum} and {maximum}.'))
        except ValueError:
            print('Please enter a number')
        else:
            check_nr(x)
            break


print('Lets play a game')
play_game()
