#removing elements from a tuple

my_tuple = (1, 2, 3, 4)

temp_list = list(my_tuple)
temp_list.remove(2)
my_tuple = tuple(temp_list)

print('Tuple after removal:', my_tuple)