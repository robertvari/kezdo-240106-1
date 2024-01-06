phonebook = {
    #  root key
    "06201234567": {"name":"Csaba", "address":"Budapest", "email": "csaba@gmail.com"},
    "06202345678": {"name":"Kriszta", "address":"Debrecen", "email": "kriszta@gmail.com"},
    "06305427578": {"name":"Tamás", "address":"Pécs", "email": "tamas@gmail.com"},
}

# add new data to phonebook
phonebook["06204256543"] = {"name":"Balázs", "address":"Eger", "email": "balazs@gmail.com"}

# edit/replace data in phonebook
phonebook["06202345678"]["address"] = "Eger"

pass