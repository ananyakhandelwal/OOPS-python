def triple(number):
    return number * 3

numbers = [1, 2, 3, 4, 5]

tripled_numbers = list(map(triple, numbers))

print("Original numbers:", numbers)
print("Tripled numbers:", tripled_numbers)
