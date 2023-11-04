#!/usr/bin/env python


from enum import Enum


MachineState = Enum(
    "MachineState",
    ["NO_QUARTER", "HAS_QUARTER", "SOLD_GUMBALL", "SOLD_OUT"]
)


class GumballMachine:
    def __init__(self, number_of_gumballs: int = 0):
        if not isinstance(number_of_gumballs, int):
            raise TypeError
        if not number_of_gumballs > 0:
            raise ValueError

        self.number_of_gumballs = number_of_gumballs
        if self.number_of_gumballs == 0:
            self.machine_state = MachineState.SOLD_OUT
        else:
            self.machine_state = MachineState.NO_QUARTER

    def insert_gumballs(self, number_of_gumballs: int) -> None:
        """Insert gumballs in the machine to be sold."""
        if not isinstance(number_of_gumballs, int):
            raise TypeError
        if not number_of_gumballs > 0:
            raise ValueError

        self.number_of_gumballs += number_of_gumballs
        self.machine_state = MachineState.NO_QUARTER

    def insert_quarter(self) -> None:
        """The behavior of the machine when a quarter is inserted."""
        if self.machine_state == MachineState.NO_QUARTER:
            print("Your quarter is accepted!")
            self.machine_state = MachineState.HAS_QUARTER

        elif self.machine_state == MachineState.HAS_QUARTER:
            print("No! You cannot insert a quarter twice.")

        elif self.machine_state == MachineState.SOLD_GUMBALL:
            print("No! First, you will get a gumball.")

        elif self.machine_state == MachineState.SOLD_OUT:
            print("No! There are no more gumballs.")

    def eject_quarter(self) -> None:
        """The behavior of the machine when a quarter is ejected."""
        if self.machine_state == MachineState.NO_QUARTER:
            print("No! There is no quarter to eject.")

        elif self.machine_state == MachineState.HAS_QUARTER:
            print("Your quarter is being ejected!")
            self.machine_state = MachineState.NO_QUARTER

        elif self.machine_state == MachineState.SOLD_GUMBALL:
            print("No! You are already getting a gumball.")

        elif self.machine_state == MachineState.SOLD_OUT:
            print("No! Quarters are no longer accepted.")

    def turn_crank(self) -> None:
        """The behavior of the machine when the crank is turned."""
        if self.machine_state == MachineState.NO_QUARTER:
            print("No! You have not inserted a quarter yet.")

        elif self.machine_state == MachineState.HAS_QUARTER:
            print("You will get a gumball.")
            self.machine_state = MachineState.SOLD_GUMBALL
            self._dispense_gumball()

        elif self.machine_state == MachineState.SOLD_GUMBALL:
            print("No! You are already getting a gumball.")

        elif self.machine_state == MachineState.SOLD_OUT:
            print("No! There are no more gumballs left.")

    def _dispense_gumball(self) -> None:
        """The behavior of the machine when dispensing a gumball."""
        if self.machine_state == MachineState.NO_QUARTER:
            print("No! You have not inserted a quarter yet.")

        elif self.machine_state == MachineState.HAS_QUARTER:
            print("No! You are getting a gumball.")

        elif self.machine_state == MachineState.SOLD_GUMBALL:
            print("I am now dispensing a gumball.")
            self.number_of_gumballs -= 1
            if self.number_of_gumballs == 0:
                self.machine_state = MachineState.SOLD_OUT
            else:
                self.machine_state = MachineState.NO_QUARTER

        elif self.machine_state == MachineState.SOLD_OUT:
            print("No! There are no more gumballs.")