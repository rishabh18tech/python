import math

a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter b"))

s=(a+b+c)/2
A=math.floor(math.sqrt(s*(s-a)*(s-b)*(s-c)))



print("area of triangle is",A)