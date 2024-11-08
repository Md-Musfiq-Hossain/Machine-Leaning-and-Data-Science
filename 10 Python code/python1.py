# Nested Lists Oparations

nested_list = [[1, 2, 3], [4, 5, [6, 7]], [8, 9]]


nested_elements = nested_list[1][2][1]


nested_list[2][1] = 10

flattened_list = [elements for sublist in nested_list for item in sublist for elements in (item if isinstance(item, list)
else [item])]


print ('Nested Element: ', nested_elements)
print ('Modified Nested List: ', nested_list)
print ('Flattened List: ', flattened_list)