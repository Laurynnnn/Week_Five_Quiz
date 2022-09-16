class BankAccount:
    def __init__(self, account_number, balance, owner, type):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.type = type
        
    def __repr__(self):
        return f"account_number: {self.account_number} \n Balance: {self.balance} \n Owner: {self.owner} \
         \n type: {self.type}"
         
    # def details():
    #     Details = []
    #     account_number = input("Please enter account number: ")
    #     # self.balance = Details[
        

    
         
class Bank:

    def __init__(self, name, accounts):
        self.name = name
        self.accounts = accounts
           
        
    def __repr__(self):
        return f"Name: {self.name}"
    
    def adding_account(self, account):
        self.accounts.append(account)
         
class Customer:
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = accounts
         
        
    def __repr__(self):
        return f"Name: {self.name}"
    
    def adding_account(self, account):
        self.accounts.append(account)
    
class Transactions:
    def __init__(self, account, amount, type):
        self.name = name
        self.accounts = accounts
        self.amount = amount
        self.type = type
    
    def transaction(self):
        self.type = input("Enter d or D for deposit, w or W for withdraw, c or C to check balance: ")
        if self.type == "d" or "D" :
            amount == float(input("How much? ")) 
            self.account.balance = self.account.balance + amount
        elif self.type ==   "w" or "W" :
            amount = float(input("How much? "))
            self.account.balance = self.account.balance + amount
        elif self.type ==  "c" or "C" :
            print(self.account.balance)
        elif self.type == "z" or "Z":
            exit()
        else:
            print("Invalid choice. Enter right option.")
            self.type = input("Enter d or D for deposit, w or W for withdraw, c or C to check balance: ")

#creating objects
bank = Bank("Centenary", [])
customer = Customer("Lauryn", [])
account = BankAccount("CT00000000034", 20000.0, "Lauryn", "Ordinary")

#adding bank account object to bank and customer
bank.adding_account(account)
customer.adding_account(account)


print(bank)
print(customer)

#transaction object
transaction = Transactions(account, amount, type)
