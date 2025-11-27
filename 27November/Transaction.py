class Transaction:
    def __init__(self,type,amount,category):
        self.__type = type
        self.__amount = amount
        self.__category = category

    @ property
    def type(self):
        return self.__type

    @property
    def amount(self):
        return self.__amount

    @property
    def category(self):
        return self.__category

    def __str__(self):
        return f"{self.__type},{self.__amount},{self.__category}"
