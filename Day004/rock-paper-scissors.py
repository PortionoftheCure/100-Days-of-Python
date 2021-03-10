import random

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

r_p_s = [rock, paper, scissors]
#didn't import module, error
# import random, moved to top, learning style guides

# player = input("0 for rock, 1 for paper, 2 for scissors. ")
# print(r_p_s[player])
# type error, convert to int
print("Rock, paper, scissors against a randomized computer program.")
# print(player)
player = int(input("Type 0 for rock, 1 for paper, 2 for scissors. "))
print(r_p_s[player])

#rock(0) > scissors(2)
#scissors(2) > paper(1)

AI = random.randint(0, 2)
print("AI picks:")
print(r_p_s[AI])

if player >=3:
  print("Invalid input, you automatically.")
  
if player == 0 and A1 == 2:
  print("You win!")

elif AI == 0 and player == 2:
  print("You lose!")
elif player == 1 and AI == 0:
  print("You win!")
elif AI == 1 and player == 0:
  print("You lose!")
elif player == 2 and AI == 1:
  print("You win!")
elif AI == 2 and player == 1:
  print("You lose!")
elif AI == player:
  print("It is a tie!")
