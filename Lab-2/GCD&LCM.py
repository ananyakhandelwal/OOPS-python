import math

# Function to calculate LCM
def calculate_lcm(x, y):
    return abs(x * y) // math.gcd(x, y)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate GCD
gcd = math.gcd(num1, num2)
# Calculate LCM
lcm = calculate_lcm(num1, num2)

# results
print(f"The GCD of {num1} and {num2} is: {gcd}")
print(f"The LCM of {num1} and {num2} is: {lcm}")
