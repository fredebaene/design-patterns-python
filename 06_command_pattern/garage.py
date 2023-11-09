class Garage:
    def __init__(self, id: str):
        self.id = id

    def open_garage_door(self) -> None:
        print(f"GARAGE : {self.id} | Door opening...")

    def close_garage_door(self) -> None:
        print(f"GARAGE : {self.id} | Door closing...")

    def switch_on_garage_light(self) -> None:
        print(f"GARAGE : {self.id} | Switch on light...")

    def switch_off_garage_light(self) -> None:
        print(f"GARAGE : {self.id} | Switch off light...")