a = int(input("enter the value of a"))
b = int(input("enter the value of b"))
c = int(input("enter the value of c"))

#if a > b and a > c:
#    print(a, " is the greatest")
#
#elif b > a and b > c:
#    print(b, "is the greatest")
#
#else:
#    print(c, "is the greatest")

greater = max(a,b,c)
print(greater ,"is the greatest")