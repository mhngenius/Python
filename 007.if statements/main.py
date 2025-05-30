# if = Do some code only IF some condition is true
# else = do something ELSE

age = int(input("Enter your age: "))

if age >= 100: # if the age is equal to or greater than 100 , do this:
    print("You are TOO old to sign up.")
elif age >= 18: # and if the age is equal or greater than 18 , do this:
    print("You are now signed up.")
elif age < 0: # elif = else if , it's a secondary "if" for more than one condition
    print("You haven't been born yet? ")
else : #if not , do this:
    print("You must be 18+ to sign up.")

# EXERCISE 1

response = input("Would you like food ? (y/n) ")

if response == "y":
    print("Have some food :)")
else:
    print("No food for you :(")

# EXERCISE 2

name = input("Enter your name: ")

if name == "":
    print("YOU DID NOT TYPE IN YOUR NAME !!!")
else :
    print(f"Hello {name} :) ")

# Booleans in "if" statements

for_sale = True

if for_sale: # writing the only name of a boolean variable means if variable = true , do this:
    print("This item is for sale")
else :
    print("This item is not for sale")

# EXERCISE 3

online = False

if online :
    print("The user is Online")
else :
    print("The user is Offline")