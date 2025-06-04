# Calculator Program ⭐

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator: (+ - * /) ")

if operator == "+":
    result = num1 + num2
    print(f"The result is: {round(result, 3)}")
elif operator == "-":
    result = num1 - num2
    print(f"The result is: {round(result, 3)}")
elif operator == "*":
    result = num1 * num2
    print(f"The result is: {round(result, 3)}")
elif operator == "/":
    result = num1 / num2
    print(f"The result is: {round(result, 3)}")
else:
    print(f"{operator} is an invalid operator.")




