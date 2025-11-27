from Transaction import Transaction


class FinanceManager:
    path = "transactions.txt"
    balance = 0
    transactions = []

    def __init__(self):
        pass


    def add_transaction(self, type, amount, category):

        try:
            if isinstance(amount,int) and amount > 0:
                transaction = Transaction(type, amount, category)
                self.transactions.append(transaction)
                if type == "доход":
                    self.balance += amount
        except:
            raise ValueError


    def get_transactions(self):
        return self.transactions


    def get_balance(self):
        return self.balance


    def save_data(self): # записали в файл
        with open(self.path, "w", encoding="utf-8") as file:
            contents = file.write(f"balance:{self.balance}\n")
            for i in self.transactions:
                file.write(f"{i}\n")



    def load_data(self):
        try:
            with open(self.path, "r",encoding = "utf-8") as file:
            contents = file.readlines()
            self.__balance = contents[0].split("")[1]
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





