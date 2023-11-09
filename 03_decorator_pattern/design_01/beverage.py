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
"""


from abc import ABC, abstractmethod


class Beverage(ABC):
    def __init__(self, description: str = "Beverage"):
        self.description: str = description

    def get_description(self) -> str:
        return self.description
    
    @abstractmethod
    def cost(self) -> float:
        ...


class HouseBlend(Beverage):
    def __init__(self):
        super().__init__("Most Excellent House Blend")

    def cost(self) -> float:
        return 3.50
    

class DarkRoast(Beverage):
    def __init__(self):
        super().__init__("Most Excellent Dark Roast")

    def cost(self) -> float:
        return 4.20
    

class Decaf(Beverage):
    def __init__(self):
        super().__init__("Most Excellent Decaf")

    def cost(self) -> float:
        return 2.50
    

class Espresso(Beverage):
    def __init__(self):
        super().__init__("Most Excellent Espresso")

    def cost(self) -> float:
        return 2.50


if __name__ == "__main__":
    espresso = Espresso()
    print(espresso.get_description())
    print(espresso.cost())