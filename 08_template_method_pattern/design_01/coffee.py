#!/usr/bin/env python


class Coffee:
    def prepare_recipe(self) -> None:
        self.boil_water()
        self.brew_coffee_grinds()
        self.pour_in_cup()
        self.add_sugar_and_milk()

    def boil_water(self) -> None:
        print("Boiling water...")

    def brew_coffee_grinds(self) -> None:
        print("Brewing coffee grinds...")

    def pour_in_cup(self) -> None:
        print("Pouring in cup...")

    def add_sugar_and_milk(self) -> None:
        print("Adding sugar and milk...")