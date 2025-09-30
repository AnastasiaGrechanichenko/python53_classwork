min_1 = int(input("Введите начало  диапазона 1 :"))
max_1 = int(input("Введите конец диапазона 1:"))
min_2 = int(input("Введите начало  диапазона 2 :"))
max_2 = int(input("Введите конец диапазона 2:"))
min_3 = int(input("Введите начало  диапазона 3 :"))
max_3 = int(input("Введите конец диапазона 3:"))

number = int(input("Введите число :"))

# решаем через счетчик
counter = 0
if min_1>max_1:
    min_1,max_1=max_1,min_1
if min_2>max_2:
    min_2,max_2 = max_2,min_2
if min_3>max_3:
    min_3,max_3=max_3,min_3

if min_1 <=n <=max_1: counter+=1
if min_2 <=n <=max_2: counter+=1
if min_3 <=n <=max_3: counter+=1
print(counter)