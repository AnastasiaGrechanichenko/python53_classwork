first_1 = int(input("Введите начало  диапазона 1 :"))
first_2 = int(input("Введите конец диапазона 1:"))
second_1 = int(input("Введите начало  диапазона 2 :"))
second_2 = int(input("Введите конец диапазона 2:"))
third_1 = int(input("Введите начало  диапазона 3 :"))
third_2 = int(input("Введите конец диапазона 3:"))

number = int(input("Введите число :"))
if first_1 <= number <=first_2 or second_1 <= number <= second_2 or third_1 <= number <= third_2:
    print("Число находится в 1 диапазоне")
    if first_1 <=number <= second_2:
        print("Число находится в 2 диапазонах")
        if first_1 <= number <= third_2:
            print("Число находится в 2 диапазонах")


