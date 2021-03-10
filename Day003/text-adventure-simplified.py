# print("Welcome to Confusing Island.")
# print("Your mission is to survive.") 
# print("You awaken on the beach of a small island, early morning, with complete amnesia aside from your ability to make decision.")
# print("As you look around, you see a tiny dock, a bare beach, and open ocean. Behind you is the jungle, full of animal noises.")
# print("Answers are case sensitive.")
choice_1 = input("Type 'Y' or 'N'. \n")

#.lower() causes variables to be skipped and I don't know why.

if choice_1 == 'Y':
  choice_2 = input("Up or down? \n")
  if choice_2 == 'Up':
    choice_3 = input("Left, right, or straight? \n")
    if choice_3 == 'Left':
      print("Win!")
    elif choice_3 == 'right':
      print("Lose.")  
    elif choice_3 == 'straight':
      print("Lose.")  
  else:
    print("Lose.")
else:
  print("Lose.")
