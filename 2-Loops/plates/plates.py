def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s): 
    return all([
        starts_with_letters(s),
        max_leng(s),
        middle_digits(s),
    ])

def starts_with_letters(plate):
    return plate[:2].isalpha()

def max_leng(plate):
    return len(plate) <= 6

def middle_digits(plate):
    return plate[1:6].isdigit()

main()
