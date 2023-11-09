#!/usr/bin/env python


from abc import ABC, abstractmethod
from enum import Enum


Size = Enum("Size", ["SMALL", "MEDIUM", "LARGE"])


class Beverage(ABC):
    def __init__(self, size: Size, description: str = "Beverage"):
        if not isinstance(size, Size):
            raise TypeError(
                "The argument passed to 'size' must be of type 'Size'."
            )
        if not isinstance(description, str):
            raise TypeError(
                "The argument passed to 'description' must of type 'str'."
            )
        
        self.size: Size = size
        self.description: str = description

    @abstractmethod
    def cost(self) -> float:
        ...

    def get_description(self) -> str:
        return self.description
    
    def get_size(self) -> Size:
        return self.size
    
    def set_size(self, size: Size) -> None:
        self.size = size