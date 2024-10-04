def power(base, exponent):
    return base ** exponent

number = int(input("enter a number: "))

indices = list(range(6))  # This will create [0, 1, 2, 3, 4, 5]

powers_list = list(map(lambda x: power(number, x), indices))

print("Base number:", number)
print("Powers of", number, "raised to indices:", powers_list)
