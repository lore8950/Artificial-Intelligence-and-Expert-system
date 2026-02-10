#Find largest number from a list
numbers = [10, 5, 20, 15, 30]
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("The largest number is:", largest)
