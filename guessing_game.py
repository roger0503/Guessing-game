
import random

num = random.randrange(10)
Guesses = 5


for i in range(1, Guesses+1):
    guess = int(input("Enter your guess:"))

    if(guess == num):
        print("Your guess is correct!")
        break
    elif(guess > num and i < Guesses):
        print("You are close, keep trying lower")
    elif(guess < num and i < Guesses):
        print("You are close, keep trying hgher")

    if(i == Guesses-1):
        print("This is your last chance")
    elif(i == Guesses and guess != num):
        print("You Lost!")
        print("Correct answer was", num)