Fruit = input("Add a fruit: ")

yummy_tummy = {
    "Apple": 130,
    "Banana": 110,
    "Orange": 80,
    "Strawberry": 50,
    "Grapes": 90,
    "Mango": 200,
    "Pineapple": 150,
    "Peach": 100,
    "Kiwi": 120,
    "Watermelon": 60,
}

if Fruit in yummy_tummy:
    print(yummy_tummy[Fruit])
else:
    print("fruit not yummy")

    

