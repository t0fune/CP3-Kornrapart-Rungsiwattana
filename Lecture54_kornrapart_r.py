
def login():
    print("Log-in")
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
        print("Login Complete")
    else:
        return False
        print("Login Failed")

def vatCalculator(totalPrice):
    print("VAT Calculator")
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    print("---Price Calculator---")
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

def Exit():
    print("Thank you for using this program")

def menuSelect():
    print("---Menu Selection---")
    print("1. Login")
    print("2. Vat Calculator")
    print("3. Price Calculator")
    print("4. Exit")
    userSelected = int(input("Select your menu :"))

    if userSelected == 1:
        login()
    elif userSelected == 2:
        totalPrice = int(input("Enter the total price :"))
        print(vatCalculator(totalPrice))
    elif userSelected == 3:
        print(priceCalculator())
    elif userSelected == 4:
        Exit()


print(menuSelect())