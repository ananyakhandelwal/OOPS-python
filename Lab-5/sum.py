list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

added_lists = list(map(lambda x, y, z: x + y + z, list1, list2, list3))

print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)
print("Sum of the lists:", added_lists)
