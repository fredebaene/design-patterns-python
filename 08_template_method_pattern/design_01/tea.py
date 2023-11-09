#!/usr/bin/env python


class Tea:
    def prepare_recipe(self) -> None:
        self.boil_water()
        self.steep_tea_bag()
        self.pour_in_cup()
        self.add_lemon()

    def boil_water(self) -> None:
        print("Boiling water...")

    def steep_tea_bag(self) -> None:
        print("Steeping tea bag...")

    def pour_in_cup(self) -> None:
        print("Pouring in cup...")

    def add_lemon(self) -> None:
        print("Adding lemon...")