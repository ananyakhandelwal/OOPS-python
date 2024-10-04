strings = ["hello", "world", "python"]

listified_strings = list(map(lambda s: list(s), strings))

print("Original strings:", strings)
print("Listified strings:", listified_strings)
