# def copy_file(file_to_read,file_to_write):
#     with open(file_to_read, "r") as file:
#         new_file = file.read()
#         with open(file_to_write, "w") as file:
#             file.write(new_file)


# def copy_f(path):
#     with open(path,"r",encoding="utf-8") as file:
#         text = file.read()
#     with open(path)



# path = "f1.txt"
# path.rfind(".")
# print(path)

Bad_words = ("ой", "уй")
def delete_bad(file_path):
    with open(file_path,"r") as file:
        contents = file.readlines()
        for index in range(len(contents)):
            if contents[index] in Bad_words:
                contents.pop(index)
        return contents




# открыли файл
# r+

