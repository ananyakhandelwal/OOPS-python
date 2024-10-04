import math

# Function to check if a number is a strong number
def is_strong_number(num):
    sum_of_factorials = 0
    temp = num
    
    while temp > 0:
        digit = temp % 10
        sum_of_factorials += math.factorial(digit)
        temp //= 10

    return sum_of_factorials == num
num = int(input("Enter a number: "))

# Check if the input number is a strong number
if is_strong_number(num):
    print(f"{num} is a Strong number.")
else:
    print(f"{num} is not a Strong number.")
