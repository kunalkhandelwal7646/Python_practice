# validate username 

# Input Username

username = input("Enter a Username - ")

if len(username) > 12:
    print("Username cannot be more than 12 characters!!")

elif not username.find(" ") == -1:
    print("Username cannot include spaces!!")

elif username.isdigit() == True:
    print("Username cannot contain digits")

else:
    print("Valid Username 👌")