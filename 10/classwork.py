matrixH = [[2, 3, 4], [5, 6, 7]]

matrixV = [[2, 5], [3, 6], [4, 7]]

matrices = [[[2, 3, 4], [5, 6, 7]], [[2, 5], [3, 6], [4, 7]]]


name = ['Aziz', 'Elbek', 'Umar', 'Abduvali']

# Последний элемент
print(name[len(name) - 1])

# индекс -1
print(name[-2])

# Индексация -> 0
# Индексация <- 1 (Нужно поставить -, как индекатор индексации справа-налево)

# print(name[0], name[1])

for name in name:
    print(name)


names = ['Elbek', 'Sardor', 'Umar', 'Abduvali', 'Dilnura', 'Oybek', 'Xasan'] 
names2 = names[:]
names2 = names

# == is
names.sort()
print(names)


names.reverse()
print(names)


print('aziz' > 'AZIZ')


97 > 65