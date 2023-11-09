#!/usr/bin/env python


from caffein_beverage import CaffeineBeverage


class Coffee(CaffeineBeverage):
    def prepare_recipe(self) -> None:
        self.boil_water()
        self.brew_coffee_grinds()
        self.pour_in_cup()
        self.add_sugar_and_milk()

    def brew_coffee_grinds(self) -> None:
        print("Brewing coffee grinds...")

    def add_sugar_and_milk(self) -> None:
        print("Adding sugar and milk...")


if __name__ == "__main__":
    coffee: Coffee = Coffee()
    coffee.prepare_recipe()