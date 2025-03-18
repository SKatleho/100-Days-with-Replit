print("Tip Calculator")
print(" ")
Bill = float (input("How much did you spend : R"))
print(" ")
percInInt = int (input("What percentage do you want to tip: "))
print(" ")
percInDouble = percInInt/100
numberOfPeople = int (input("How many people are in your group: "))
print(" ")

Bill = ((Bill*percInDouble)+Bill)
myBill = Bill/numberOfPeople
myBill = round(myBill,2)
print("The bill is R",myBill)