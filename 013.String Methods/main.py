# string methods

name = input("Enter your full name: ")

result = len(name) # "len" function measures the length of a string value
print(result)

result2 = name.find("M") # "find" function , finds the first appearance of a specific character
print(result2)

result3 = name.rfind("M") # "rfind" function , finds the last appearance of a specific character
print(result3)

result4 = name.capitalize() # "capitalize" function , turns the first letter to the capital form
print(result4)

result5  = name.upper() # "upper" function , turns all of the letters to the capital form (upper case)
print(result5)

result6 = name.lower()  # "lower" function , turns all of the letters to lower case
print(result6)

result7 = name.isdigit() # "isdigit" function returns True if a value is number and if not it returns False
print(result7)

result8 = name.isalpha() # "isalpha" function returns True if a value is a string (alphabetical characters) and if not it returns False
                         # " " = False
print(result8)

result9 = name.startswith("m") # "startswith" function checks if a value starts with a specific character (boolean)
print(result9)

result10 = name.endswith("m") # "endswith" function checks if a value ends with a specific character (boolean)
print(result10)

phone_number = input("Enter your phone number: ")
result11 = phone_number.count("-") # "count" function , counts amount of  a specific character
print(result11)

result12 = phone_number.replace("-"," ") # "replace" function actually replaces a specific character with another one
                                                     # syntax = ("old" , "new")
print(result12)

# help() function actually shows a list of methods available for a data type:
print(help(str))

# Exercise 1 : Validate user input
# 1.username is no more than 12 characters
# 2.username must not contain spaces
# 3.username must not contain digits

user_name = input("Enter a username: ")

if len(user_name) > 12 :
    print("Your username can't be more than 12 characters")
elif not user_name.find(" ") == -1: # when something is wrong python returns -1
    print("Your username can't contain spaces")
elif not user_name.isalpha():
    print("Your username can't contain numbers")
else :
    print(f"Welcome {user_name}")
