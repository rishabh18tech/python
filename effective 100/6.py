a = int(input("enter the value of a"))
b = int(input("enter the value of b"))

#value swapped using third variable
# c = a
# a = b
# b = c

#value swapped without using third variable
a = a + b  # a=5
b = a - b  # b=3
a = a - b  # a=2


print("the swapped value of a is", a, "the swapped value of b is", b)
