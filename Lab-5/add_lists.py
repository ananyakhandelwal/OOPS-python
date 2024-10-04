list1 = [10, 20, 30, 40, 50]
list2 = [5, 15, 25, 35, 45]

added_lists = list(map(lambda x, y: x + y, list1, list2))

difference_lists = list(map(lambda x, y: x - y, list1, list2))

print("List 1:", list1)
print("List 2:", list2)
print("Sum of the lists:", added_lists)
print("Difference between the lists:", difference_lists)
