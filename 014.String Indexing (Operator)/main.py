# indexing = accessing elements of a sequence using [] (indexing operation)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0]) # first index
print(credit_number[1])
print(credit_number[2])
print(credit_number[4])

print(credit_number[0:4]) # first 4 characters
print(credit_number[:4]) # it's the same as the one above (writing nothing before the colon means going all the way at the beginning)

print(credit_number[5:9]) # second 2 characters
print(credit_number[5:]) # writing nothing after the colon means going all the way to the end

# negative indexes
print(credit_number[-1]) # -1 = last index
print(credit_number[-2])
print(credit_number[-3])
print(credit_number[-5])

# steps
print(credit_number[::2]) # every second character
print(credit_number[::3]) # every third character

# Exercise 1 :
# getting the last four digits of a credit card number :

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

# Exercise 2 :
# reversing the characters in the string
reversed = credit_number[::-1]
print(reversed)