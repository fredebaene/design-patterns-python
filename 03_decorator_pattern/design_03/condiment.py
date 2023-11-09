#!/usr/bin/env python


from abc import abstractmethod
from beverage import Beverage, Size


class BeverageCondiment(Beverage):
    @abstractmethod
    def get_description(self) -> str:
        ...

    def set_size(self, size: Size) -> None:
        self.beverage.set_size(size)