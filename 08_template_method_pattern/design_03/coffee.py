#!/usr/bin/env python


from caffein_beverage import CaffeineBeverage


class Coffee(CaffeineBeverage):
    def add_condiments(self) -> None:
        print("Adding sugar and milk...")

    def brew(self) -> None:
        print("Brewing coffee grinds...")