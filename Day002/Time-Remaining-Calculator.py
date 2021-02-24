# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# sloppy draft
age = (int(age)) 
years = 90 - age
months = 1080
months_left = months - (age * 12)
weeks = (round(4692.86)) 
weeks_left = weeks - (age * 52)
days = 32850
days_left = days - (age * 365)
print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left.")

#instructor's solution

# age_as_int= int(age)

# years_remaining = 90 - age_as_int
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12

# message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
# print(message)
