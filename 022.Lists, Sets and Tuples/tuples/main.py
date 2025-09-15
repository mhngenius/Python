# lists, sets, and tuples

# collection = single "variable" used to store multiple values
# List  =  [] ordered and changeable. Duplicates OK
# Set   =  {} unordered and immutable , but Add/Remove OK. NO Duplicates
# Tuple =  () ordered and unchangeable. Duplicates OK. FASTER

fruits = ("apple","orange","banana","coconut","coconut")
print(fruits)

print(fruits.index("apple")) # shows the index number
print(fruits.count("coconut")) # counts specific values

for fruit in fruits:
    print(fruit)