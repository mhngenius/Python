# lists, sets, and tuples

# collection = single "variable" used to store multiple values
# List  =  [] ordered and changeable. Duplicates OK
# Set   =  {} unordered and immutable , but Add/Remove OK. NO Duplicates
# Tuple =  () ordered and unchangeable. Duplicates OK. FASTER

fruits = {"apple","orange","banana","coconut","coconut"}

# print(fruits[0]) # error because there is no index number in sets because they are unordered

fruits.add("pineapple")
fruits.remove("orange")
fruits.pop() # pop = removes the first element (in this case , randomly)
fruits.clear() # all the element would be gone



print(fruits)