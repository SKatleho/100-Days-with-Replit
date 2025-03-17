print("\033[33mWhole Positivity Machine\033[0m")
print(" ")
print(" ")
name = input("Who are you?")
print(" ")
goal = input("What do you want to achieve?")
print(" ")
feeling = input("On a scale of 1 to 10, how do you feel today (1:😥,10:🥳)")
print(" ")
print(" ")
if feeling == "1":
    feeling1="you've survived tough days before, and you can do it again,"
elif feeling == "2":    
    feeling1="I believe in you, and I know you can turn this day around,"
elif feeling == "3":    
    feeling1="take a deep breath, you're stronger than you think"
elif feeling == "4":    
    feeling1="you're doing better than you think, keep pushing forward"
elif feeling == "5":    
    feeling1="neutral is okay! Let's work together to shift the scale"
elif feeling == "6":   
    feeling1="you're on the verge of a breakthrough, keep going"
elif feeling == "7":    
    feeling1 ="your hard work is paying off, keep shining"
elif feeling == "8":    
    feeling1="you're crushing it! Keep that momentum going"
elif feeling == "9":    
    feeling1="you're unstoppable! Keep pushing yourself to new heights"
elif feeling == "10":    
    feeling1="you're amazing! Celebrate your wins and keep soaring"
print("Hey ",name,", ",feeling1,"! Today you're going to ",goal," and in the most amazing way, ")
print("simply by being you - YOU ROCK!")