#ordered by when they joined the union
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(states_of_america)
#inside of the brackets is the index
# print(states_of_america[2])
#counts from zero, one explanation is how offset from the beginning it is
#negative numbers count from the end
# print(states_of_america[-1])

#can change items in list by setting index to variable
# states_of_america[1] = "Pencilvania"
# print(states_of_america[1])

# .append adds to end of list
# states_of_america.append("PedroLand")
# .extend([])
# states_of_america.extend(["PedroLand2", "PedroLand3"])

# print(lens(states_of_america))
# print(states_of_america[50]) # IndexError, list index out of range

num_of_states = len(states_of_america)
#counts 50 items, but index goes to 49, same IndexError
# print(states_of_america[num_of_states])

# print(states_of_america[num_of_states - 1])

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

#split the lists? manually would be-
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

#nested lists-
#LIST IN A LIST
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])
