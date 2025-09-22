# 2D collections = a list made with lists

fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

fruits[0] = "pineapple" # changing the index 0 of fruits list
print(fruits)
print(vegetables)
print(meats)
print()

print(groceries)
print(groceries[1]) # prints the whole list as the index 1
print(groceries[2][1]) # prints the inner index of the inner list (for specific item)
                       # syntax = [index of the 2D list][index of the specified 1D list]

# for iterating in 2D lists we should use nested loops

for collection in groceries:
    print(collection) # prints the whole 1D lists

for collection2 in groceries:
    for food in collection2:
        print(food, end=" ") # prints each element individually
    print()

# YOU CREATE USE 2D COLLECTION WITH EVERY TYPE OF COLLECTIONS

# EXERCISE: key pad

# this time we are using tuples so they would be unchangeable (in order)
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

# now we have a phone num pad