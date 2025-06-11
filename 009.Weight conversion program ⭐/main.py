# Weight conversion program ⭐

weight = float(input("Enter your weight: "))
unit = input("KG or lbs? ")

if unit == "KG" or unit == "kg":
    weight = weight * 2.205
    unit = "lbs"
    print(f"your weight is: {round(weight, 3)}{unit}")
elif unit == "lbs" :
    weight = weight / 2.205
    unit = "KG"
    print(f"your weight is: {round(weight, 3)}{unit}")
else :
    print(f"{unit} was not valid")
