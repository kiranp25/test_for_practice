
class PizzaShop:
    def __init__(self, toppings, size):
        self.toppings = toppings
        self.size = size

    

    @staticmethod
    def is_store_open(hour):
        if hour in range(10,22):
            return True
        else:
            return False

    @classmethod
    def margherita(cls, size):
        return cls(['cheese', 'basil', 'tomato'], size)


    def __str__(self):
        return f"A {self.size} inch Pizza with {', '.join(self.toppings)}"

print("Store Opened" if PizzaShop.is_store_open(12) else "CLosed")


print(PizzaShop.margherita(12))


# class Pizza:
#     def __init__(self, toppings, radius):
#         self.toopings = toppings
#         self.radius = radius


#     @staticmethod
#     def calculate_area(r):
#         return 3.14 * r * r
    
#     @classmethod
#     def margherita(cls):
#         return cls("Cheese and Basil", 6)
        

# print("area of a 10-inch pizza", Pizza.calculate_area(10))

# my_dinner = Pizza.margherita()

# print(f"my dinner is {my_dinner.radius} inch {my_dinner.toopings} pizza!")