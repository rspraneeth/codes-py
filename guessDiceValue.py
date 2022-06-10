from random import choice

print("Welcome to dice game. \n")

# dice game that takes first number and second number and asks user to guess if second number is
# higher/lower than first number, if the user choice is right then the game continues by swapping
# second number value to the first and first number is picked randomly from dice again and again
# asks for user input and the game continues on as long user is guessing right and score will be
# incremented everytime user guesses  right. If at anywhere user guesses wrong game will be stopped
# and users score is displayed.

dice_values = [1, 2, 3, 4, 5, 6]
f_num = choice(dice_values)
scr = 0

def game(first_num, score):
    dice_list = [1, 2, 3, 4, 5, 6]
    second_num = choice(dice_list)
    option = input(f"Guess if second num is higher or lower than first number {first_num}, H/L: ").lower()
    if option == 'h':
        if second_num >= first_num:
            score += 1
            print(f"2nd number {second_num} is higher than= 1st number {first_num}, score is {score}")
            first_num = second_num
            game(first_num, score)
        else:
            print(f"You lost your score is {score}, 2nd number {second_num} is lower than 1st number {first_num}")

    elif option == 'l':
        if second_num <= first_num:
            score += 1
            print(f"2nd number {second_num} is lower than= 1st number {first_num}, score is {score}")
            first_num = second_num
            game(first_num, score)
        else:
            print(f"You lost your score is {score}, 2nd number {second_num} is higher than 1st number {first_num}")

game(f_num, scr)
