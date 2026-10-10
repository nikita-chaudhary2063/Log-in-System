users = {}

def register(username, password):
    if username in users:
        print("Username already exists!")
    else:
        users[username] = password
        print(f"User '{username}' registered successfully!")

def login(username, password):
    if username in users and users[username] == password:
        print(f"✅ Login successful! Welcome, {username}.")
    else:
        print("❌ Invalid username or password.")

print("Simple Login System")
print("Options: register, login, quit")

while True:
    choice = input("Enter option: ")

    if choice == "register":
        username = input("Enter new username: ")
        password = input("Enter new password: ")
        register(username, password)
    elif choice == "login":
        username = input("Enter username: ")
        password = input("Enter password: ")
        login(username, password)
    elif choice == "quit":
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid option")
