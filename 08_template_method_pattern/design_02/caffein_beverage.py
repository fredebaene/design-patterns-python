#!/usr/bin/env python


from abc import ABC


class CaffeineBeverage(ABC):
    def prepare_recipe(self) -> None:
        ...

    def boil_water(self) -> None:
        print("Boiling water...")

    def pour_in_cup(self) -> None:
        print("Pouring in cup...")