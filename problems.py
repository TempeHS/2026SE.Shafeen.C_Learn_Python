num1 = int(input("num 1: "))
num2 = int(input("num 2: "))
operator = input("enter an operator: ")
ui_output = ""

if operator == "-":
    ui_output = num1 - num2
elif operator == "+":
    ui_output = num1 + num2
elif operator == "*":
	ui_output = num1 * num2
elif operator == "/":
	ui_output = num1 / num2
else:
	ui_output = print("Not a known operator")

print(ui_output)
