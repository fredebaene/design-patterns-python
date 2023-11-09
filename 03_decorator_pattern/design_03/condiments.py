#!/usr/bin/env python


from beverage import Beverage, Size
from condiment import BeverageCondiment


class Milk(BeverageCondiment):
    def __init__(self, beverage: Beverage):
        self.beverage: Beverage = beverage
        super().__init__(self.beverage.get_size(), "Milk")

    def get_description(self) -> str:
        return self.beverage.get_description() + "\n+ Milk"
    
    def cost(self) -> float:
        cost = self.beverage.cost()
        if self.beverage.get_size() == Size.SMALL:
            cost += 0.15
        elif self.beverage.get_size() == Size.MEDIUM:
            cost += 0.20
        elif self.beverage.get_size() == Size.LARGE:
            cost += 0.25
        return cost


class Mocha(BeverageCondiment):
    def __init__(self, beverage: Beverage):
        self.beverage: Beverage = beverage
        super().__init__(self.beverage.get_size(), "Mocha")

    def get_description(self) -> str:
        return self.beverage.get_description() + "\n+ Mocha"

    def cost(self) -> float:
        cost = self.beverage.cost()
        if self.beverage.get_size() == Size.SMALL:
            cost += 0.25
        elif self.beverage.get_size() == Size.MEDIUM:
            cost += 0.30
        elif self.beverage.get_size() == Size.LARGE:
            cost += 0.40
        return cost


class Soy(BeverageCondiment):
    def __init__(self, beverage: Beverage):
        self.beverage: Beverage = beverage
        super().__init__(self.beverage.get_size(), "Soy")

    def get_description(self) -> str:
        return self.beverage.get_description() + "\n+ Soy"
    
    def cost(self) -> float:
        cost = self.beverage.cost()
        if self.beverage.get_size() == Size.SMALL:
            cost += 0.20
        elif self.beverage.get_size() == Size.MEDIUM:
            cost += 0.25
        elif self.beverage.get_size() == Size.LARGE:
            cost += 0.30
        return cost