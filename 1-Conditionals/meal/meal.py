def main():
    meal = input("What's the time? ")
    hours = convert(meal)

    if 7 <= hours <= 8:
        print("Breakfast time!")
    elif 12 <= hours <= 13:
        print("Lunch time!")
    elif 18 <= hours <= 19:
        print("Dinner time!")

def convert(time):
    hours, minutes = map(int, time.split(":"))
    return hours + minutes / 60

if __name__ == "__main__":
    main()