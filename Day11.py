print("Second Calculator In a Year")
print(" ")
sec = int(input("How many seconds are there in a minute: "))
min = int(input("How many minutes are there in a hour: "))
hour = int(input("How many hours are there in a day: "))
day = int(input("How many days are there in a year: "))
day1 = int(input("How many days are there in a leap year: "))

secondsInAYear = day*hour*min*sec
secondsInALeapYear = day1*hour*min*sec
print(" ")
print("There are ",secondsInAYear," seconds in a year,")
print("and in a leap year there are ",secondsInAYear,)
    