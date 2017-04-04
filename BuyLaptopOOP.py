''' Assumptions made : All laptops have Manufacturer name .
                     Gaming are expensive than'''
class Laptop(object):
    def __init__(self,name):

        self.name = name

class Gaminglaptop(Laptop):
     def BuyLaptop(self, amount):
        if amount < 0:
            return "invalid amount"
        if amount >=0 and amount <=50000:
            return "we Currently do have the Laptop that fits that amount"
        if amount >= 50000 and amount <= 70000:
            return "you can buy a Core i3 660M "
        elif amount >=70000 and  amount <= 85000:
            return "you can buy a Core i3 760M"
        elif amount > 100000:
            return "you can customized your laptop specs"

class Normallaptop(Laptop):
     def __init__(self,amount):

        self.Amount =Amount
     def BuyLaptop(self, amount):
        if amount <0:
             return "invalid amount"
        if amount >=0 and amount <=50000:
            return "we Currently do have the Laptop that fits that amount"
        if amount >= 50000 and amount <= 70000:
            return "you can buy a Core i5 8gb RAM "
        elif amount >=70000 and  amount <= 85000:
            return "you can buy a Core i7 4th Gen 16gb   RAM"
        elif amount > 10000:
            return "you can customized your laptop specs"


Laptop("HP")

i = Gaminglaptop("hp")

print (i.BuyLaptop(70000))