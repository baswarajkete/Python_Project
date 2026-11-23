'''
15. Mini project — ATM
Create an ATM or BankAccount class with these features:
Initialize the account holder and starting balance.
Check the balance.
Deposit money.
Withdraw money only if sufficient funds are available.
Display a transaction summary.
'''

class ATM:
    def __init__(self,owner):     
        self.owner = owner
        self.balance = 0
        self.l =[]
        self.menu()


    def menu(self):
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
                self.checkbalance()
            elif user_input == 2:
                self.deposit()
            elif user_input == 3:
                self.withdraw()
            elif user_input == 4:
                self.trans_summeary()
            elif user_input == 5:
                print("Thank you")
                break
            else:
                print("Invalid input")


    def checkbalance(self):
        print("Available balance is ",self.balance)
        #self.menu()
    def deposit(self):
        while True:
            amount = int(input("Enter amount "))
            if amount >0:
                self.balance += amount
                self.l.append(f'credited {amount}')
                print("Successfully credited your amount", amount)
                break
            else:
                print("please enter positive amount")
        #self.menu()
    def withdraw(self):
        while True:
            amount = int(input("Enter amount "))
            if amount >0:
                if self.balance >=amount:
                    self.balance -= amount
                    self.l.append(f'debited {amount}')
                    print("Please collect your amount", amount)
                    break
                else:
                    print("Insufficient funds")
            else:
                print("Please enter positive amount")
    def trans_summeary(self):
        print("Account holder:", self.owner)

        if not self.l:
             print("No transactions yet")
        else:
            for i in self.l:
                 print(i)

p1 = ATM("Ram")

