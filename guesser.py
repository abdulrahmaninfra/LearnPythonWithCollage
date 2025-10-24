# This little game built by simple code of python and theory there a secret number from 1 to 10 and you should to guess this number right. that it...
import random

secret= random.randint(1,10)

guess = 0

while guess != secret:
    guess= int(input("Select a Number Between 1,10: "))

    if guess == secret:
        print("Winner!! :D ")

    elif guess == secret - 1:
        print("Too Close!!! :| ")

    elif guess == secret + 1:
        print("Too Close!!! :| ")

    elif guess == secret - 2:
        print("Close! :( ")

    elif guess == secret + 2:
        print("Close! :( ")

    elif guess > secret:
        print("Loser :( , Lower")

    elif guess < secret:
        print("Loser :( , Higher")

print("Secret Number Was", secret)

