#Create accounts,deposit and withdraw funds,transferring funds and viewing details

class Bank:
    def __init__(self, account_number, intial_balance = str(input("Enter your acc num:")), name = str(input("Enter your name:")), ):
        self.account_number = account_number #initialiazing the attribute
        self.name = name
        self.balance = intial_balance 
    def __str__(self):
        pass
class deposit_money(Bank):
    def __init__(self, amount = int(input("How much will you like to deposit?"))):
        super().__init__() #calling the parent class
        self.amount = amount 
    def deposit(self):
        self.initial_balance += self.amount #Incrementing the balance
        return f'your balance is {self.initial_balance}'
class withdrawal(Bank):
    def __init__(self, enter_amount=int(input("Enter the amount to withdraw:"))):
        super().__init__() #Calling the parent class
        self.enter_amount = enter_amount #Initializing the attribute
    def withdraw_money(self):
        if self.initial_balance >= self.enter_amount:
            money = self.initial_balance - self.enter_amount
            return f'you have withdrawn{self.enter_amount}, your balance is {money}'
        else :
            return f'not enough money in your account.'
class transferred(Bank):
    def __init__(self, how_much=int(input("how much will you like to transfer?"))):
        super().__init__()
        self.how_much = how_much
    def transfer_money(self):
        if self.initial_balance >= self.how_much : #stating the condition if available balance is up to the requested money
            transferred_money = self.initial_balance - self.how_much #Deduct if the code passes and store it in the variable transferred_money
            return f"{transferred_money} has beentransferred from {self.name}'s account."

balance = deposit_money()       
print(balance.deposit())

withdraw = withdrawal(2000)
print(withdraw.withdraw_money())

transfer = transferred()
print(transfer.transfer_money)
