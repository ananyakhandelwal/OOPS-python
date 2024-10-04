# Write a Python program to compute the sum of elements of an array of integers. Use the map() function.

def sum_of_array(arr):
    int_array = list(map(int, arr))

    total_sum = sum(int_array)
    
    return total_sum

user_input = input("Enter integers separated by spaces: ")

input_array = user_input.split()

result = sum_of_array(input_array)

print("The sum of the elements is:", result)
