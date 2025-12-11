class BankAccount:
    def __init__ (self,owner_name,balance=0):
        self.owner_name= owner_name
        self.balance= balance
        
   def deposit(self, amount):
        if amount <= 0:
            print(" Amount must be positive!")
            return
       balance += amount
       print (f' the new balance account is {balance} with deposit of {amount}')
   def withdraw(self,amount):
        if amount <= 0:
            print(" Amount must be positive!")
            return
        if amount > self.balance:
            print(" Insufficient balance.")
            return
        balance -= amount
        print (f' the new balance account is {balance} with withdraw of {amount}')
    def display(self):
        print (f" owner's name{self.owner_name} , deposit {amount} , withdraw {amount} , balance{ self.balance}")
    
    
    
account = BankAccount("Meryem" , 2000)
account.deposit (500)
account.withdraw(200)
account.display ()