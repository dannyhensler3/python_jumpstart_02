import random

print('--------------------------------')
print('    GUESS THAT NUMBER GAME')
print('--------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1

name = input('Player what is your name? ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)
    if guess < the_number:
        print(str.format('Sorry {} guess of {} is too LOW', name, guess))
    elif guess > the_number:
        print(str.format('Sorry {} guess of {} is too HIGH', name, guess))
    else:
        print(str.format('Excellent work {}, you won! The number was {}!', name, guess))

print('Done')
