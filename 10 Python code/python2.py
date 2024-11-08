#Tuple Unpacking

person_info = ('John', 25, 'New Tork', 'Engineer', 'Single')

name , age, *other_details = person_info

print('Name: ', name)
print('Age: ', age)
print('Ohter Details: ', other_details)
