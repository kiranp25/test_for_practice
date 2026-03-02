from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    role: str
    id_number: int 

new_emp = Employee("kiran", "Admin", 1)
print(new_emp)

# 1. The Strict Boss
class Payment(ABC): 
    @abstractmethod
    def pay_bill(self, amount):
        pass


class CreditCard(Payment):
    def __init__(self):
        pass

    def pay_bill(self, amount):
        return f"Processing credit card for ${amount}"
    

pay = CreditCard()
print(f"pay wtih bill {pay.pay_bill(1000)}")