print('Условная конструкция, оператор if')
first=int(input('Введите первое число: '))
second=int(input('Введите второе число: '))
third=int(input('Введите третье число: '))
if first==second and first==third:
    print('Числа равны,',3)
elif first==second or first==third or second==third:
    print('Чисел равных между собой,',2)
else:
    print('Равных между собой,',0)
print('End')