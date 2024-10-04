for i in range(1, 6):  # Loop for each row
    #  increasing sequence
    increasing = list(range(1, i + 1))
    #  decreasing sequence
    decreasing = list(range(i - 1, 0, -1))
    # Combine and print the pattern
    print(' '.join(map(str, increasing + decreasing)))
