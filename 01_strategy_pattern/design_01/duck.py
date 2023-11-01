#!/usr/bin/env pyuthon


from abc import ABC, abstractmethod
from _fly_behavior import (
    IFlyBehavior,
    RegularFlying,
    NoFlying,
    JetPackFlying,
)
from _quack_behavior import (
    IQuackBehavior,
    RegularQuacking,
    NoQuacking,
    SqueakQuacking,
)


class Duck(ABC):
    def __init__(
        self,
        fly_behavior: IFlyBehavior = None,
        quack_behavior: IQuackBehavior = None,
    ):
        self._fly_behavior: IFlyBehavior = fly_behavior
        self._quack_behavior: IQuackBehavior = quack_behavior

    @property
    def fly_behavior(self):
        return self._fly_behavior
    
    @property
    def quack_behavior(self):
        return self._quack_behavior

    @abstractmethod
    def display(self) -> None:
        ...

    def set_fly_behavior(self, fly_behavior: IFlyBehavior) -> None:
        if not isinstance(fly_behavior, IFlyBehavior):
            raise TypeError(
                "The argument passed to 'fly_behavior' must be of "
                "type 'IFlyBehavior'."
            )
        self._fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior: IQuackBehavior) -> None:
        if not isinstance(quack_behavior, IQuackBehavior):
            raise TypeError(
                "The argument passed to 'quack_behavior' must be of "
                "type 'IQuackBehavior'."
            )
        self._quack_behavior = quack_behavior

    def fly(self):
        self._fly_behavior.fly()

    def quack(self):
        self._quack_behavior.quack()


class MallardDuck(Duck):
    def __init__(
        self,
        fly_behavior: IFlyBehavior = None,
        quack_behavior: IQuackBehavior = None,
    ):
        super().__init__(fly_behavior, quack_behavior)

    def display(self) -> None:
        print("I am a Mallard duck!")


class RubberDuck(Duck):
    def __init__(
        self,
        fly_behavior: IFlyBehavior = None,
        quack_behavior: IQuackBehavior = None,
    ):
        super().__init__(fly_behavior, quack_behavior)

    def display(self) -> None:
        print("I am a rubber duck!")


class DecoyDuck(Duck):
    def __init__(
        self,
        fly_behavior: IFlyBehavior = None,
        quack_behavior: IQuackBehavior = None,
    ):
        super().__init__(fly_behavior, quack_behavior)

    def display(self) -> None:
        print("I am a decoy duck!")