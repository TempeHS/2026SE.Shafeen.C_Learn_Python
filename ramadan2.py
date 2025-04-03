import time 

print("Assalamu Alaikum!")
time.sleep(2)
print("Today is Ramadan.")
time.sleep(2)
print("What would you like to eat for Suhoor?")

haram_list = ["pork", "alcohol", "drugs", "gambling", "theft", "cheating", "lying", "backbiting", "gossiping", "adultery", "stealing", "dogs", "rats", "snakes", "pig", "ham", "wine", "spider", "spiders", "beer", "liquor", "vodka", "whiskey", "rum", "gin", "brandy", "tequila", "cognac", "sake", "soju", "baijiu", "baiju", "baijou"]
while True:
    suhoor_choice = input("Enter your choice: ")
    if any(haram in suhoor_choice.lower() for haram in haram_list):
        print("That is haram. Please choose something else.")
    elif "date" in suhoor_choice.lower():
        print("so halal mode")
        break
    else:
        print(f"Great choice! {suhoor_choice} will help you stay energized throughout the day.")
        break
time.sleep(2)

print("What would you like to drink for suhoor")

while True:
    drink_choice = input("Enter your choice: ")
    if any(haram in drink_choice.lower() for haram in haram_list):
        print("That is haram. Please choose something else.")
    else:
        print(f"Great choice! {drink_choice} will keep you hydrated for the day.")
        break
time.sleep(2)

print("What would you like to eat for Iftar?")

while True:
    iftar_choice = input("Enter your choice: ")
    if any(haram in iftar_choice.lower() for haram in haram_list):
        print("That is haram. Please choose something else.")
    else:
        print(f"Delicious! {iftar_choice} will be a wonderful way to break your fast.")
        break

time.sleep(2)
print("Well, sleep well for the next day of fasting.")
time.sleep(2)
print("Inshallah, May Allah accept your fasts and prayers. Ramadan Mubarak!")
time.sleep(2)

print("Welcome to Eid!")
time.sleep(2)
eid = input("What would you like to eat for Eid? ")
while True:
    if any(haram in eid.lower() for haram in haram_list):
        print("That is haram. Please choose something else.")
    else:
        print(f"Delicious! {eid} will be a wonderful way to break your fast.")
        break
time.sleep(2)


