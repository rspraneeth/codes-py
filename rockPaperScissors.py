rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if choice == 0:
  print("You choose Rock \n" +rock)
elif choice == 1:
  print("You choose Paper \n" +paper)
else:
  print("You choose scissors \n" +scissors)

import random
comp_choice = random.randint(0, 2)
if comp_choice == 0:
  print("Computer choose Rock \n" +rock)
elif comp_choice == 1:
  print("Computer choose Paper \n" +paper)
else:
  print("Computer choose scissors \n" +scissors)

output = [["Draw", "Computer wins", "You win"],["You win", "Draw", "Computer wins"], ["Computer wins", "You win", "Draw"]]
print(output[choice][comp_choice])