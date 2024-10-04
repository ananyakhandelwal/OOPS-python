user_input = input("Enter a string: ")

unique_chars = list(dict.fromkeys(user_input))

uppercase_chars = list(map(lambda x: x.upper(), unique_chars))
lowercase_chars = list(map(lambda x: x.lower(), unique_chars))

print("Original string:", user_input)
print("Unique uppercase characters:", ''.join(uppercase_chars))
print("Unique lowercase characters:", ''.join(lowercase_chars))
