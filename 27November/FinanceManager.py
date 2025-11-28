from Transaction import Transaction


class FinanceManager:
    path = "transactions.txt"
    menu = '''
Меню:
1.Добавить доход/расход
2.Показать баланс и транзакции
3.Сохранить и выйти'''

    balance = 0
    transactions = list()

    def __init__(self):
        pass

    # здесь добавляем @ logger
    def add_transaction(self, type, amount, category):
        if type =="доход":
            self.balance += amount # обновили баланс
        elif type == "расход":
            self.balance -= amount
        else:
            print("некорректный тип")
        self.transactions.append(Transaction(type,amount,category)) #добавили в наш список транзакций новый объект



    def get_transactions(self):
        return self.transactions


    def get_balance(self):
        return self.balance

    # здесь тоже сделать логирование
    def save_data(self): # записали в файл
        with open(self.path, "w", encoding="utf-8") as file:
            file.write(f"balance:{self.balance}\n") # записали баланс в наш файл
            for i in self.transactions:
                file.write(f"{i}\n") # запись каждой транзации на отдельной строке



    def load_data(self): # отвечает за загрузку данных
        try:
            with open(self.path, "r",encoding = "utf-8") as file:
                contents = file.readlines() #читает строки из файла делает из них список
                self.balance = int(contents[0].split(":")[1]) # изначально баланс это строка, 1 по индексу эл. это бал
                contents.pop(0)
                for i in contents:
                    values = i.split((","))
                    self.transactions.append(Transaction(values[0],values[1],values[2]))

        except FileNotFoundError as ex:
            print("файл не найден")




    def read(self):




    def write(self):
        pass





    def run(self):
        while True:
            print("Меню\n 1. Добавить доход/расход\n 2. Показать баланс и транзакции\n 3. Сохранить и выйти")
            action = input("Введите номер операции:")
            if action == "1":
                self.add_transaction()

            elif action == "2":




if __name__ == '__main__':
    fm = FinanceManager()
    fm.run()





