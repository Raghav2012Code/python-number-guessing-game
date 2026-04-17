import random



while True:
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between one and one hundred.")

    rand_number = random.randint(1, 100)   # generate FIRST
    attempts = 0
    
    while True:
        usr_guess = int(input("Guess a number between 1 and 100: "))
        attempts = attempts + 1 

        if usr_guess == rand_number:
            print("You have successfully guessed the right number!")
            print(f"It took you {attempts} to guess the number!")
            print("Good Job!!")
            break
        elif usr_guess > rand_number:
            print("Too High!")
            print("Guess Lower.")
        else:
            print("Too Low!")
            print("Guess Higher.")

    play_again = input("Do you want to play again (y/n): ")
    if play_again != "y":
        break