# Decorator/alldecorators/Pizzaria.py
# Pizzaria example using decorators

class Pizza:
    def getDescription(self):
        return self.__class__.__name__
    def getTotalCost(self):
        return self.__class__.cost

class Bandeja(Pizza):
    cost = 0.0

class Decorator(Pizza):
    def __init__(self, pizza):
        self.component = pizza
    def getTotalCost(self):
        return self.component.getTotalCost() + Pizza.getTotalCost(self)
    def getDescription(self):
        return self.component.getDescription() + ' ' +Pizza.getDescription(self)

class Calabresa(Decorator):
    cost = 15.00
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        
class Cebola(Decorator):
    cost = 5.00
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Mucarela(Decorator):
    cost = 10.00
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Catupiry(Decorator):
    cost = 20.00
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Atum(Decorator):
    cost = 20.00
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Chocolate(Decorator):
    cost = 30.00
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

calabresa = Calabresa(Mucarela(Cebola((Bandeja()))))
print(calabresa.getDescription()+ ": $" + str(calabresa.getTotalCost()))
moda = Atum(Mucarela(Catupiry( Calabresa(Cebola(Bandeja())))))
print(moda.getDescription()+ ": $" + str(moda.getTotalCost()))