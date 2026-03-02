class ShoppingCart:
    def __init__(self):
        # This is just a normal list of item prices in the cart
        self._prices = [10, 25, 5]

    @property
    def price(self):
        return sum(self._prices)

    @price.setter
    def price(self, new_data):
        if type(new_data) == list:
            self._prices = new_data
        else:
            print("Error I only accepts list")


my_shopping_cart = ShoppingCart()
print("Starting total:", my_shopping_cart.price)

my_shopping_cart.price = [100, 200]
print("After Setter price:", my_shopping_cart.price)


my_shopping_cart.price = "I am a hacker!"

# class Shop:
#     total_shops_opened = 0

#     def __init__(self, cafe_name):
#         self.name = cafe_name
        
#         ### 1. THE SAFE: We add an underscore to lock it in the back room
#         self._stock = {} 
#         Shop.total_shops_opened += 1

#     ### 2. THE TELLER: We create the read-only window. 
#     ### (Notice we deleted the old get_data() method entirely!)
#     @property
#     def stock(self):
#         return self._stock

#     def unpack_delivery(self, delivery_list: list):
#         for delivery in delivery_list:
#             item = delivery["item"]
#             qty = delivery.get("qty",0)
            
#             ### CHANGED: Internal methods must now use the locked _stock safe
#             self._stock[item] = self._stock.get(item,0) + qty

#     def __str__(self):
#         ### CHANGED: Internal methods must now use the locked _stock safe
#         return f"Shop: {self.name} | Total unique items: {len(self._stock)}"

# # ---------------------------------------------------------
# # EVERYTHING BELOW THIS LINE STAYS EXACTLY THE SAME!
# # ---------------------------------------------------------

# class TechShop(Shop):
#     def run_diagnostics(self):
#         print("Running computer diagnostics...")
#         print(self.name)

# class GroceryStore(Shop):
#     def __init__(self, cafe_name, has_bakery:bool):
#         super().__init__(cafe_name)
#         self.has_bakery = has_bakery

# truck_delivery = [
#     {"item": "coffee_beans", "qty": 50},
#     {"item": "milk", "qty": 20},
#     {"item": "sugar"},                   
#     {"item": "coffee_beans", "qty": 30}
# ]

# bakery_truck_delivery = [
#     {"item": "paw", "qty": 50},
#     {"item": "milk", "qty": 20},
#     {"item": "cake","qty":10},
#     {"item":"soda"}
# ]

# obj = Shop("SHANKAR Inventory")
# obj.unpack_delivery(truck_delivery)

# tech_obj = TechShop("Maruti Tech")
# tech_obj.run_diagnostics()

# grosery = GroceryStore("shreeRam", True)
# grosery.unpack_delivery(bakery_truck_delivery)

# print(obj, end="\n")
# print(tech_obj, end="\n")
# print(grosery, end="\n")

# print(f"Total Shop is : {Shop.total_shops_opened}")

# # =========================================================
# # THE HACKER TEST (Add this to the very bottom of your file!)
# # =========================================================
# print("\n--- Testing the Security ---")
# print("Reading stock is allowed:", obj.stock) # The Teller allows this!

# print("Trying to ruin the stock...")
# obj.stock = "I ruined your dictionary!" # 💥 Python will crash right here!