#Task 1: Your Mood Today

import random

emotions_list = ["Happy" , "Sad" , "Energetic" , "Calm"]

week_days = ["Sunday" , "Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday"]
# Len gives a number of 7 and then range sets it to have an endpoint of 6 (0,6)
# Then the for loop will iterate through each available day of the week unil it caps
for i in range(len(week_days)):
    mood = random.choice(emotions_list)
    print("On " + week_days[i] + " you were feeling " + mood)