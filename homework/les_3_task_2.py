# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
# т. к. именно в этих позициях первого массива стоят четные числа.

f_list = []
while True:
    a = (input("Введите число для добавления в список, если хотите выйти, напишите '!': "))
    if a != "!":
        f_list.append(int(a))
    else:
        break

even_numbers = [i for i, x in enumerate(f_list) if x % 2 == 0]
print(f"Индексы элементов кратные двум: {even_numbers}")