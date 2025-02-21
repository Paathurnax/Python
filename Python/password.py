def log_in_machine(username, password):
    '''prompts the user to login and gives them 4 tries before locking them out'''
    attempts = 1
    while attempts < 5:
        if [username, password] == domain_accept[0]:
            print("good to see you!")
            break
        
        elif [username, password] == domain_accept[1]:
            print("there are 10 types of people in this world...")
            break
        
        elif [username, password] == domain_accept[2]:
            print("you're not funny")
            break
        
        elif [username, password] in domain_accept:
            print("welcome!")
            break
        
        else:
            print("try again")
            username = input("what is the username? ")
            password = input("what is the password? ")
            attempts = attempts + 1
            
    if attempts == 5:
        print("get outta here!")


def login_or_create(login_type):
    '''asks the user if they would like to login or create a new account'''
    if login_type == "login":
        log_in_machine(input("what is the username? "), input("what is the password? "))
        
    elif login_type == "create new":
        new_user = input("what is the new username? ")
        new_pass = input("what is the new password? ")
        
        domain_accept.append([new_user, new_pass])
        log_in_machine(input("what is the username? "), input("what is the password? "))
    
    else:
        print("try again")

#creating the login list
domain_accept = [["gracy", "compsci"], ["eason", "binary"], ["ligma", "balls"]]

#calling the function
login_or_create(input("would you like to login or create a new account? "))