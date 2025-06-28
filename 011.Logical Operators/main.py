# logical operator = evaluate multiple conditions (or, and, not)
#         or = at least one condition must be true
#         and = both conditions must be true
#         bot = inverts the condition (not False, not True)
from math import trunc

# 1) or:

temp = 35 #40 #-3
is_raining = False # True

if temp > 35 or temp < 0 or is_raining:
    print ("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

# 2) and:

temp2 = -5 #30 #20
is_sunny = False #True

if temp2 >= 28 and is_sunny: #boolean variable with nothing in front of it in an if statement means
                             # if that variable's value is what we have already defined
    print("It is HOT outside!!! 🥵")
    print("It is SUNNY!!")
elif temp2 <= 0 and is_sunny:
    print("It is COLD outside!!! 🥶")
    print("It is Sunny!!")
elif 28 > temp2 > 0 and is_sunny: # between a range
    print("It is WARM outside")
    print("It is sunny")

# 3) not:
# Continuation of the previous code:

elif temp2 >= 28 and not is_sunny: # It means if "is_sunny" was False do some code ,
                                # because is_sunny is already True and the "not" operator inverts it
    print("It is HOT outside!!! 🥵")
    print("It is cloudy")
elif temp2 <= 0 and not is_sunny:
    print("It is COLD outside!!! 🥶")
    print("It is cloudy")
elif 28 > temp2 > 0 and  not is_sunny: # between a range
    print("It is WARM outside")
    print("It is cloudy")
