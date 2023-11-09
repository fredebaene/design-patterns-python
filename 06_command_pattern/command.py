from typing import Protocol, runtime_checkable
from light import Light
from garage import Garage


@runtime_checkable
class ICommand(Protocol):
    def execute(self) -> None:
        ...

    def undo(self) -> None:
        ...

class NoCommand:
    def execute(self) -> None:
        raise NotImplementedError
    
    def undo(self) -> None:
        raise NotImplementedError

class LightOnCommand:
    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.switch_on()

    def undo(self) -> None:
        self.light.switch_off()

class LightOffCommand:
    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.switch_off()

    def undo(self) -> None:
        self.light.switch_on()

class OpenUpGarageCommand:
    def __init__(self, garage: Garage):
        self.garage = garage

    def execute(self) -> None:
        self.garage.switch_on_garage_light()
        self.garage.open_garage_door()

    def undo(self) -> None:
        self.garage.switch_off_garage_light()
        self.garage.close_garage_door()

class CloseDownGarageCommand:
    def __init__(self, garage: Garage):
        self.garage = garage

    def execute(self) -> None:
        self.garage.switch_off_garage_light()
        self.garage.close_garage_door()

    def undo(self) -> None:
        self.garage.switch_on_garage_light()
        self.garage.open_garage_door()