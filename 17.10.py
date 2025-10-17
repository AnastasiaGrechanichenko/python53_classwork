#1
num1=int(input("Введите число: "))
num2=int(input("Введите число: "))
num3=int(input("Введите число: "))
num4=int(input("Введите число: "))
minimum = num1
if num1 > num2:
    minimum=num2
    if num2>num3:
        minimum = num3
    else:
        minimum = num2
        if num3>num4:
            minimum=num4
        else:
            maximum = num3
print(minimum)

#2
for in range

#3
# side = int(input("Введите сторону квадрата: "))
# counter = side+1
# for i in range(1,side+1):
#     for j in range(side - i, i ):
#         print("*", end = " ")
#         print()
#     print(" ",end = " ")


# #4
# counter = 0
# summ=0
# while True:
#     num1=int(input("Введите число: "))
#     if num1==0:
#         print(summ/counter)
#         break
#     else:
#         counter+=1
#         summ+=num1

#5
import random
list1=[0]*10


size=len(list1)

b1 = int(input("Введите 1 границу: "))
b2 = int(input("Введите 2 границу: "))
if b2 < b1:
    b1,b2 = b2,b1
for i in range(size):
    random_number = random.randint(b1,b2)
    list1[i] = random_number

print(list1)

#6
list3=[1,2,5]
minimum=list3[0]
for x in list3:
    if x < minimum:
        minimum = x
print(list3.index(minimum))

#7
def copy_list(list1,list2):
    for i in range(len(list)):
        list2[i]=list1[i]
first=[1,2]
second=[0,0]


print(copy_list(first,second))
#8
list4=[1,2,3,4]

def insert_element(_list,element,position):
    _list.insert(position,element)
print(insert_element(list4,5,0))



#9
def generate_list(n,a,b):
    list1 = []
    if a > b:
        a,b=b,a
    for x in range(a,b):
        random_number=random.randint(a,b)
        list1.append(random_number)
        if len(list1)==n:
            print(list1)
            break
def delete_number(_list,num):
    if num in _list:
        del num

list2=[1,2,1,3]
print(delete_number(list2,1))


print(generate_list(10,1,5))













