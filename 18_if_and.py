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
    if email != input_email:
        print("Email is not correct.")
    
    if password != input_password:
        print("Password is not correct.")
    
    print("Try again.")