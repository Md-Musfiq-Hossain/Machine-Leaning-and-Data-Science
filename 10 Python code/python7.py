#dictonary with nested structures

nested_dict = {
    'person' : {
        'name' : 'john', 
        'details' : {
            'age' : 25,
            'city' : 'New York',
            'skils' : ['python', 'Data analysis']
        }
    }
}

city = nested_dict['person']['details']['city']

nested_dict ['person']['details']['skils'].append('Meachine Learning')

print('City: ', city)
print('Updated nested Dictonary: ', nested_dict)