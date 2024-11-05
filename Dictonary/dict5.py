#removeing key value pairs from dictonary

my_dict = {'name' : 'John', 'age' : '25', 'city' : 'New York'}

age = my_dict.pop('age')
#my_dict.clear()

print ('Dictonary After Removel: ', my_dict)
print ('Age', age)