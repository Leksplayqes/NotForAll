first_list = input('Введите числа через пробел\n')
for k in range(len(first_list)):
    if first_list[k].isalpha() == True:
        first_list = input('Введите ЧИСЛА, а не буквы\n')
        pass
first_list = first_list.split()
first_list = list(map(int, first_list))
max_list = max(first_list)
min_list = min(first_list)
for i in range(len(first_list)):
    if first_list[i] % 3 == 0 and first_list[i] % 5 != 0:
        print('Значение делящеся на 3 и не делящееся на 5: ', first_list[i])

print('Максимальное значение = ', max_list, '\nМинимальное значение = ', min_list)
