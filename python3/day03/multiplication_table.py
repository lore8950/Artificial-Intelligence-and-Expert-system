#print multiplication table of a number
def print_multiplication_table(number):
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

# Example usage:
number = 7
print_multiplication_table(number)
