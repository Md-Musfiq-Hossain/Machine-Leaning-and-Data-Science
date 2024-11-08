#set oparations with multiple set

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {4, 6, 7, 8}

union_result = set1 | set2 | set3
intersection_result = set1 & set2 & set3
symmetric_difference_result = set1 ^ set2 ^ set3

print('Union of Sets:', union_result)
print('Intersection of Sets:', intersection_result)
print('Symmetric Difference of Sets:', symmetric_difference_result)