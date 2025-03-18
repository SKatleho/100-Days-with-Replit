print("Generator Identifier")
print(" ")
print("++++++++++++++++++++")
print(" ")
year = int (input("Which year were you born: "))
if year >= 1883 and year <= 1900:
    message = "Lost Generation"
elif year >= 1901 and year <= 1927:
    message = "Greatest Generation"
elif year >= 1928 and year <= 1945:
    message = "Silent Generation"
elif year >= 1946 and year <= 1964:
    message = "Baby Boomers"
elif year >= 1965 and year <= 1980:
    message = "Generation X"
elif year >= 1981 and year <= 1996:
    message = "Millennials"
elif year >= 1997 and year <= 2012:
    message = "Generation Z"
else :
    message = "Generation Alpha"
print(" ")
print("Hah! ",message,"! Avocado toast and Starbuck much!")