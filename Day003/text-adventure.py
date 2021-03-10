print('''
*******************************************************************************
    _.------._
 _.-'          '-._
/                  \
'------------------'
| .--------------. |
| |      ||      | |
|[]      ||      | |
| |======||======| |
| |      ||      | |
| |      ||      | |
|[]======||======[ |
| |======||======| |
| |      ||      | |
| |      ||      | |
|[]======||======| |
| |      ||      | |
| '------''------' |
|__________________|
*******************************************************************************
''')
print("Welcome to Save the Future.")
print("Your mission is to heavily impact the future of humanity by interacting with Adolf Hitler.") 

first_choice = input('You stumble up a box that says Time Machine to the last moments of Hitler. Type "enter" to step into the machine. Type "leave" to walk way. \n').lower()


if first_choice == "enter":
  second_choice = input('You step into the Time Machine, arriving in the office of Hitler, alone,  in his last moments before losing the war. Type "hey" to initiate conversation or "stare" to remain silent. \n').lower()
  if second_choice == "hey":
    third_choice = input('Adolf is startled by your sudden appearance. He looks like he needs a hug. Type "hug" to hug the bad boi, type "scream" to succumb to the existential crisis, or "freeze" to do nothing. \n').lower()
    if third_choice == "hug":
      print("All he needed was a hug. You have saved the future of humanity. 6 million Jews are still dead, if you believe that.")
    elif third_choice == "scream":
      print("You begin to scream as a startled Adolf shoots you. You die and lose. Game Over.")
    elif third_choice == "freeze":
      print("You an Adolf stare at each other until he reaches under the desk and shoots you with a Luger. Game Over.")
    else:
      print("You can't make a decision, why did you even enter the box, Game Over.")
  else:
    print("You and Adolf stare at each other as reality fractures around you. Indecision collapsed reality due to your inability to sieze the day. Game Over.")    
else: 
  print("Humanity is doomed, you lose.")


#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
