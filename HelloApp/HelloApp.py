# -*- coding: cp1251 -*-

print("Hello Python from Visual Studio!")

s = "*"*30
print(s)
print("New Project")
print(s)

try:
    month = int(input("Введите номер месяца\n"))
except:
    print("Ошибка ввода данных")
    exit()
if month in [1,2,3]: 
    print("Квартал №1\n")
elif month in [4,5,6]:
    print("Квартал №2\n")
elif month in [7,8,9]:
    print("Квартал №3\n")
elif month in [10,11,12]:
    print("Квартал №4\n")
else: print("Введён некорректный номер месяца")
