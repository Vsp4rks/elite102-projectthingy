name = input("Type in your name here: ")

def displaymenu():
    print("\n Welcome to the banking app, " + name + "!")
    print()
    print("1. Check your balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Create Account")
    print("5. Modify Account")
    print("6. Delete Account")

def selectionmenu():
    in_use = True
    selection = int(input("Choose one of the options listed above: "))