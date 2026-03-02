# from abc import ABC, abstractmethod
# from dataclasses import dataclass

# # --- CONCEPT 1: DATACLASS ---
# # CHALLENGE 1: What decorator goes here?
# @dataclass
# class Weapon:
#     name: str
#     damage: int

# # --- CONCEPT 2: ABSTRACTION ---
# class Hero(ABC):
#     @abstractmethod
#     def attack(self):
#         pass

# # --- CONCEPT 3: COMPOSITION & MRO ---
# class Warrior(Hero):
#     def __init__(self, name):
#         self.name = name
#         # CHALLENGE 2: Use Composition to assign a brand new Weapon("Axe", 50) to this variable
#         self.weapon = Weapon("Axe", 50)

#     def attack(self):
#         return f"{self.name} swings their {self.weapon.name}!"

# class Mage(Hero):
#     def attack(self):
#         return "Casts a massive fireball!"

# # Inheriting from both! (MRO will pick Warrior's attack because it is first)
# class MagicKnight(Warrior, Mage):
#     pass

# # --- CONCEPT 4: DECORATORS & MAGIC METHODS ---
# class Guild:
#     def __init__(self, name, member_count):
#         self.name = name
#         self.member_count = member_count

#     @classmethod
#     def starter_guild(cls, name):
#         # Factory method for a quick start
#         return cls(name, 1)

#     @staticmethod
#     def is_full(member_count):
#         # Utility tool
#         return member_count >= 50

#     # CHALLENGE 3: What magic method name allows us to use the '+' sign?
#     def __add__(self, other):
#         total = self.member_count + other.member_count
#         return Guild("Allied Forces", total)


# user_input = "three"
# try:
#     numb = int(user_input)

# except ValueError:
#     print("something wrong")


# print("okay")

class Treasure:
    
    def __init__(self, tresure_gold: int):
        self.tr_gold = tresure_gold

    def divide_gold(self, member: int):
            return self.tr_gold//member


tr = Treasure(100)
while True:
    try:
        number_of_member = int(input("Enter Member count:"))
        dev_count = tr.divide_gold(number_of_member)
        print(dev_count)
        break
    except ZeroDivisionError as e:
         print(e)

    except ValueError as v:
         print(v)

    finally:
         print("turning off...")




