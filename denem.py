year = int(input("Enter year to be checked:"))
print(year % 4 == 0 and year % 100 != 0 or year % 400 == 0 and year % 4000 != 0)
