class Transaction:
    def __init__(self, type, summ, category):
        self.type=type
        self.summ=summ
        self.category=category

    def __str__(self):
        return f"{self.type},{self.summ},{self.category}"

def logger(input_func):
    def wrapper(*args):
        print(input_func.__name__)
        input_func(*args)
    return wrapper


class FinanceManager:
    path = "transaction.txt"
    menu = '''
Меню:
1. Добавить доход/расход
2. Показать баланс и транзакции
3. Сохранить и выйти'''

    balance=0
    transactions=list()

    def __init__(self):
        pass

    @logger
    def add_transaction(self, type, summ, category):
        if type=="доход":
            self.balance+=summ
        elif type=="расход":
            self.balance -= summ
        else:
            print("некорректный тип")
            return
        self.transactions.append(Transaction(type, summ, category))

    def get_transactions(self):
        return self.transactions

    def get_balance(self):
        return self.balance

    @logger
    def save_data(self):
        with open(self.path, "w", encoding="utf-8") as file:
            file.write(f"balance:{self.balance}\n")
            for i in self.transactions:
                file.write(f"{i}\n")

    @logger
    def load_data(self):
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                contents = file.readlines()
                self.balance = int(contents[0].split(":")[1])
                contents.pop(0)
                for i in contents:
                    values = i.split((','))
                    self.transactions.append(Transaction(values[0],values[1],values[2]))
        except FileNotFoundError:
            print("файл не найден")

    def run(self):
        self.load_data()
        while True:
            print(self.menu)
            variant = input('Выберите действие: ')
            if variant=='1':
                type = input("введите тип: ")
                summ = input("введите сумму: ")
                category = input("введите кутегорию: ")
                self.add_transaction(type,summ,category)
            elif variant=='2':
                self.get_balance()
                self.get_transactions()
            elif variant=='3':
                self.save_data()
                exit()
            else:
                print('некорректные данные')

if __name__ == '__main__':
    manager = FinanceManager()
    manager.run()