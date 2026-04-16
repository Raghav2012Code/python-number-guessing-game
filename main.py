import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between one and one hundred.")

rand_number = random.randint(1, 100)   # generate FIRST

usr_guess = int(input("Guess a number between 1 and 100: "))

if usr_guess == rand_number:
    print("You have successfully guessed the right number!")
    print("Good Job!!")
elif usr_guess > rand_number:
    print("Too High!")
    print("Guess Lower.")
else:
    print("Too Low!")
    print("Guess Higher.")