class Wallet:

    def __init__(self, amount):
        self.amount = amount

    
    def __str__(self):
        return f"Wallet with Amount {self.amount}"
    
    def __add__(self, other):
        return Wallet(self.amount + other.amount)
    

my_wallet = Wallet(30)

other_wallet = Wallet(50)


wallet_account = my_wallet + other_wallet
print(wallet_account)