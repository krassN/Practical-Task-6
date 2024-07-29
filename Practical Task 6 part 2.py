# работа с множествами:

my_set = {1, 2, 5.5, 7, 1, 5, 1000, 'Sun', 'Sun', 'Sea', (1, 2), (2, 1), False, True}
print('Set:', my_set)
my_set.update(['Beach', 23])
my_set.pop()
print('Modified set', my_set)

# дополнительно к заданию:
my_set2 = {3, 7, 10, 5.5}
my_set3 = my_set.union(my_set2)
print('My_set:', my_set3)
