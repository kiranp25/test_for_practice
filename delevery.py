class DeliveryVan:
    def __init__(self):
        self.delivery_made = 0

    def drive_to_customer(self, address):
        self.delivery_made += 1

        return f"delivery to {address}, Total Delieverys {self.delivery_made}"

class CashRegister:
    def __init__(self):
        self.total_cash =  0

    def add_money(self, price):
        self.total_cash += price
        return f"Register updated: ${self.total_cash}"

class Shop:
    def __init__(self, name):
        self.name = name
        self.register = CashRegister()
        self.delivery = DeliveryVan()

    
    def make_delivery(self, customer_address):
        return self.delivery.drive_to_customer(customer_address)
        

my_shop = Shop('Shankars Express')

print(my_shop.make_delivery("123 akash nagar, pune"))
print(my_shop.make_delivery("123 karun viar, pune"))
