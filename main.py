journal =[
    [56,67,78,67],
    [66,78,89,87],
    [90,78,89,88]
]

# print(students)
# print(students[0][2])
#
# for x in students:
#     print(*x)
#
# for x in range(len(students)):
#     for y in range (len(students[x])):
#         print(students[x][y],end = " ")
#
#
# for i in students[0]:
#     print(i,end=" ")
# # we make cycle so
# for i in students:
#     for j in i:
#         print(j,end = " ")
#     print()
#
#
# math_marks = []
# for i in range(len(students)):
#     math_marks.append(students[i][1])
#
# average = (sum(math_marks))/3
# print(average)
#
#
# print("№\t| рус\t| мат\t| лит\t| физ")
# for i in range(len(students)):
#     print(i+1, end = "\t")
#     for j in range (len(students[i])):
#         print("|",students[i][j], end ="\t")
#     print()

subjects=["рус","мат","лит", "физ"]
student_names = ["Ivanov","Petrov"]
journal = []

english_marks=[90,80,70,99]

def add_subject(subject_name):
    subject_name = subject_name[:3]
    subjects.append(subject_name)
    for i in journal:
        i.append(0)

# def add_marks(student, subject,mark):
#     journal[subject].append(mark)

def change_mark(number,subject,mark):
    index= subjects.index(subject)
    journal[number-1][index]=mark

def remove_student(index):
    journal.pop(index-1)


def delete_subject(subject):
    for i in subjects:
        subject

def add_student():
    journal.append([])

    for i in subjects:
        journal[len(journal)-1].append(0)

def show_journal():
    print("№", end = "")
    for i in subjects:
        print(f"\t| {i}", end = "")
    print()

    for i in range(len(journal)):
        print(i + 1, end="\t")
        for j in range(len(journal[i])):
            print(f"| {journal[i][j]}", end="\t")
        print()


def best_student():
    best_index = 0
    best_summa = 0
    for mark in range(len(journal)):
        if sum(journal[i])>best_summa:
            best_index=i
    return best_index


def show_menu():
    action = int(input(
        '''
        
        1. вывод журнала 
        2. добавление студента
        3. добавление дисциплины
        4. удаление студента
        5. удаление дисциплины
        6. замена оценки
        7. выйти
        '''
    ))
    match action:
        case 1: show_journal()
        case 2: add_student()
        case 3: add_subject()
            add_subject(input("введите название дисциплины: "))
        case 4: remove_student()
                remove_student(input("введите имя студента: "))
        case 6:
            number = int(input("Введите название дисциплины"))
            mark = int (input("Введите оценку"))
            change_mark(number,subject,mark)
        case 7:
            exit()
        case _: show_menu

if __name__ == '__main__':
    add_subject("английский")
    add_subject("алгебра")
    add_student()
    change_mark(2,"мат","67")
    remove_student(1)
    show_journal()



