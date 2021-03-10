print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
#adding ticket price into original ticket code
#has to be nested in same if block

#creating variable to add photo price to ticket
bill = 0
if height >= 120:
  print("You can ride the rollercoaster!") 
  age= int(input("What is your age? "))
  if age < 12:
    bill = 5 #adding variable with price to add ticket
    print("Child tickets are $5.")
  elif age <=18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  #adding photo option with input
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3  #Add $3 to bill
  #don't have to write else statement because it doesn't change
  print(f"Your final bill is ${bill}.")

else:
  print("Sorry, you don't meet the height requirement for this ride.")
