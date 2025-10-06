# dictionary = a collection of {key:value} pairs
#              ordered and unchangeable. NO duplicates


capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

# getting the value of a key
print(capitals.get("USA"))

if capitals.get("Japan"):
    print("That capital exists.")
else:
    print("That capital doesn't exist.")

# updating a dictionary (adding a key and it's value to an existing dictionary)
capitals.update({"Germany": "Berlin"})
# with update function we can update an existing value as well
# capitals.update({"USA": "Detroit"})
print(capitals)

# removing a key value pair
capitals.pop("China")
print(capitals)

# removing the latest key value pair
capitals.popitem()
print(capitals)

# getting all of the keys (not the values)
keys = capitals.keys()
print(keys)

# iterating through the keys
for key in keys:
    print(key)

# getting all of the values (not the keys)
values = capitals.values()
print(values)

for value in values:
    print(value)

# items = returns a dictionary object that resembles a 2D tuple
items = capitals.items()
print(items)

for key,value in capitals.items():
    print(f"{key}:{value}")

# clearing the dictionary
capitals.clear()
print(capitals)