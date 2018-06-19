import collections

data = {
    "1": {"id": 1, "Name": "Darsh", "Age": 22, "Account": "Saving", "AccountNo": 1000, "Amount": 500}
}

def printDataBase():
    for k,v in collections.OrderedDict(sorted(data.items())).items():
        print(k,v)



def addCustomer():
    id = int(input("Enter ID of the Customer"))
    Name = input("Enter Name of the Customer")
    Age = int(input("Enter Age"))
    Account = input("Enter Type of Account(Saving or Current)")
    AccountNo = int(input("Enter Accountno"))
    Amount = int(input("Enter Amount"))


    newCustomer = {
        str(id): {"id": id, "Name": Name, "Age": Age, "Account": Account, "AccountNo": AccountNo, "Amount": Amount}
    }
    data.update(newCustomer)
    printDataBase()



def delCustomer(id):
    data.pop(id)


addCustomer()

