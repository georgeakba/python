import math

age = int(input("How old are you?\n"))
decades = math.floor(age/10)
years = age % 10
print("You are " + str(decades) + " decades and " + str(years) + " years old")