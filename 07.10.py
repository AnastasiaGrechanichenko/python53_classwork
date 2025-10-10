# count = 0
# summ = 0
#
#
# while True:
#     number = int(input("Введите число кратное 5 "))
#     if number % 5 == 0:
#         break
#     else:
#         summ+=number
#         count += 1
#


#  print(summ / count)
# number = int(input("Введите простое число"))
# delit = 2
# flag_element= True
# while delit < number/2 :
#     if number % delit == 0:
#         flag_element = False
#         break
#     delit +=1
# print( "простое " if flag_element else "не простое ")


# number = int(input("Введите простое число"))
# count = 0
# while count <=number:
#     delit = 2
#     flag_element = False
#     while delit<= count / 2:
#         if count % delit == 0:
#             flag_element = False
#             break
#         delim +=1
#     if flag_element:
#         print(count, end= " ")
# count = 0
# for i in range(10):
#     if  i == 3:
#         count +=4
#         continue
#         print(i, end =" ")
# max_ = int(input("Введите диапазон "))
# min_ = int(input("Введите диапазон "))
# if min_ > max_:
#     _min, _max = _max, _min
# if _max%2==1:
#     _max-=1
# for x in range (_max,_min-1, -2 ):
#     print(x, end = " ")

# number = int(input("Введите число: "))
# for x in range (1, number+1 ):
#     print (" * "* number)

# number = int(input("Введите число: "))
# for x in range (1, number+1 ):
#     for i  in range (1, number+1):
#         print("*", end = " ")
#     print()
# count = 1
# number = int(input("Введите число: "))
# for x in range (1, number):
#     for i  in range (1, number):
#         print(count, end = " \t")
#         count+=1
#     print()

# count = 1
# number = int(input("Введите число: "))
# for x in range (number):
#     for i  in range (number):
#         print(x+1 , ":", i+1, end = " \t")
#         count+=1
#     print()


# number = int(input("Введите число: "))
# for i in range (number):
#     for j in range (i+1):
#         print("*", end = " ")
#     print()


# number = int(input("Введите число: "))
# for i in range (number):
#     for j in range (number-i):
#         print( "*", end = " ")
#     print()

# number = int(input("Введите число: "))
# for i in range (number):
#     for j in range (i,number):
#         print( "*",end = " ")
#     print()

# number = int(input("Введите число: "))
# space = " "

# number = int(input("Введите число: "))
# for i in range (number):
#     for j in range (number):
#         print( " ",end = " ")
#     for j in range (number-i ):
#         print( "*",end = " ")
#     print()

 # *
#
                                         # **
# number = int(input("Введите число: "))
# for i in range (number):
#     for j in range (number-i):
#         print( " ",end = " ")
#     for j in range (i):
#         print( "*",end = " ")
#     print()

number = int(input("Введите число: "))
for i in range (number):
    for j in range(i):
        print(" ", end = " ")
    for j in range (number-(i*2)):
        print("* ", end =" ")
    print()



























