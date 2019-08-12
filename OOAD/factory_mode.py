from abc import ABC, abstractmethod

class Pizza(ABC):
    def __init__(self, dough, sauce, cheese):
        self.dough = dough
        self.sauce = sauce
        self.cheese = cheese

class Dough(ABC):
    def __init__(self, cost):
        self.cost = cost
class Sauce(ABC):
    def __init__(self, cost):
        self.cost = cost
class Cheese(ABC):
    def __init__(self, cost):
        self.cost = cost


class ThickCrustDough(Dough):
    def __init__(self, cost):
        super(ThickCrustDough, self).__init__(cost)
class ThinCrustDough(Dough):
    def __init__(self, cost):
        super(ThickCrustDough, self).__init__(cost)

class PlumTomatoSauce(Sauce):
    def __init__(self, cost):
        super(PlumTomatoSauce, self).__init__(cost)
class MarinaraSauce(Sauce):
    def __init__(self, cost):
        super(MarinaraSauce, self).__init__(cost)

class MozzarellaCheese(Cheese):
    def __init__(self, cost):
        super(MozzarellaCheese, self).__init__(cost)
class ReggianoCheese(Cheese):
    def __init__(self, cost):
        super(ReggianoCheese, self).__init__(cost)

class IngredientFactory(ABC):
    @abstractmethod
    def create_daugh(dough):
        raise NotImplementedError
    @abstractmethod
    def create_sauce(sauce):
        raise NotImplementedError
    @abstractmethod
    def create_cheese(cheese):
        raise NotImplementedError

class NYIngredientFactory(IngredientFactory):
    def create_daugh(self, name):
        if name == 'ThickCrustDough':
            return ThickCrustDough(8)
        elif name == 'ThinCrustDough':
            return ThinCrustDough(4)
    # def create_sauce(self, name):
    #     if name == 
class PizzaStore(ABC):
    def __init__(self, ingredientfactory):
        self.ingredientfactory = InterruptedError