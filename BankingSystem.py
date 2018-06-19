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
    print("Added a new Customer "+ Name)
    printDataBase()



def delCustomer(id):
    data.pop(id)



def addAmount():
    data1 = data.copy()
    amount=int(input("Add amount to be added"))
    CustId= str(input("Enter the Account to be added"))
    data1[CustId]["Amount"] = data[CustId]["Amount"] + amount
    data.update(data1)
    printDataBase()


def TransferAmount():
    data1 =  data.copy()
    amount = int(input("Add amount Transfered"))
    CustId1 = str(input("Enter the Account to be deducted"))
    CustId2 = str(input("Enter the Account to be added"))

    data1[CustId1]["Amount"] = data[CustId1]["Amount"] - amount
    data1[CustId2]["Amount"] = data[CustId2]["Amount"] + amount
    printDataBase()

