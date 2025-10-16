list1=[1,2,8,3,4,8,5,4,3]
list2=[1,2,8,3,4,8,5,4,7]

def print_list(_list):
    for x in _list:
        print(x,end = " ")
    print()
print_list(list1)
print_list(list2)


for x in range(len(list1)):
    print(list1[x], end = " ")
print()


print(*list1)


# for x in range(len(list1)):
#     for y in range(len(list1)):
#         if list1[x] % 2 == 0:
#             list1[x] = list1[x]
#         else:
#             list1[x] = 0
#
# print(list1)


for i in range(len(list1)):
    flag1 = False
    for j in range(len(list1)): # не учитывать самого себя только повторы печатаем
        if i == j:
            continue

        if list1[i] == list1[j]:
            flag1=True
            break
    if flag1:
        for j in range(i):
            if list1[i] == list1 [j]:
                flag1 = False
                break
        if flag1:
            print(list1[i], end = " ")


tuple1 = (2,4,6)
set1 = {1,2,8,3,4,8,5,4,3}
set1=set(list1)
dict1 = {
    1: "Vasya",
    2: "Ira",
    3: "Robert"
}
print()
print(list1)
print(tuple1)
print(set1)
print(dict1)

print(dict1.get(2)) # по ключу

def print_sum(_list):
    print(sum(_list))
print_sum(list2)

def list_sum(_list):
    summ = 0
    for x in range (len(_list)):
        summ+=_list[x]
    return summ
print_sum(list2)
print(list_sum(list1)/ len(list1))

number = 8
def foo1():
    a=number
    print(a)
def foo2():
    a=number
    print(a)
foo1()
foo2()

list3=[3,4,5,6]
print(list3)
def p_even(_lst):
    for i in range(len(_lst)):
        for j in range(len(_lst)):
            if _lst[i] % 2 == 0:
                _lst[i] = 0
print(list3)
p_even(list3)
print(list3)


a=6
b=7
def change_bigger(a,b):
    if a > b:
        a = 0
    else:
        b = 0
    return a,b
print(a,b)
print(change_bigger(1,2))
d= change_bigger(a,b)
print(d)

list3=[3,4,5,6]
def present(_lst, element):
    if element in _lst:
        return True
    else:
        return False
print(present(list3, 1 ))
print(present(list3, 4 ))
print("yes" if present(list3, 789) else "no")


lst4=[1,2,1,7,8,1]
def repeat (_lst, element):
    counter = 0
    for x in _lst:
        if x == element:
            counter += 1
    print(counter)
repeat(lst4,1)




def even_only(_lst):
    even = []
    for i in range(len(_lst)):
        if _lst[i] % 2 == 0:
            even.append(_lst[i])
    print(even)
even_only(lst4)

def delete_from_list(_lst,element):
    for x in _lst:
        if element in _lst:
            _lst.remove(element)
    return _lst
print(delete_from_list(lst4,2))

repeat(lst4,1)






