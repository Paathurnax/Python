got_password_right = False

while got_password_right == False:
    password = input("What's the password? ")
    
    if password == "123456789":
        got_password_right = True
    else:
        print("try again! ")
        
        
print("Correct! ")
    