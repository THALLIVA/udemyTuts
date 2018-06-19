import collections
import csv

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
    printDataBase()



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

def main():
    print("*************************** WELCOME TO BANKING SYSTEM*********************")
    choice = 0
    while choice != 99:
        choice = int(input("Enter 1.Add Customer "
                           "2.Delete Customer "
                           "3.Add Amount "
                           "4.Tranfer Amount" ))

        if choice == 1:
            addCustomer()
        elif choice == 2:
            CustId = str(input("Enter the Customer Id to be Removed "))
            delCustomer(CustId)
        elif choice == 3:
            addAmount()
        elif choice == 4:
            TransferAmount()

        else:
            print("Enter a valid Choice or Enter 99 to break the loop ")


    w = csv.writer(open("output.csv", "w"))
    for key, val in data.items():
        w.writerow([key, val])


main()
