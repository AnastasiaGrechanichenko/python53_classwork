def count_word(file_name,word):
    with (open(file_name,"r") as file): # or read (считывает в одну строку)
        contents = file.readlines()
        count = 0
        for line in contents:
            if word in line:
                count+=1
        return count
print(count_word("st.txt","privet"))

