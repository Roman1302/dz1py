# сортировка массива


from random import randint
len_mass = int(input("Количество столбцов: ")) # задаем длину массива(списка из списков)
len_elem = int(input("Количество строк: ")) # количество элементов в элементе(подсписке)
a,b = 0,9 # диапазон, можно задавать через input()
mass = [[randint(a,b) for _ in range(len_elem)] for _ in range(len_mass)] #задаем рандомный массив
for i in range(len(mass)): #выводим на печать 
    for j in range(len(mass[i])):
        print(mass[i][j], end='    ')
    print()

    
print("--------------")

mas2 = []
for i in mass:
    for i2 in i:
        mas2.append(i2)
mass=sorted(mas2) #сортируем массив
for x in range(0, len(mass), len_elem):
    e_c = mass[x : len_elem + x]
    if len(e_c) < len_elem:
        e_c = e_c + [None for y in range(x - len(e_c))]
    print(list(e_c))
