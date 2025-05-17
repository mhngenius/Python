# Accepting User Input :
# input() = A function that prompts the user to enter data
#           Returns the data as a string

name = input("What is your name?")# asks the user to enter their name (put it in the variable "name")
print (f"Hello {name}")# print a hello message for them

age = input("H0w old are you?")
age = int(age)# because the age variable is a string we have to convert it to integers
age = age + 1 # when we want to change them mathematically
              # or another way:
              # age = int(input("Hpw old are you?")) type cast it at the begging
print("HAPPY BIRTHDAY!")
print (f"You are {age} years old")

# EXERCISE 1
# Area of a rectangle
length = float(input("Enter the length:"))
width = float(input("Enter the width:"))

area = length * width

print(f"The area is: {area}cm²")

# EXERCISE 2
# shopping cart program

item = input("What item would you like to buy?")
price = float(input("What is the price?"))
quantity = int(input("How many would you like?"))

total = price * quantity

print(f"You have bought ${quantity} x ${item}/s")
print(f"Your total is {total}$")
