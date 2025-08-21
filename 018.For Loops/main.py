# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

for x in range(1,11): # (starting number , ending number + 1)
    print(x)

for i in reversed(range(1,11)): # counting backwards using reversed function
    print(i)
print("HAPPY NEW YEAR !!!")

for y in range (1, 11, 2): # ,2 = two by two
    print(y)

credit_card = "1234-5678-9012-3456"

for z in credit_card : # digits of variable
    print(z)

# Exercise 1 :

# Skipping the number 13

for a in range (1,21):
    if a == 13:
        continue # continue key word is useful for skipping over things
    else:
        print(a)