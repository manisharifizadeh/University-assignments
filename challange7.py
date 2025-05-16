# Empty list to store even numbers
even_numbers = []

# Check numbers from 1 to 100
for num in range(1, 101):

    # If the number is even
    if num % 2 == 0:
        # Add number to the list
        even_numbers.append(num)

# Print even numbers
print(even_numbers)
