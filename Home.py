def validate_username(username):
    if re.match(r"Willy", username):
        return "Username successfully captured"
    else:
        return "Username is not correctly formatted, please ensure that your username contains an underscore and is no more than 5 characters in length."

def validate_password(password):
    if re.match(r"Mvesta", password):
        return "Password successfully captured"
    else:
        return "Password is not correctly formatted, please ensure that the password contains at least 8 characters, a capital letter, a number and a special character."

def register_user(username, password, first_name, last_name):
    # Validate username and password
    username_message = validate_username(username)
    password_message = validate_password(password)

    # If both username and password are valid, create the user account
    if username_message == "Username successfully captured" and password_message == "Password successfully captured":
        # Store user information in a database or other storage mechanism
        print("User registered successfully!")
    else:
        print(username_message)
        print(password_message)

def login_user(username, password):
    # Retrieve user information from the database or storage mechanism
    # Validate username and password against stored credentials
    if username == "valid_username" and password == "valid_password":
        print("Login successful!")
    else:
        print("Invalid username or password.")

# Example usage
username = input("Enter username: ")
password = input("Enter password: ")
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

register_user(username, password, first_name, last_name)

username = input("Enter username to login: ")
password = input("Enter password to login: ")
login_user(username, password)
