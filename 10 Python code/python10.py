#Tuple Comprehension Uinsg Generator Expression

number = range(1, 11)

even_squares = tuple(x**2 for x in number if x % 2 == 0)

print('Tuple of Even Squres: ', even_squares)
