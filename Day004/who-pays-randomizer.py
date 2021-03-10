# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
# .split("x") indexes a list after each iteration of "x"
#Write your code below this line 👇

import random
#get total number of items in list
number_of_people = len(names)
#use that variable which is now an integer in randm.randit
#zero is list starting point so the range will be -1 of the total
#if this wasn't a randomization though then I am thinking you could nest [-1] with the variable to span the range
pick = random.randint(0, number_of_people - 1)
pays = names[pick]
print(pays + " is going to buy the meal today!")

#can use random.choice(list)
#shorter code but less understanding of list indexes and variables
# pays = random.choice(names)
# print(pays + " is going to buy the meal today!")
