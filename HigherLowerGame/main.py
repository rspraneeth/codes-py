from art import logo, vs
from game_data import data
from random import choice
print(logo)

a_person = choice(data)
scr = 0

# check_b_equals_a(a, b)
def game(a, score):
    b = a
    while b == a:
        b = choice(data)
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
    opt = input("Who has more followers A/B: ").lower()
    if opt == 'a':
        if a['follower_count'] >= b['follower_count']:
            score += 1
            a = b
            print(f"You're right! Current score: {score}")
            game(a, score)
        else:
            print(f"Sorry, that's wrong! Final score: {score} ")
    elif opt == 'b':
        if a['follower_count'] <= b['follower_count']:
            score += 1
            a = b
            print(f"You're right! Current score: {score}")
            game(a, score)
        else:
            print(f"Sorry, that's wrong! Final score: {score} ")

game(a_person, scr)
