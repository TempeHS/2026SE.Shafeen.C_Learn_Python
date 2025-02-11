x, y, z = input("Enter somthibg: ").split()
x = int(x)
z = int(z)

if y == '+':
    result = (x + z)
elif y == '-':
    result = (x - z)
elif y == '*':
     result = (x * z)
elif y == '/':
    result = (x / z)  
else:
    print("Invalid operator")
print(f"{result:.1f}") 




