for i in range(3):
    password = int(input("Enter Password: "))

    if i == 2:
        print("Access Denied")
        break

    if password == 1234:
        print("Access Granted")
        break
    else:
        print("Wrong Password")
        print("Try Again: ")
