class Light:
    def __init__(self, id: str):
        self.id = id

    def switch_on(self) -> None:
        print(f"LIGHT : {self.id} | Switching on...")

    def switch_off(self) -> None:
        print(f"LIGHT : {self.id} | Switching off...")