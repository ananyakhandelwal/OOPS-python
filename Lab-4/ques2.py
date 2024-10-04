# A. Separate the string into comma-separated values
X = "India.is.my.country"
comma_separated_values = X.replace('.', ',')
print("Comma-separated values:", comma_separated_values)

# B. Remove a given character from a string
Y = "M.A.N.I.P.A.L"
char_to_remove = input("Enter the character to remove from the string Y: ")  
modified_string = Y.replace(char_to_remove, '')
print("String after removing character:", modified_string)

# C. Remove the (.) dots from the above string 
dots_removed_string = Y.replace('.', '')
print("String after removing dots:", dots_removed_string)

