def main():
    while True:
        try:
            # Get input from the user
            x, y = input("Enter fuel (must be something like 0/4): ").split("/")
            x = int(x)
            y = int(y)

            # Checks if the denominator is zero
            if y == 0:
                raise ZeroDivisionError("The denominator cannot be zero")

            # Convert the fraction to a decimal
            percentage = (x / y) * 100

            # Print the result
            if percentage < 1.0:
                print("e")
            elif percentage > 99.0:
                print("f")
            else:
                print(f"Fuel level is {percentage:.1f}%")
            break  
        except ValueError:
            print("another input please: ")
if __name__ == "__main__":
    main()