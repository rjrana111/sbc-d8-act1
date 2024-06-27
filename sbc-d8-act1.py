#file = open("storage.txt", "r")
#var = file.readlines()
#print(var[2])


#lines = [line.strip() for line in open ("Storage.txt")]
#for line in lines:
#    print(line)



#file = open("storage.txt", "r")
#print(file.readlines())



#file = open("storage.txt", "w")
#file.write("hello\n")
#file.write("summer\n")
#file.write("goodbye\n")
#file.close()


#write = open("storage.txt" , "w")
#print("Hello", file=write)
#print("Summer", file=write)
#print("Goodbye", file=write)
#write.close()



user = {}

def sign_up():
    with open("data2.txt", "a") as storage:
        username = input("Enter Username: ")
        if username in user:
            print(f"Username '{username}' is already in use.")
        else:
            password = input("Enter Password: ")
            user[username] = password
            print(f"Account for '{username}' has been created successfully.")
            print(f"Username:{username} Password:{user[username]}", file=storage)
            storage.close()

def sign_in():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username in user and user[username] == password:
        print(f"Login successful. Welcome, {username}!")
    else:
        print("Login Failed")

def update_pass():
    with open("data2.txt", "a") as storage:
        username = input("Enter Username: ")
        if username in user:
            old_pass = input("Enter Current Password: ")
            if user[username] == old_pass:
                new_pass = input("Enter New Password: ")
                user[username] = new_pass
                print(f"Username:{username} Password:{user[username]}", file=storage)
                print(f"Password for '{username}' has been updated.")
                storage.close()
            else:
                print("Incorrect current password.")
        else:
            print("User not found.")

while True:
    print('''Welcome
          1. Sign In
          2. Sign Up
          3. Update Password''')

    option = int(input("Select an option: "))

    if option == 1:
        sign_in()
    elif option == 2:
        sign_up()
    elif option == 3:
        update_pass()
    else:
        print("Invalid choice. Please select a proper option.")



