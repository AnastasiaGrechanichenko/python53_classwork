class Transaction:
    def __init__(self,type,amount,category):
        self.type = type
        self.amount = amount
        self.category = category

# необходимо добавить логгер

    def __str__(self):
        return f"{self.__type},{self.__amount},{self.__category}"
