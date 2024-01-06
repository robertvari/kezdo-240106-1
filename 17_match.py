status = 600

match status:
    case 200:
        print("OK")
    case 300:
        print("Multiple Choices")
    case 400:
        print("Bad Request")
    case 500:
        print("Internal Server Error")
    case _:
        print("This status is not handled")