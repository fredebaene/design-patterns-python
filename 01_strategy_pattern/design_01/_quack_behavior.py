#!/usr/bin/env python


from typing import Protocol, runtime_checkable


@runtime_checkable
class IQuackBehavior(Protocol):
    def quack(self) -> None:
        ...


class RegularQuacking:
    def quack(self) -> None:
        print("I am quacking!")


class NoQuacking:
    def quack(self) -> None:
        print("I cannot quack!")


class SqueakQuacking:
    def quack(self) -> None:
        print("I am squeaking!")