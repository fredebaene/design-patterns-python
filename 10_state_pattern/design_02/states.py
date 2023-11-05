#!/usr/bin/env python


"""
A better approach to solve the problem is to encapsulate each state in its 
own class. We can then delegate to the current state object when an action is 
required. This approach allows us to localize the behavior associated with 
each state of the machine to a particular class.
"""


from __future__ import annotations
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


class NoQuarterState:
    def __init__(self, gumball_machine: GumballMachine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print("Your quarter is accepted!")
        self.gumball_machine.set_state(HasQuarterState)

    def eject_quarter(self) -> None:
        print("No! You have not inserted a quarter yet.")

    def turn_crank(self) -> None:
        print("No! You have not inserted a quarter yet.")

    def _dispense_gumball(self) -> None:
        print("No! You have not inserted a quarter yet.")


class HasQuarterState:
    def __init__(self, gumball_machine: GumballMachine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print("No! You cannot insert a quarter twice.")

    def eject_quarter(self) -> None:
        print("Your quarter is being ejected!")
        self.gumball_machine.set_state(NoQuarterState)

    def turn_crank(self) -> None:
        print("You will get a gumball!")
        self.gumball_machine.set_state(SoldGumballState)
        self.gumball_machine._dispense_gumball()

    def _dispense_gumball(self) -> None:
        print("No! You are getting a gumball.")


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
            self.gumball_machine.set_state(NoQuarterState)
        else:
            self.gumball_machine.set_state(SoldOutState)


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