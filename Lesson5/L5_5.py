account_Dict = {"admin": "admin", "account1": "qwerty1", "account2": "qwerty2", "account3": "qwerty3", "account4": "qwerty4", "account5": "qwerty5", "account6": "qwerty6", "account7": "qwerty7", "account8": "qwerty8", "account9": "qwerty9"}

#While loop for checking purposes
while(True):
    username = input("Username: ")
    password = input("Password: ")
    
    if username in account_Dict.keys():
        if password == account_Dict[username]:
            print("Logged in to the system.")
            break
        else:
            print("Password is invalid.")
    else:
        print("Not a valid user in the system.")