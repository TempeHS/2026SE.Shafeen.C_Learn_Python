def main():
    x = get_int()
    print(f"Your number is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x?: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")

main()