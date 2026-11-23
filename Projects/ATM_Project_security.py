'''
Upgrade your ATM project using encapsulation.
Make the balance a private attribute.
Prevent negative deposits and withdrawals.
Allow withdrawals only when sufficient funds exist.
Return transaction history safely.
Ensure all balance changes go through validated methods.
Test whether assigning to account.__balance changes the actual private balance.
'''
class ATM:
    def __init__(self,owner):
        self.owner = owner
        self.__balance = 0
        self.__transactions =[]
        self.__menu()


    def __menu(self):
        while True:
            user_input = int(input(
            '''
            1: checkbalance
            2: deposit
            3: withdraw
            4: trans_summeary
            5: exit

            '''
        ))


            if user_input == 1:
                self.__checkbalance()
            elif user_input == 2:
                self.__deposit()
            elif user_input == 3:
                self.__withdraw()
            elif user_input == 4:
                self.__trans_summeary()
            elif user_input == 5:
                print("Thank you")
                break
            else:
                print("Invalid input")

    def get_balance(self):
        return self.__balance

    def __checkbalance(self):
        print("Available balance is ",self.__balance)
        #self.menu()
    def __deposit(self):
        while True:
            amount = int(input("Enter amount "))
            if amount >0:
                self.__balance += amount
                self.__transactions.append(f'credited {amount}')
                print("Successfully credited your amount", amount)
                break
            else:
                print("please enter positive amount")
        #self.menu()
    def __withdraw(self):
        while True:
            amount = int(input("Enter amount "))
            if amount > 0:
                if self.__balance >=amount:
                    self.__balance -= amount
                    self.__transactions.append(f'debited {amount}')
                    print("Please collect your amount", amount)
                    break
                else:
                        print("Insufficient funds")
            else:
                print("Please enter positive amount")

    def get_transaction_history(self):
        return self.__transactions.copy()

    def __trans_summeary(self):
        print("Account holder:", self.owner)

        if not self.get_transaction_history():
             print("No transactions yet")
        else:
            for i in self.get_transaction_history():
                 print(i)



p1 = ATM("Ram")