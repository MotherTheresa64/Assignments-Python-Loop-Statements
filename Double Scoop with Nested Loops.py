# Task 1: Your Mood Tracker

import random

emotions_list = ["Happy" , "Sad" , "Energetic" , "Calm"]
time_of_day = ["Morning" , "Afternoon" , "Night"]
week_days = ["Sunday" , "Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday"]
# Len gives a number of 7 and then range sets it to have an endpoint of 6 (0,6)
# Then the for loop will iterate through each available day of the week unil it caps
for x in range(len(week_days)):
    for y in range(len(time_of_day)):
        mood = random.choice(emotions_list)
        print("On " + week_days[x] + " " + time_of_day[y] + " you were feeling " + mood)

