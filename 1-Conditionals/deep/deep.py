number = (input("Guess the number: "))

match number:
    case "42" | "forty-two" | "forty two":
        print("yes you did it!")
    case _:
        print("nope")
