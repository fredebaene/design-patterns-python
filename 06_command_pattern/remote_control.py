from command import ICommand, NoCommand


class RemoteControl:
    def __init__(self, on_commands: list = None, off_commands: list = None):
        self.on_commands = [NoCommand() for _ in range(7)]
        self.off_commands = [NoCommand() for _ in range(7)]

    def set_commands(
            self,
            slot: int,
            on_command: ICommand,
            off_command: ICommand) -> None:
        # Check if the slot ID is valid
        if not -1 < slot < 7:
            raise ValueError("The slot ID is invalid.")
        # Load the slots with the on and off commands
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def press_on_command_button(self, slot: int) -> None:
        self.on_commands[slot].execute()

    def press_off_command_button(self, slot: int) -> None:
        self.off_commands[slot].execute()