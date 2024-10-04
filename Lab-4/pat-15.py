for i in range(1, 6):  # Loop for rows from 1 to 5
    # Print leading spaces for alignment
    print(' ' * (10 - 2 * i) + ' '.join(str(j) for j in range(1, i + 1)))

