#!/usr/bin/env python


from caffein_beverage import CaffeineBeverage


class Tea(CaffeineBeverage):
    def prepare_recipe(self) -> None:
        self.boil_water()
        self.steep_tea_bag()
        self.pour_in_cup()
        self.add_lemon()

    def steep_tea_bag(self) -> None:
        print("Steeping tea bag...")

    def add_lemon(self) -> None:
        print("Adding lemon...")


if __name__ == "__main__":
    tea: Tea = Tea()
    tea.prepare_recipe()