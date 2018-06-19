email = input("Enter Email:").strip()


if "@" in email:

    username = email[:email.index("@")]
    domain = email[email.index("@"):]
    print("Username:  "+ username + "   Domain : "+ domain )
else:
    print("Enter a Valid Email")






