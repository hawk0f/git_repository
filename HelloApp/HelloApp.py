# -*- coding: cp1251 -*-

print("Hello Python from Visual Studio!")

s = "*"*30
print(s)
print("New Project")
print(s)

try:
    month = int(input("������� ����� ������\n"))
except:
    print("������ ����� ������")
    exit()
if month in [1,2,3]: 
    print("������� �1\n")
elif month in [4,5,6]:
    print("������� �2\n")
elif month in [7,8,9]:
    print("������� �3\n")
elif month in [10,11,12]:
    print("������� �4\n")
else: print("����� ������������ ����� ������")
