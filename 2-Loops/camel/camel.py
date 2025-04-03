huzz = input("what should the camel name be? ")
snake_case = ""

for char in huzz: 
    if char.isupper():
        snake_case += "_"
        snake_case += char.lower()
    else:
        snake_case += char

print(snake_case)
# asked for help 