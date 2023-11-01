#!/usr/bin/env python


from typing import Protocol, runtime_checkable


@runtime_checkable
class Duck(Protocol):
    def quack(self) -> None:
        ...

    def fly(self) -> None:
        ...