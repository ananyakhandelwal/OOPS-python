user_input = input("Enter strings separated by commas: ")

string_list = user_input.split(',')

string_list = [s.strip() for s in string_list]

# Sort the list alphabetically
string_list.sort()

print("Sorted strings:")
for s in string_list:
    print(s)
