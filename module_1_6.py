print('Словари и множества')
my_dict={'Алёна':16071982,'Валерий':4111965,'Лев':30052016}
print(my_dict)
a=my_dict.pop('Алёна')
print(a)
print(my_dict.get('Вася','Такого ключа нет'))
my_dict.update({'Андрей':21011964,'Саша':9111990})
print(my_dict)
del my_dict['Валерий']
print(my_dict)
my_set={1,2,3,4,3,2,1,'book'}
print(my_set)
print(my_set.add(5))
print(my_set.add(6))
print(my_set)
print(my_set.remove(3))
print(my_set)
print('End')
