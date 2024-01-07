# stored in my database
email = "robert@gmail.com"
password = "testpas123"
max_tries = 3

# input form
input_email = input("Email:")
input_password = input("Password:")

#         False                       False
while email != input_email or password != input_password:
    max_tries -= 1

    if max_tries == 0:
        print("Sorry Game over! :))))")
        exit()

    print(f"Email or password is incorrect. You have {max_tries} tries left.")
    
    input_email = input("Email:")
    input_password = input("Password:")

print("Wellcome back!")