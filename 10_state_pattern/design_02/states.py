#!/usr/bin/env python


"""
A better approach to solve the problem is to encapsulate each state in its 
own class. We can then delegate to the current state object when an action is 
required. This approach allows us to localize the behavior associated with 
each state of the machine to a particular class.
"""


from __future__ import annotations
import random
from typing import Protocol, runtime_checkable, TYPE_CHECKING


if TYPE_CHECKING:
    from gumball_machine import GumballMachine


@runtime_checkable
class State(Protocol):
    """The interface for each state class."""
    def __init__(self, gumball_machine: GumballMachine):
        ...

    def insert_quarter(self) -> None:
        ...

    def eject_quarter(self) -> None:
        ...

    def turn_crank(self) -> None:
        ...

    def _dispense_gumball(self) -> None:
        ...

    def refill_gumballs(self, number_of_gumballs: int) -> None:
        ...


class NoQuarterState:
    def __init__(self, gumball_machine: GumballMachine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print("Your quarter is accepted!")
        self.gumball_machine.set_state(
            self.gumball_machine._has_quarter_state
        )

    def eject_quarter(self) -> None:
        print("No! You have not inserted a quarter yet.")

    def turn_crank(self) -> None:
        print("No! You have not inserted a quarter yet.")

    def _dispense_gumball(self) -> None:
        print("No! You have not inserted a quarter yet.")

    def refill_gumballs(self, number_of_gumballs: int) -> None:
        print("Refilling gumballs!")
        self.gumball_machine.number_of_gumballs += number_of_gumballs


class HasQuarterState:
    def __init__(self, gumball_machine: GumballMachine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print("No! You cannot insert a quarter twice.")

    def eject_quarter(self) -> None:
        print("Your quarter is being ejected!")
        self.gumball_machine.set_state(
            self.gumball_machine._no_quarter_state
        )

    def turn_crank(self) -> None:
        print("You will get a gumball!")
        if random.randint(1, 10) == 5:
            self.gumball_machine.set_state(
                self.gumball_machine._winner_state
            )
        else:
            self.gumball_machine.set_state(
                self.gumball_machine._sold_gumball_state
            )

    def _dispense_gumball(self) -> None:
        print("No! You must turn the crank to get a gumball.")

    def refill_gumballs(self, number_of_gumballs: int) -> None:
        print("Cannot refill gumballs while holding a quarter!")


class SoldGumballState:
    def __init__(self, gumball_machine: GumballMachine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print("No! You are already getting a gumball.")

    def eject_quarter(self) -> None:
        print("No! You are already getting a gumball.")

    def turn_crank(self) -> None:
        print("No! You are already getting a gumball.")

    def _dispense_gumball(self) -> None:
        print("Dispensing a gumball!")
        self.gumball_machine.release_gumball()
        if self.gumball_machine.number_of_gumballs > 0:
            self.gumball_machine.set_state(
                self.gumball_machine._no_quarter_state
            )
        else:
            self.gumball_machine.set_state(
                self.gumball_machine._sold_out_state
            )

    def refill_gumballs(self, number_of_gumballs: int) -> None:
        print("Cannot refill gumballs while selling a gumball!")


class SoldOutState:
    def __init__(self, gumball_machine: GumballMachine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print("Sold out! Gumballs are no longer available.")

    def eject_quarter(self) -> None:
        print("Sold out! Gumballs are no longer available.")

    def turn_crank(self) -> None:
        print("Sold out! Gumballs are no longer available.")

    def _dispense_gumball(self) -> None:
        print("Sold out! Gumballs are no longer available.")

    def refill_gumballs(self, number_of_gumballs: int) -> None:
        print("Refilling gumballs!")
        self.gumball_machine.number_of_gumballs += number_of_gumballs
        self.gumball_machine.set_state(
            self.gumball_machine._no_quarter_state
        )


class WinnerState:
    def __init__(self, gumball_machine: GumballMachine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print("No! You are already getting two gumballs.")

    def eject_quarter(self) -> None:
        print("No! You are already getting two gumballs.")

    def turn_crank(self) -> None:
        print("No! You are already getting two gumballs.")

    def _dispense_gumball(self) -> None:
        print("Dispensing a gumball!")
        self.gumball_machine.release_gumball()
        if self.gumball_machine.number_of_gumballs > 0:
            print("You are getting a second gumball!")
            self.gumball_machine.release_gumball()

        if self.gumball_machine.number_of_gumballs > 0:
            self.gumball_machine.set_state(
                self.gumball_machine._no_quarter_state
            )
        else:
            self.gumball_machine.set_state(
                self.gumball_machine._sold_out_state
            )

    def refill_gumballs(self, number_of_gumballs: int) -> None:
        print("Cannot refill gumballs while selling a gumball!")