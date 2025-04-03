total = 50
coins = [25, 10, 5]
inserted_amount = 0

while inserted_amount < total: # this continues until enough money
    pepsi = int(input("Insert coin (25, 10, or 5 cents): ")) 
    if pepsi in coins:
        inserted_amount += pepsi
        print(f"Total inserted: {inserted_amount} cents") # adds the money 
    else:
        print("Invalid coin. Please insert 25, 10, or 5 cents.")

if inserted_amount >= total:
    print("Enjoy your drink.")





