status = 200


if status == 200:
    print("OK")
elif status == 300:
    print("Multiple Choices")
elif status == 400:
    print("Bad Request")
elif status == 500:
    print("Internal Server Error")