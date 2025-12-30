name = str(input("what is your name"))
age = int(input("enter your age"))

if age >= 18:
    print("hello ", name, "you are an valid voter")

else:
    print(
        "hello",
        name,
        "you are not an valid voter you will be eligible after ",
        18 - age,
    )
