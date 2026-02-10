#Defining a Function
def add (a, b):
    return a + b

# Calling the add function (moved outside the function definition)
result_add = add(5,10)
print(f"Result of add function: {result_add}")

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

# Calling the factorial function
result_factorial = factorial(5)
print(f"Result of factorial function: {result_factorial}")
