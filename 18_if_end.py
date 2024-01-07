# stored in my database
email = "robert@gmail.com"
password = "testpas123"

# input form
input_email = input("Email:")
input_password = input("Password:")

#         True                       True
if email == input_email and password == input_password:
    print("Wellcome back!")
else:
    print("email or password is not correct. Try again.")