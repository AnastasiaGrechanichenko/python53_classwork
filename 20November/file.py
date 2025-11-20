# def close_file(file):
#     print(file.name,"closed")
#     file.close(file)
#
#
#
file_path = "20November/st.txt"
# try:
#     file = open (file_path,"r")
#     print(file.read())
#     file.close()
# except Exception as ex:
#     print(ex)
# finally:
#


#with открывает поток, src/st.txt первое слово папка

with open(file_path,"r")as file:
    print(file.read())

 посмотреть модуль ре