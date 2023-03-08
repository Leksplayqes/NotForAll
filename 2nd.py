first_list = input('Введите числа через пробел\n')
for k in range(len(first_list)):
    if first_list[k].isalpha() == True:
        first_list = input('Введите ЧИСЛА, а не буквы\n')
        pass
first_list = first_list.split()
for i in range(len(first_list)):
    for k in range(i+1, len(first_list)):
        if first_list[i] == first_list[k]:
            print(first_list[i])
