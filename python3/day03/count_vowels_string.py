#count vowels in a string
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

# Example usage:
my_string = "Hello World"
vowel_count = count_vowels(my_string)
print(f"The number of vowels in '{my_string}' is: {vowel_count}")

another_string = "Python Programming"
vowel_count_2 = count_vowels(another_string)
print(f"The number of vowels in '{another_string}' is: {vowel_count_2}")
