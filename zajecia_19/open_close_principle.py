from abc import ABC, abstractmethod

# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def discount_item(self, discount_type):
#         if discount_type == "christmas":
#             self.price = self.price * 0.8
#         elif discount_type == "black_friday":
#             self.price = self.price * 0.7
#         elif discount_type == "clearance":
#             self.price = self.price * 0.5
#         else:
#             print("Unknown discount type")

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self):
        pass

class ChristmasDiscount(DiscountStrategy):
    def apply_discount(self):
        return 0.8


class BlackFridayDiscount(DiscountStrategy):
    def apply_discount(self):
        return 0.7

class ClearanceDiscount(DiscountStrategy):
    def apply_discount(self):
        return 0.5


class Item:
    def __init__(self, name, price, discount_strategy: DiscountStrategy):
        self.name = name
        self.price = price
        self.discount_strategy = discount_strategy

    def discount_item(self):
        self.price = self.price * self.discount_strategy.apply_discount()