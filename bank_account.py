#1. Create a class named BankAccount.
#2. Add a constructor that sets the account owner's name and starting balance.
#3. Add a deposit method that increases the balance.
#4. Add a withdraw method that decreases the balance (only if balance is enough).
#5. Add a display method to show the owner's name and current balance.
#6. Create an object of the class (an account).
#7. Call the methods using the object to deposit, withdraw, and display information.



class BankAccount:
    def __init__(self, owner_name, balance=0):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive!")
            return
        self.balance += amount
        print(f'The new balance is {self.balance} with a deposit of {amount}')

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        print(f'The new balance is {self.balance} with a withdrawal of {amount}')

    def display(self):
        print(f"Owner's name: {self.owner_name}, Balance: {self.balance}")

acc= BankAccount("Rahmet", 3000)
acc.deposit(1000)
acc.withdraw(500)
acc.display()
