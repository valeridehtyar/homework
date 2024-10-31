def print_params(a=1, b='строка', c=True) :
    print(a,b,c)
print_params()
print_params(2,'столбец',False)

print_params(b = 25 )
print_params(c=[1,2,3])

print_params()

values_list = [100,'ok',5.5]
values_dist = {'a':[1,2,3],'b':'Leon','c': 0.1}
print_params(*values_list)
print_params(**values_dist)

values_list_2 = [54.32,'строка']
print_params(*values_list_2, 42)
