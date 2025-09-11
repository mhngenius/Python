# lists, sets, and tuples

# collection = single "variable" used to store multiple values
# List  =  [] ordered and changeable. Duplicates OK
# Set   =  {} unordered and immutable , but Add/Remove OK. NO Duplicates
# Tuple =  () ordered and unchangeable. Duplicates OK. FASTER

# Lists
fruits = ["apple", "orange", "banana", "banana", "coconut", "pineapple"]
# print(dir(fruits)) guide
# print(help(fruits)) guide

print(fruits) # prints all of them

print(fruits[0]) # prints the specified index number
print(fruits[1])
print(fruits[2])
print(fruits[3])

print(fruits[0:3]) # prints specified range from one index number to the another
print(fruits[::2]) # prints the range by a specific step
print(fruits[::-1]) # reverses

fruits[0] = "peach" # changing a specified element (here it's at index of 0 means apple) to another specified value (peach)

fruits.append("strawberry") # adds one element to the end

fruits.remove("orange") # removes the specified value
print(fruits)

fruits.insert(0,"grapes") # adds one element to a specified index number
print(fruits)

fruits.reverse() # reverses the elements based on the order
print(fruits)

fruits.sort() # sorts the elements by Alphabetical order
print(fruits)

fruits.reverse() # reverses the elements by Alphabetical order
print(fruits)

print(fruits.index("coconut")) # returns the index number of an element

print(fruits.count("banana")) # counts how many times an element appeared in the list

fruits.clear() # all of the elements are gone
print(fruits)

for fruit in fruits: # iterating through the list by using a for loop
    print(fruit)

print(len(fruits)) # length of the list

print("apple" in fruits) # in operator returns if an value is in list or not (boolean)
print("kiwi" in fruits)