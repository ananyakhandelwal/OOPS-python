# Write a Python program to compute the square of the first N Fibonacci numbers, using the map function and generate a list of the numbers.

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    return fib_sequence[:n]

N = int(input("Enter the number of Fibonacci numbers to compute: "))

fib_numbers = fibonacci(N)

squared_fib_numbers = list(map(lambda x: x ** 2, fib_numbers))

print(f"The first {N} Fibonacci numbers:", fib_numbers)
print(f"The squares of the first {N} Fibonacci numbers:", squared_fib_numbers)
