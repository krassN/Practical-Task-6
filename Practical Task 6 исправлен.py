# работа с множествами:

my_set = {1, 2, 5.5, 7, 1, 5, 1000, 'Sun', 'Sun', 'Sea', (1, 2), (2, 1), False, True}
print('Set:', my_set)
my_set.update(['Beach', 23])
my_set.discard('Sea')
print('Modified set', my_set)
