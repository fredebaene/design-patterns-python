#!/usr/bin/env python


from states import (
    State,
    NoQuarterState,
    HasQuarterState,
)


class GumballMachine:
    def __init__(self, number_of_gumballs: int = 0):
        self.number_of_gumballs = number_of_gumballs
        if self.number_of_gumballs > 0:
            self.machine_state = NoQuarterState(self)

    def insert_quarter(self) -> None:
        self.machine_state.insert_quarter()

    def eject_quarter(self) -> None:
        self.machine_state.eject_quarter()

    def turn_crank(self) -> None:
        self.machine_state.turn_crank()
        self.machine_state._dispense_gumball()

    def set_state(self, machine_state: State) -> None:
        self.machine_state = machine_state(self)

    def release_gumball(self) -> None:
        self.number_of_gumballs -= 1