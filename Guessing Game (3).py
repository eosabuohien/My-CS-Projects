#E
#11/12/2024
#Initialize
import random
#Functions
def guess_the_number():
    print("Welcome to the Guessing Game")
    print("Guess the secret number to win the game")
    print("If you guess the wrong number. You lose:<")
    print("If you guess the correct number. You have won the game:>")
#Beginning of the game, try 1
    guess = int(input("Enter Guess of the number"))#integer
    secret= random.randint(0,10)#integer
    if guess== secret:
        print("Congratulations, you have guessed the secret number")
    else:
        print("Incorrect, the number you have guessed is not the secret number." "The secret number was"+ " "+ str(secret))
    if secret<=guess:
        print("The number you have guessed is too high")
    else:
        print("The number you have guessed is too low")
    print("If you guessed the wrong number you can try again 2 more times")
#Second Try at the Game
    guess = int(input("Enter Guess of the number"))#integer
    secret= random.randint(0,10)#integer
    if guess==secret:
        print("Congratualations, you have beat the game on your second try")
    else:
        print("Incorrect, the number you have guessed is wrong again:<." "The secret number was" +" "+ str(secret))
    if secret<= guess:
        print("The number you have guessed is too high")
    else:
        print("The number you have guessed is too low")
    print("You have 1 more try to guess the right number")
#Last try of the Game
    guess = int(input("Enter Guess of the number"))#integer
    secret= random.randint(0,10)#integer
    if guess==secret:
        print("Congratualations, at last you have guessed the right number")
    else:
        print("Whomp, whomp. You have officially lost the game." "The secret number was" + " "+ str(secret))
    if secret<= guess:
        print("The number you have guessed is again too high")
    else:
        print("The number you have guessed is too low")
#Main
guess_the_number()
