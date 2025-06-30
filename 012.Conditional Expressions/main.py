# conditional expressions = a one line shortcut for the if-else statements (ternary operator)
#                           Print or assign one of two values based on a condition
#                           syntax = X if condition else Y

num = 5 #-5
print("Positive" if num > 0 else "Negative") # if the "num" variable is a positive number , it prints "positive"
                                             # and if not it prints "negative"

# even or odd :

num2 = 8 #7

result = "Even" if num2 % 2 == 0 else "Odd"
print(result)

# greater number :

a = 120
b = 65

max_num = a if a > b else b
print(max_num)

# lesser number :

c = 10
d = 4

min_num = c if c < d else d
print(min_num)

# age status:

age = 25 #17

status = "Adult" if age >= 18 else "Child"
print(status)

# temperature status:

temp = 50 #25

weather = "Hot" if temp > 20 else "Cold"
print(weather)

# user role:

user_role = "Admin" #"Guest"
access_level = "Full Access" if user_role =="Admin" else "Limited Access"
print(access_level)
