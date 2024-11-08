# List Comprehension with Conditional Nesting

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
even_flattened = [num for row in matrix for num in row if num%2 == 0]

print('Flattened Even Number: ', even_flattened)