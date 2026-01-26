account = {"name": "user",
           "age": 25,
           "city": "London"
}
choose = " "

while choose != "esci":
    choose = input("What you want to do? (modify / visual / exit)   ").lower()
    
    if choose == "modify":
        print(f"What you want to modify? name: {account['name']}, age: {account['age']}, city: {account['city']}")
        modif = input("choose   ")
        if modif == "name":
            mdf = input("now is   ")
            account['name'] = mdf
            print(f"ok, now your name is {account['name']}")
        elif modif == "city":
            mdf
            account['city'] = mdf
            print(f"ok, now your city is {account['city']}")
        else:
            csmd
            profilo['età'] = mdf
            print(f"ok, now your age is {account['age']}")
    elif choose == "exit":
        break
    else:
        print(f"your name is {account['name']}, your age is {account['age']}, your city is {account['city']}")


