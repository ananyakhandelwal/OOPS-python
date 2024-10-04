# Write a Python program to create a new list taking specific elements from a tuple and convert a string value to an integer. 

integer_tuple = (10, 20, 30, 40, 50)

indices_to_take = [0, 2, 4]  # Taking the 1st, 3rd, and 5th elements

new_list = [integer_tuple[i] for i in indices_to_take]

string_value = "123"

converted_integer = int(string_value)

print("Original tuple:", integer_tuple)
print("New list from tuple:", new_list)
print("Converted integer from string:", converted_integer)
