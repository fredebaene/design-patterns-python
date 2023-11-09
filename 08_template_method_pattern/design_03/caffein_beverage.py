#!/usr/bin/env python


from abc import ABC


class CaffeineBeverage(ABC):
    def prepare_recipe(self) -> None:
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def add_condiments(self) -> None:
        ...

    def brew(self) -> None:
        ...

    def boil_water(self) -> None:
        print("Boiling water...")

    def pour_in_cup(self) -> None:
        print("Pouring in cup...")