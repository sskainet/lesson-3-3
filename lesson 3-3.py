def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
# 1
print_params(b = 25)
print_params(c = [1,2,3])
# 2
values_list = ['Привет', 999, [1, 2, 3]]
values_dict = {'a': [1, 2, 3], 'b': 'Привет', 'c': 999}
print_params(*values_list)
print_params(**values_dict)
# 3
values_list_2 = ['абв', [4, 5, 6]]
print_params(*values_list_2, 42)