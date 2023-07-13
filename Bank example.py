'''
Bank:
    -create client(name,age,gender)
    -deposit
    -withdraw
    -show details
'''
class User:
    def __init__(self,name,age,gender):
        print(f'Welcome{name}')
        self.name=name
        self.age=age
        self.gender=gender
        
    def show_details(self):
        print(f'Name:{self.name}')
        print(f'Age:{self.age}')
        print(f'Gender:{self.gender}')
        print(f'Balance:{self.balance}')
         

class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance=0
        
    def deposit(self,amount):
        self.balance+=amount
        print(f"your current balance:{self.balance}")

    def withdraw(self,amount):
        if self.balance<amount:
            print(f'insuffecient balance:{self.balance}')
            return
        
        self.balance-=amount
        print(f"your current balance:{self.balance}")


c1=Bank('Ali',30,'Male')
c1.deposit(500)
c1.deposit(1000)
c1.withdraw(800)
c1.withdraw(1000)
c1.show_details()
