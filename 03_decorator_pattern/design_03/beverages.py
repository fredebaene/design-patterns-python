#!/usr/bin/env python


from beverage import Beverage, Size


class HouseBlend(Beverage):
    def __init__(self, size: Size):
        super().__init__(size, "Most Excellent House Blend")

    def cost(self) -> float:
        if self.size == Size.SMALL:
            return 2.80
        elif self.size == Size.MEDIUM:
            return 3.20
        elif self.size == Size.LARGE:
            return 3.50
    

class DarkRoast(Beverage):
    def __init__(self, size: Size):
        super().__init__(size, "Most Excellent Dark Roast")

    def cost(self) -> float:
        if self.size == Size.SMALL:
            return 3.80
        elif self.size == Size.MEDIUM:
            return 4.20
        elif self.size == Size.LARGE:
            return 4.50
    

class Decaf(Beverage):
    def __init__(self, size: Size):
        super().__init__(size, "Most Excellent Decaf")

    def cost(self) -> float:
        if self.size == Size.SMALL:
            return 2.30
        elif self.size == Size.MEDIUM:
            return 2.50
        elif self.size == Size.LARGE:
            return 2.80
    

class Espresso(Beverage):
    def __init__(self, size: Size):
        super().__init__(size, "Most Excellent Espresso")

    def cost(self) -> float:
        if self.size == Size.SMALL:
            return 2.30
        elif self.size == Size.MEDIUM:
            return 2.50
        elif self.size == Size.LARGE:
            return 2.80
    