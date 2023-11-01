#!/usr/bin/env python


from typing import Protocol, runtime_checkable


@runtime_checkable
class Turkey(Protocol):
    def gobble(self) -> None:
        ...

    def fly(self) -> None:
        ...