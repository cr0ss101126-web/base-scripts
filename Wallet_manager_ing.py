Wallet = {"start_budget": 0,
               "total": 0
               }
buy_history = []

budget = float(input("How much you want to spend today? "))
budget
print(f"Perfect, add {budget} euro to the budget")
Wallet['start_budget'] = budget

name = input("What you buy? ")
price = float(input("How many did it cost? "))

def add(buy_history, name, price):
    new_product = {"name": name,
                   "price": price
                     }
    buy_history.append(new_product)

add(buy_history, name, price)

print(f"ok, this is your spending history: ")
for product in buy_history:
    print(f"Product: {product['name']}, Price: {product['price']}")

choose = " "

while choose != "exit":
    print("What you want to do now? (view budget / modify budget / add product / view spending history / exit)")
    choose = input("Choose ")
    if choose == "view budget":
        nbdgt = budget - price
        print(f"Your daily budget is of {nbdgt} euro")

    elif choose == "modify budget":
        modify_bdgt = float(input("How much do you want to add to the budget? "))
        nbdgt = budget - price
        Wallet['start_budget'] = modify_bdgt + nbdgt
        print(f"Now your budget is of {Wallet['start_budget']} euro")

    elif choose == "add product":
        new_name = input("What you buy? ")
        new_price = float(input("How much did it cost? "))
        add(buy_history, new_name, new_price)
        print("Product add successful!")

    elif choose == "view spending history":
        print(f"This is your spending history: ")
        for product in buy_history:
            print(f"Product: {product['name']}, Price: {product['price']}.")

    else:
        break

