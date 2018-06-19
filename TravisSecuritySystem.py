data = {
    1:{"id":1,"Name":"Darsh","Age":22,"Score":86},
    2:{"id":2,"Name":"Parth","Age":21,"Score":65},
    3:{"id":3,"Name":"Sanjil","Age":22,"Score":75},
    4:{"id":4,"Name":"Raj","Age":43,"Score":33},
    5:{"id":5,"Name":"Viral","Age":23,"Score":75},
}

SearchId = int(input("Enter Our ID:"))
if SearchId in data:
    print("Hello Our ID is Present in Database")
    choice = input(print("Do u want to Remove it?(y/n)")).lower()

    if choice == "y":
        print("Your Name is been removed")
        data.pop(SearchId,None)
        print(data)

    else:
        print("Your Data is safe with us")

else :
    print("Do u want to add a new Entry:?")
    choice = input(print("Do u want to Add it?(y/n)")).lower()

    if choice == "y":
        print("Pls enter Our Details")
        newId = int(input("Pls Enter your Id"))
        newName = input("Pls Enter your Name")
        newAge = int(input("Pls Enter your Age"))
        newGrade = int(input("Pls enter your grade"))

        newdata = {
            newId: {"id": newId, "Name": newName, "Age": newAge, "Score": newGrade}

        }
        data.update(newdata)


        print(data)

    else :
        print("Not added of the database")



