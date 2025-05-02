import getpass

users = {
    "admin": "admin123",
    "lucas": "lucas123",
    "marcia": "marcia123",
    "andrew": "andrew123"
}

while True:
    username = input("Enter your username, or enter 'q' to quit: ")
    if username == 'q':
        break
    password = getpass.getpass(prompt="Enter your password, or enter 'q' to quit: ", stream=None) 

    if username in users:
        if users[username] == password:
            print("login successful")
            break
        else:
            print("Login or password incorrect, please try again or press 'q' to quit")
    else:
        print("Login or password incorrect, please try again or press 'q' to quit")
