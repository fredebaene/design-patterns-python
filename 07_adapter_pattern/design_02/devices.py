from abc import ABC, abstractmethod
from typing import Literal


class TheaterLights:
    def on(self) -> None:
        print("Turning on theater lights ...")

    def off(self) -> None:
        print("Turning off theater lights ...")

    def dim(self, strength: int) -> None:
        print(f"Dimming theater lights: setting to {strength} ...")

    
class PopcornPopper:
    def on(self) -> None:
        print("Turning on popcorn popper ...")

    def off(self) -> None:
        print("Turning off popcorn popper ...")

    def pop(self) -> None:
        print("Popping popcorn ...")


class Screen:
    def up(self) -> None:
        print("Hiding screen ...")

    def down(self) -> None:
        print("Showing screen ...")


class Tuner:
    def on(self) -> None:
        print("Turning on tuner ...")

    def off(self) -> None:
        print("Turning off tuner ...")

    def set_am(self) -> None:
        print("Setting tuner to AM ...")

    def set_fm(self) -> None:
        print("Setting tuner to FM ...")

    def set_frequency(self, frequency: float) -> None:
        print(f"Setting frequency to {frequency} ...")


class Projector:
    def on(self) -> None:
        print("Turning on projector ...")

    def off(self) -> None:
        print("Turning off projector ...")

    def tv_mode(self) -> None:
        print("Setting projector to TV mode ...")

    def widescreen_mode(self) -> None:
        print("Setting projector to widescreen mode ...")


class DvdPlayer:
    def on(self) -> None:
        print("Turning on DVD player ...")
    
    def off(self) -> None:
        print("Turning off DVD player ...")

    def eject(self) -> None:
        print("Ejecting DVD from DVD player ...")

    def pause(self) -> None:
        print("Pausing DVD in DVD player ...")

    def play(self) -> None:
        print("Starting DVD in DVD player ...")

    def stop(self) -> None:
        print("Stopping DVD in DVD player ...")

    def set_surround_audio(self) -> None:
        print("Enabling surround sound for DVD player ...")

    def set_two_channel_audio(self) -> None:
        print("Enabling two-channel audio for DVD player ...")


class CdPlayer:
    def on(self) -> None:
        print("Turning on CD player ...")
    
    def off(self) -> None:
        print("Turning off CD player ...")

    def eject(self) -> None:
        print("Ejecting CD from CD player ...")

    def pause(self) -> None:
        print("Pausing CD in CD player ...")

    def play(self) -> None:
        print("Starting CD in CD player ...")

    def stop(self) -> None:
        print("Stopping CD in CD player ...")
    

class Amplifier:
    def on(self) -> None:
        print("Turning on amplifier ...")

    def off(self) -> None:
        print("Turning off amplifier ...")

    def set_cd(self) -> None:
        print("Setting input to CD player for amplifier ...")

    def set_dvd(self) -> None:
        print("Setting input to DVD player for amplifier ...")

    def set_stereo_sound(self) -> None:
        print("Enabling stereo sound for amplifier ...")

    def set_surround_sound(self) -> None:
        print("Enabling surround sound for amplifier ...")

    def set_tuner(self) -> None:
        print("Setting tuner for amplifier ...")

    def set_volume(self, volume: float) -> None:
        print(f"Setting volume to {volume} on amplifier ...")