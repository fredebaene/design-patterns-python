#!/usr/bin/env python


"""
For every beverage, there is a specific class, i.e., there is a class for 
espresso, for decaf, etc. However, it is also possible to order condiments 
with each beverage, such as whipped milk, soy, chocolate, etc. We could create 
a class for every beverage without and with a combination of one or more 
condiments. However, this will lead to a class explosion. Imagine, for 
espresso we would need the following classes:

- EspressoWithWhip
- EspressoWithSoy
- EspressoWithSteamedMilk
- EspressoWithChocolate
- EspressoWithSoyChocolate
- ...

Each of the subclasses extending the Beverage base class implements its own 
cost() method. This class explosion is not manageable neither maintainable.

To avoid this problem, let's define the base class with instance variables 
indicating whether or not condiments are required by the customer.
"""


from abc import ABC, abstractmethod


class Beverage(ABC):
    def __init__(self, description: str = "Beverage"):
        self.description: str = description
        self.milk: bool = False
        self.soy: bool = False
        self.mocha: bool = False
        self.whip: bool = False

    def get_description(self):
        return self.description
    
    def toggle_milk(self) -> None:
        self.milk = False if self.milk else True

    def toggle_soy(self) -> None:
        self.soy = False if self.soy else True

    def toggle_mocha(self) -> None:
        self.mocha = False if self.mocha else True

    def toggle_whip(self) -> None:
        self.whip = False if self.whip else True
    
    def cost(self) -> float:
        cost = 0.0
        if self.milk:
            cost += 0.30
        if self.soy:
            cost += 0.30
        if self.mocha:
            cost += 0.50
        if self.whip:
            cost += 0.50
        return cost


class HouseBlend(Beverage):
    def __init__(self):
        super().__init__("Most Excellent House Blend")

    def cost(self) -> float:
        cost = super().cost()
        cost += 3.50
        return cost
    

class DarkRoast(Beverage):
    def __init__(self):
        super().__init__("Most Excellent Dark Roast")

    def cost(self) -> float:
        cost = super().cost()
        cost += 4.20
        return cost
    

class Decaf(Beverage):
    def __init__(self):
        super().__init__("Most Excellent Decaf")

    def cost(self) -> float:
        cost = super().cost()
        cost += 2.50
        return cost
    

class Espresso(Beverage):
    def __init__(self):
        super().__init__("Most Excellent Espresso")

    def cost(self) -> float:
        cost = super().cost()
        cost += 2.50
        return cost


if __name__ == "__main__":
    espresso = Espresso()
    espresso.toggle_milk()
    espresso.toggle_whip()
    print(espresso.get_description())
    print(espresso.cost())