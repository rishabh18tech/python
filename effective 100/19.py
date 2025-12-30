y = int(input("enter the year"))

if y % 400 == 0:
    print(y, "given year is leap year")
elif y % 100 == 0:
    print(y, "given leap year is not leap year ")
elif y % 4 == 0:
    print(y, "given year is a leap year")
else:
    print(y, "given year is not a leap year")
