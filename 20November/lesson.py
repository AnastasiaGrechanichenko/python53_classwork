with open("st.txt", "r") as file:
    contents = file.readlines()# формируется список
    print(len(contents))
    for i in contents:
        print(i,end="")
with open("st.txt","a") as file:# a - это дозапись, \n делаем с новой строки
    file.write("\nhello work")