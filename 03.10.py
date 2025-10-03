# n = int(input("n="))
# a= 0
# while n>0:
#     print(a)
#     a+=1
#     n-=1
#     if n == 6:
#         break
# num = int(input("num="))
# a = 0
# while a <= num:
#     print(a)
#     a += 2
# number = int(input("number="))
# while number > 0 :
#     print("Привет")
#     number-=1
# min_1 = int(input("min_1="))
# max_1 = int(input("max_1="))
#
# if max_1<min_1:
#     min_1,max_1=max_1,min_1
#
# if min_1 % 2: # если тру значит четное
#     min_1+=1
#
# while min_1 <= max_1:
#     if min_1 % 2 == 0: # неоптимально проверку перед циклом
#     print(min_1)
#     min_1+=2
# n=0
# number = int(input("number="))
# while number > 0:
#     number= number//10
#     n += 1
# print(n)

# summ = 0
# while True:
#     number = int(input("number="))
#     if n==0:
#         break
#     sum += number
# print(summ)


import random


answer = random.randint(0,100)
attempts = 0
best_attempt = 101
counter = 5
number_of_games=1
best_game
while True:
    number_of_games+=1
    while True:
        number = int(input("Введите число от 0 до 100: "))
        if number > answer:
            print("Введенное число больше загаданного")
        elif number < answer:
            print ("Введенное число меньше загаданного")
        elif number == answer:
            print("Вы угадали {attempts} раз!")
            if best_attempt > counter:
                best_result=counter
                best_game=number_of_games
            break

        if number !=answer:
            counter-=1
            attempts += 1
            if counter ==0:
                print("Количество попыток исчерпано")
                break


    continuation=input("Желаете продолжить игру(да/нет)?").lower()
    if continuation=="да":
        number = int(input("Введите число от 0 до 100: "))
        number_of_games+=1
    elif continuation=="нет":
        print(best_attempt)
        break
print(best_attempt,number_of_games)







