#!/usr/bin/env python


from typing import Protocol, runtime_checkable


@runtime_checkable
class IFlyBehavior(Protocol):
    def fly(self) -> None:
        ...


class RegularFlying:
    def fly(self) -> None:
        print("I am flying with my wings!")


class NoFlying:
    def fly(self) -> None:
        print("I cannot fly!")


class JetPackFlying:
    def fly(self) -> None:
        print("I am flying with turbo jets!")