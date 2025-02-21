password_right = False
while password_right == False:
    password = input("What is the password? ")
    if password == "sask":
        print("what a great place!")
        password_right = True
    else:
        print("Try Again")