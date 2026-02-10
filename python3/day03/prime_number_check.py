#write a function to check prime number
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage:
print(f"Is 7 a prime number? {is_prime(7)}")       # Expected: True
print(f"Is 10 a prime number? {is_prime(10)}")      # Expected: False
print(f"Is 2 a prime number? {is_prime(2)}")        # Expected: True
print(f"Is 1 a prime number? {is_prime(1)}")        # Expected: False
print(f"Is 29 a prime number? {is_prime(29)}")      # Expected: True
