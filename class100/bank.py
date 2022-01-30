class Bank():
    def __init__(self, withdraw, deposit, pin, balance):
        self.withdraw=withdraw
        self.deposit=deposit
        self.pin=pin
        self.balance=balance
    def start(self):
        print('Enter your pin')
    def stop(self):
        print('Collected your cash')
pnc=Bank(1000, 500, 1234, 150)
print(pnc.withdraw)
print(pnc.deposit)
print(pnc.pin)
print(pnc.balance)
