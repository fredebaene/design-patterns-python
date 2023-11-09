#!/usr/bin/env python


from beverage import Beverage, Size
from beverages import (
    HouseBlend,
    DarkRoast,
    Decaf,
    Espresso,
)
from condiments import (
    Milk,
    Mocha,
    Soy,
)


def main() -> None:
    beverage: Beverage = Espresso(Size.LARGE)
    beverage = Milk(beverage)
    beverage = Mocha(beverage)
    beverage = Soy(beverage)
    beverage = Mocha(beverage)
    beverage.set_size(Size.MEDIUM)
    print(beverage.get_description())
    print(f"Total cost: {beverage.cost()}")


if __name__ == "__main__":
    main()