print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

#nested spacing is important, if and else on same line
#to include 120cm, >=
#comparison operators
# nested ifs, and then elif
if height >= 120:
  print("You can ride the rollercoaster!") #lives in if
  age= int(input("What is your age? "))
  if age < 12:
    print("Please pay $5.")
  elif age <=18:        #if over 12, check for under 18
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you don't meet the height requirement for this ride.") # lives in else

# = assigns, == is comparison operator
#nested, after first condition passes, check for another condition

# if condition:
#   if anoter condition:
#     do this
#   else:
#     do this
# else:
#   do this
