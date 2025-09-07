# nested loops = A loop within another loop (outer , inner)
#                Outer loop:
#                           Inner loop:

for i in range (3):
    for x in range (1,11):  # printing numbers from 1-10
     print(x, end=" ") # 'end = " "' = every single of the numbers are in one line
    print() # print() = put each iteration on a new line (it should be on outer loop)


# EXERCISE 1 : Create a rectangle

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for z in range (rows):
    for y in range (columns):
        print(symbol, end="")
    print()


# EXERCISE 2 : making a triangle

highest_point = int(input("Enter the highest point of the triangle: "))

for a in range (1, highest_point+1):
    print("*" * a)
for b in range (highest_point, 0, -1):

    print("*" * b)
