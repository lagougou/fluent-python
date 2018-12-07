from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price


class Order:

    def __init__(self, customer, car, promotion=None):
        self.customer = customer
        self.car = list(car)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total=sum(item.total() for item in self.car)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

class Promotion(ABC):

    @abstractmethod
    def discount(self, order):
        """ return  the discount price (postive value)"""
    
class FidelityPromotion(Promotion):
    
    def discount(self, order):
        if order.customer.fidelity >= 1000:
            return order.total() * 0.05
        return 0

class BulkItemPromotion(Promotion):
    
    def discount(self, order):
        discount = 0
        for item in order.car:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount


class LargeOrderPromotion(Promotion):

    def discount(self, order):
        distinct_items =  { item.product for item in order.car }
        if len(distinct_items) >= 10:
            return order.total() * 0.07
        return 0



joe = Customer("Jone Doe", 0)
ann = Customer("Ann Smith", 1100)

car = [LineItem('banana', 4 ,0.5), LineItem('apple', 10, 1.5), LineItem("watermellon", 5, 5.0)]
long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
print(Order(joe,car,FidelityPromotion()))
print(Order(ann, car, FidelityPromotion()))
print(Order(joe, long_order, LargeOrderPromotion()))

global_name = [name for name in globals() if not name.startswith("__")]
print(global_name)