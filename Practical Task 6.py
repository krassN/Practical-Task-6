# работа со словарями:

my_dict = {'Nataly': 1986, 'Vladimir': 1984, 'Elena': 1985}
print(my_dict)
print('Existing value:', (my_dict['Vladimir']))
print('Not existing value:', (my_dict.get('Kamila')))
my_dict.update({'Ekaterina': 1986, 'Oleg': 1988})
a = my_dict.pop('Elena')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
