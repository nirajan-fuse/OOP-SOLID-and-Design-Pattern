# [Open-Closed Principle (OCP)] Download the python file from this link. Suppose we have a Product class that represents a 
# generic product, and we want to calculate the total price of a list of products. Initially, the Product class only has a 
# price attribute, and we can calculate the total price of products based on their prices.

# Now, let's say we want to add a discount feature, where some products might have a discount applied to their prices. To add 
# this feature, we would need to modify the existing Product class and the calculate_total_price function, which violates the 
# Open/Closed Principle. Redesign this program to follow the Open-Closed Principle (OCP) which represents “Software entities 
# (classes, modules, functions, etc.) should be open for extension, but closed for modification.”

from abc import abstractmethod

class Product:
    def __init__(self, price):
        self.price = price

class Discount:
    @abstractmethod
    def apply_discount(self, price):
        pass

class NoDiscount(Discount):
    def apply_discount(self, price):
        return price

class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, price):
        return price * (1 - self.percentage / 100)
        
def calculate_total_price(products, discount=NoDiscount()):
    total_price = 0
    for product in products:
        total_price += discount.apply_discount(product.price)
    return total_price

# Using the calculate_total_price function with a list of products
products = [Product(100), Product(50), Product(75)]
print("Total Price:", calculate_total_price(products))

# Applying a 20% discount
discounted_total_price = calculate_total_price(products, PercentageDiscount(20))
print("Discounted Total Price:", discounted_total_price)