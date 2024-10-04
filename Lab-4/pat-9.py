number = 1  # Start from 1

for i in range(1, 5):  # Loop for the number of rows
    row_numbers = list(range(number, number + i))  # Create a list of numbers for the current row
    row_numbers.reverse()  # Reverse the order for the current row
    print(' '.join(map(str, row_numbers)))  # Print the reversed numbers as a string
    number += i  # Update the starting number for the next row
