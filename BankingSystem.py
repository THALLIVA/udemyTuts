data = {
    "1": {"id": 1, "Name": "Darsh", "Age": 22, "Account": "Saving", "AccountNo": 1000, "Amount": 500}
}


def addCustomer(id, Name, Age, Account, AccountNo, Amount):
    newCustomer = {
        1: {"id": id, "Name": Name, "Age": Age, "Account": Account, "AccountNo": AccountNo, "Amount": Amount}
    }
    data.update(newCustomer)



def delCustomer(id):
    data.pop(id)


