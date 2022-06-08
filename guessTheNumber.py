import random

def guess_num():
    return int(input("Make a guess: "))

def chance_msg(chance):
    if chance == 0:
        print("You've run out of guesses! You loose")
    elif chance == 1:
        print(f"You have {chance} chance to guess the number")
    else:
        print(f"You have {chance} chances to guess the number")

def game():
    print("Welcome to number guessing game.\nI'm thinking of a number between 1 and 100")
    num = random.randint(1, 100)
    diff = input("Choose a difficulty type! Type easy(e) or hard(h) e/h: ").lower()

    if diff == 'e':
        chances = 10
    else:
        chances = 5

    print(f"You have {chances} chances to guess the number")
    num_guessed = False
    while chances != 0 and not num_guessed:
        guess = guess_num()
        if guess == num:
            print(f"You got it! The answer is {num}")
            num_guessed = True
        elif guess > num:
            print("Too high")
            chances -= 1
            chance_msg(chances)

        elif guess < num:
            print("Too low")
            chances -= 1
            chance_msg(chances)

game()









