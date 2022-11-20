#3.10
my_tuple = (1, 2, 3, ['Hi', 'world'])
my_tuple[3][0] = 'hello'
print(my_tuple)
print(my_tuple.count(2))
print(my_tuple.index(['hello', 'world']))