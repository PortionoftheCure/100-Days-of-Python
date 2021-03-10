# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#my solution
name1 = name1.lower()
name2 = name2.lower()
# count outputs integer
n1_true = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
n2_true = name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")
true = (str(n1_true + n2_true))

n1_love = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")
n2_love = name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")
love = (str(n1_love + n2_love))

score = (int(true + love))

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")  

#instructor solution

# combined_string = name1 + name2
# lower_case_string = combined_string.lower()

# t = lower_case_string.count("t")
# r = lower_case_string.count("r")
# u = lower_case_string.count("u")
# e = lower_case_string.count("e")

# true = t + r + u + e

# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# e = lower_case_string.count("e")

# love = l + o + v + e

# #going back a step, wrapping string concatenation into an int
# love_score = int(str(true) + str(love)) 
# #string can't be used in int comparison
# # int_score - int(love_score)
# if (love_score < 10) or (love_score > 90):
#   print(f"Your love socre is {love_score}, you go together like coke and mentos.")
# elif (love_score >= 40) and (love_score <= 50):
#   print(f"Your score is {love_score}, you are alright together.")
# else:
#   print(f"Your score is {love_score}.")
