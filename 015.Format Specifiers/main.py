# format specifiers = {:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed points)
# :(number) = allocate that many spaces
# :3 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = inserts a space before positive numbers
# :, = comma separator

price1 = 3.14159
price2 = -987.65
price3 = 12.34
price4 = 123456789

print(f"price 1 is ${price1:+.12f}") # 1 decimal place + added a plus sign (plus positives)
print(f"price 2 is ${price2:^10.3f}") # centered
print(f"price 3 is ${price3:0<10}") # 10 spaces + 0s instead of spaces + right justified
print(f"price 4 is {price4:,}") # comma separate the thousands