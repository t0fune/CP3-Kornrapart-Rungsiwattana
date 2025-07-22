print("---- Register ID ----")
Water = 10
Banana = 20
Coke = 15
Snack = 20
Username1 = input("Username :")
Password1 = input("Password :")
confirmPassword1 = input("ConfirmPassword :")

if Username1 == Username1 and Password1 == confirmPassword1 :
    if len(Password1) >= 6 and len(Username1) >= 6 :
        print("Register Complete :" + Username1)

        print("-----Login-------")

        if input("Log in Username :") == Username1 and input("Log in Password :") == Password1:
            print("----Welcome Korn Shop----")
            print("Product               Price")
            print("1.Water               10 THB")
            print("2.Banana              20 THB")
            print("3.Coke                15 THB")
            print("4.Snack               20 THB")

            Select = int(input("Enter your Product :"))
            Amount = int(input("Enter your Amount :"))
            print(" *************************")
            print("  -------RECEIPT--------")
            print(" *************************")
            if Select == 1 : print("Water =" , Water*Amount , "THB")
            elif Select == 2 : print("Banana =", Banana*Amount , "THB")
            elif Select == 3: print("Coke =", Coke * Amount, "THB")
            elif Select == 4: print("Snack =", Snack * Amount, "THB")

        else:
            print("Your ID or Password is Wrong , Try again")
    else :
        print("Your Username and Password must be more than 6 Character , try again")


else :
    print("Your Password is not the same , Try again")