p = int(input("enter p"))
r = int(input("enter r"))
t = int(input("enter t"))
n = int(input("enter n"))

r=r/100

a = p * (1 + r / n) ** (n * t)
print("ci is ",a)