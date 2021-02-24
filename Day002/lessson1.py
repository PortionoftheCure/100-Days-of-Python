# print(int(8 / 3))
# int chops off decimal

# to round, use round()
# print(round(8 / 3)) 
# print(round(8 / 3, 2)) #rounds to decimal places after comma
# print(round(2.6666666, 2))

# // is floor division, outputs int instead of float
# print(8 // 3)
# # print(type(8 // 3))

# #variable number manipulation
# result = 4 / 2
# result /= 2  #
# print(result) #divides, so is a float

# score = 0

# User scores a point
# score = score + 1, operation before = applies operation
# += -+ *= /=
# score += 1 
# print(score)
# print("your score is " + score) # error, can't concatonate str and int
#convert score to str
# print("your score is " + str(score) )

score = 0 #int
height = 1.8 #float
isWinning = True #boolean

#f-string
{} to place variables
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
