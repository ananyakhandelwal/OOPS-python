# Function to print the multiplication table
def print_multiplication_table(number, upto):
    for i in range(1, upto + 1):
        print(f"{number} x {i} = {number * i}")

number = int(input("Enter the number for which you want the multiplication table: "))
upto = int(input("Enter the range (upto which multiple): "))

print_multiplication_table(number, upto)
