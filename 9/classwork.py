# while условие:
    # тело цикла


# ! В цикле while условие когда - то должно стать FALSE
# ? В условии есть переменная, которая должна меняться при каждом проходе цикла
# * Переменная меняется в теле цикла 
# ! Обычно переменная явлется счётчиком 

# Пример вывода чисел от 10 до 20 включительно

i = 10
while i <= 20:
     print(i, end=' ')
     i = i + 1


for i in range(10, 21):
     print(i, end=' ')


# Пример вывода чисел от 200 до 150 включительно, десятками

for i in range(200, 149, -10):
     print(i, end=" ")

i = 200 
while i >= 150:
     print(i, end=" ")
     i = i - 10

name = 'Aziz'

# Индексы долджны быть целым числом, а иначе будет ошибка
i = 0
while i < 5: 
     print(name[i])
     i = i + 1


for ltr in name: 
     print(ltr, end="/")

for i in range(len(name)):
     print(name[i], end="/")


# Способы создать бесконечный цикл 
# 1. Написать условие, которое всегда будет верным

while i > 0:
     pass


# 2. В условии написать TRUE

while True:
    pass

# Как остановить цикл, который бесконечный -> Нужно, чтобы консоль была активной и нажать Ctrl + C


# Как управлять циклом, который бесконечный?
# Ответ -> с помощью if и break

i = 0
while True:
    print('Aziz')
    i = i + 1 
    if i == 10:
        break


while True: 
    num = int(input('Enter positive number: '))
    if num - 2 < 0:
        break

# int
# float
# bool

# !Индекструемые объекты
# str
#list

# Гомогенный список -> потом, что в нём только СТРОКИ
students = ['Umar', 'Abduvali', 'Oybek', 'Iskander']
ages = [16, 16, 16, 13, 14, 15]
countries = ['Ubekistan', 'USA', 'Germany', 'Poland', 'Sweden']
country_codes = ["UZ", "PO", "UK", "UA"]

cars = ["BMW", "Audi", "Lamborgini", "Mersedes" ]
drinks = ["Cola", "Pepsi", "Fanta",]