for i in range(1, 6):  # Loop for the number of rows
    even_numbers = [str(10 - 2 * j) for j in range(i)]  # Generate even numbers in reverse order
    print(' '.join(even_numbers))  # Print the even numbers for the current row
