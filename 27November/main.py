from FinanceManager import FinanceManager
if __name__ == '__main__':
    finance_manager = FinanceManager(0,[])
    finance_manager.add_transaction("доход","100","зарплата")
    print(finance_manager.transactions)