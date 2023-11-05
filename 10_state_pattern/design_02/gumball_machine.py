#!/usr/bin/env python


from states import (
    State,
    NoQuarterState,
    HasQuarterState,
    SoldGumballState,
    SoldOutState,
)


class GumballMachine:
    def __init__(self, number_of_gumballs: int = 0):
        err_msg = (
            "The argument passed to `number_of_gumballs` must be a "
            "non-negative integer."
        )
        if not isinstance(number_of_gumballs, int):
            raise TypeError(err_msg)
        if number_of_gumballs < 0:
            raise ValueError(err_msg)
        
        self._no_quarter_state = NoQuarterState(self)
        self._has_quarter_state = HasQuarterState(self)
        self._sold_gumball_state = SoldGumballState(self)
        self._sold_out_state = SoldOutState(self)

        self.number_of_gumballs = number_of_gumballs
        if self.number_of_gumballs > 0:
            self.machine_state = self._no_quarter_state
        else:
            self.machine_state = self._sold_out_state

    def insert_quarter(self) -> None:
        self.machine_state.insert_quarter()

    def eject_quarter(self) -> None:
        self.machine_state.eject_quarter()

    def turn_crank(self) -> None:
        self.machine_state.turn_crank()
        self.machine_state._dispense_gumball()

    def set_state(self, machine_state: State) -> None:
        self.machine_state = machine_state

    def release_gumball(self) -> None:
        self.number_of_gumballs -= 1