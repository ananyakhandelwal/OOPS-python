for i in range(5, 0, -1):  # Loop for each row starting from 5 to 1
    # decreasing sequence
    decreasing = list(range(5, i - 1, -1))
    # increasing sequence
    increasing = list(range(i, 6))
    pattern = decreasing + increasing
    print(' '.join(map(str, pattern)))
