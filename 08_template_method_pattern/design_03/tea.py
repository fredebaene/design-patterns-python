#!/usr/bin/env python


from caffein_beverage import CaffeineBeverage


class Tea(CaffeineBeverage):
    def add_condiments(self) -> None:
        print("Adding lemon...")

    def brew(self) -> None:
        print("Steeping tea bag...")