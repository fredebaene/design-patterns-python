from light import Light
from garage import Garage
from command import ICommand, NoCommand, LightOnCommand, LightOffCommand, OpenUpGarageCommand, CloseDownGarageCommand
from remote_control import RemoteControl


def main():
    # Initialize the receivers
    kitchen_light: Light = Light("Kitchen Light")
    living_room_light: Light = Light("Living Room")
    garage_door: Garage = Garage("Garage")

    # Initialize the receiver-specific commands
    switch_kitchen_light_on: LightOnCommand = LightOnCommand(kitchen_light)
    switch_kitchen_light_off: LightOffCommand = LightOffCommand(kitchen_light)
    switch_living_room_light_on: LightOnCommand = LightOnCommand(living_room_light)
    switch_living_room_light_off: LightOffCommand = LightOffCommand(living_room_light)
    open_garage_door: OpenUpGarageCommand = OpenUpGarageCommand(garage_door)
    close_garage_door: CloseDownGarageCommand = CloseDownGarageCommand(garage_door)

    # Initialize a remote control
    remote_control: RemoteControl = RemoteControl()
    remote_control.set_commands(0, switch_kitchen_light_on, switch_kitchen_light_off)
    remote_control.set_commands(1, switch_living_room_light_on, switch_living_room_light_off)
    remote_control.set_commands(2, open_garage_door, close_garage_door)

    # Press buttons
    remote_control.press_on_command_button(0)
    remote_control.press_on_command_button(1)
    remote_control.press_off_command_button(1)
    remote_control.press_off_command_button(0)
    remote_control.press_on_command_button(2)
    remote_control.press_off_command_button(2)


if __name__ == "__main__":
    main()