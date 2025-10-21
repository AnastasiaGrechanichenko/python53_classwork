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
journal = []

english_marks=[90,80,70,99]

def add_subject(subject_name):
    subject_name = subject_name[:3]
    subject.append(subject_name)
    for i in journal:
        i.append(0)

def add_marks(number, subject,mark):



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




if __name__ == '__main__':
    add_subject("английский")
    add_subject("алгебра")
    add_student()

    show_journal()



