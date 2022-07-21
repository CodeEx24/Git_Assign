list = [1, 2, 3]
tuple_list = []
for i in (list):
    tuple_list.extend([(i, i*i)])
print(tuple_list)
