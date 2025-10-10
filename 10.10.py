# min1=int(input("Введите 1 границу:"))
# max1=int(input("Введите 2 границу:"))
# if min1 > max1:
#     min1,max1=max1, min1
# for x in range(max1,min1,-1):
#     print(x)

#2
# n=int(input("Введите желаемое количество цифр"))
# count_even = 0
# for x in range(n):
#     number = int(input("Введите число"))
#     if number % 2 == 0:
#         count_even += 1
# print(count_even)
#3
marks = [4,5,98,11,16,100]
# print(marks[1])
# marks_sorted =sorted(marks,reverse = True)
# marks_sorted1 = sorted(marks)
# print(marks_sorted1[0], marks_sorted1[-1])
#
# for x in range(4,-1,-1):
#     print(marks[x],end = " ")


# for in range (5):
#     print(marks[i],end = " ")

# print(marks_sorted)
# print(sum(marks))
# summa = 0
# for i in range(5):
#     summa+=marks[i]
# print(summa)
# min_ = marks[0]
# for y in range(5):
#     if min_ > marks[y]:
#         min_= marks[y]
#
# print(min_)
#1
# counter_2= 0
# for x in marks:
#     if 11<=x<=99:
#         counter_2+=1
# print(counter_2)
#
#
# for x in range (len(marks)+1):
#     if 10<=x<=99:
#         counter_2+=1
# print(counter_2)

#2
# min_ind=0
# max_ind=0
# _min=marks[0]
# _max=marks[0]
# for i in range(len(marks)):
#     if marks[i]>_max:
#         _max=marks[i]
#         max_ind=i
#     if marks[i] < _min:
#         _min=marks[i]
#         min_ind=i
# marks[min_ind],marks[max_ind]=marks[max_ind],marks[min_ind]
# print(marks)

# marks = [4,5,98,11,16,100]
# last=marks[-1]
# first=marks[0]
# #3 нужно перевернуть список
# for i in range(len(marks)//2):
#     marks[i],marks[len(marks)-1-i] = marks[len(marks)-1-i], marks[i]               # do serediny
#
# print(marks)
#
#
# number=int(input("Введите число"))
# for x in marks:
#     if number in marks:
#         print("yes")
#     else:
#         print("no")

# list1=[1,2,3,4,5,6]
# # list2=[1,8,9,6]
# #
# # counter=0
# # for x in list1:
# #     for j in list2:
# #         if x == j:
# #             counter+=1
# #             break
# # print(counter)
#
# size=len(list1)
# counter=0
# for x in range(size):
#     for j in range(size):
#         if x == j:
#             continue
#         if list1[x]==list[j]:
#             unique+=1
#             break
# print(size - counter)

list1=[1,2,3,4,5,6]
list2=[1,8,9,6]
for x in range(len(list1)):
    flag=True
    for j in range(len(list2)):
        if list1[i]==list2[j]
            flag=True
            break
    if flag:
        for j in range(i):
            if list1[i]==list1[j]
                break
        if flag:
            print(list[i], end=" ")









