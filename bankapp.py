class BankAccount:
    def __init__(self, account_number, balance, owner, type):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.type = type
        
    def __repr__(self):
        return f"account_number: {self.account_number} \n Balance: {self.balance} \n Owner: {self.owner} \
         \n type: {self.type}"
        
  
         
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
        self.account = account
        self.amount = amount
        self.type = type
    
    def make_transaction(self):
        choice = input("Enter d or D for deposit, w or W for withdraw, c or C to check balance: ")
        if choice == "d" or "D" :
            # trans == "Deposit"
            self.amount == float(input("How much? ")) 
            self.account.balance = self.account.balance + self.amount
        elif choice ==   "w" or "W" :
            # trans == "Withdraw"
            self.amount = float(input("How much? "))
            self.account.balance = self.account.balance + self.amount
        elif choice ==  "c" or "C" :
            # trans == "Balance Check"
            print(self.account.balance)
        elif choice == "z" or "Z":
            print("Exiting...")
            break
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
transaction = Transactions(account, 3000.0, "DEpo")

Transactions.make_transaction(transaction)

# transaction = Transactions(account, amount, trans)

print(transaction)
