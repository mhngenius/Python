#typeCasting = the process of converting a variable from one data to another
#               str(), int(), float(), bool()

name = "Mahan Mehrabi"
age = 17
gpa = 4.1
is_student = True

#type() = when you put a variable in them , they tell you the type of that variable
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

#converting type of variables
gpa = int(gpa)#removes the decimal point
print(gpa)

age = float(age)#adds a decimal point
print(age)

age = str(age)
print(age)
print(type(age))#It is now converted to a string

name = bool(name)
print(name)#turns it into a "True"
#if the name variables value was empty ("") it would be "False"

