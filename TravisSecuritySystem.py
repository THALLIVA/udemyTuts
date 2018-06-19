data = [
        ["Username","age"],
        ["Darsh",22],
        ["Raj",22],
        ["Parth",22]
        ]

name = input("Enter Our Name").strip().capitalize()

while True:
    name = input("Enter Our Name").strip().title()

    if name in data :
        print("Hello Our Name is Present in Database")
        choice = input(print("Do u want to Remove it?(y/n)"))

        if choice is "y" :
            print("Your Name is been removed")
            data - name



