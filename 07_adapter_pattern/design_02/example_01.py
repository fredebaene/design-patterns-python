#!/usr/bin/env python


"""
The adapter pattern changes the interface of a class to an interface that the 
client expects. This is done by wrapping the class with the incompatible 
interface by another class which implements the compatible interface. The 
adapter pattern changes an interface to resolve a compatibility issue.

The facade pattern changes the interface of a class or multiple classes to 
simplify it. It hides the internal complexity of the class(es) after a clean 
facade. This script shows what must happen when someone wants to watch a movie 
on DVD, and its associated complexity, when that person has a home theater.
"""


from devices import (
    Amplifier,
    DvdPlayer,
    PopcornPopper,
    Projector,
    Screen,
    TheaterLights,
)


def main() -> None:
    # Initialize devices in home theater
    popcorn_popper: PopcornPopper = PopcornPopper()
    theater_lights: TheaterLights = TheaterLights()
    screen: Screen = Screen()
    projector: Projector = Projector()
    amplifier: Amplifier = Amplifier()
    dvd_player: DvdPlayer = DvdPlayer()

    # Starting home theater
    popcorn_popper.on()
    popcorn_popper.pop()

    theater_lights.on()
    theater_lights.dim(10)

    screen.down()

    projector.on()
    projector.set_input("DVD")
    projector.widescreen_mode()

    amplifier.on()
    amplifier.set_dvd()
    amplifier.set_surround_sound()
    amplifier.set_volume(5)

    dvd_player.on()
    dvd_player.play()


if __name__ == "__main__":
    main()