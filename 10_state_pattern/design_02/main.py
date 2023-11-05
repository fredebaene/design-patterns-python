#!/usr/bin/env python


from gumball_machine import GumballMachine


def main() -> None:
    gumball_machine: GumballMachine = GumballMachine(5)
    for i in range(6):
        gumball_machine.insert_quarter()
        gumball_machine.eject_quarter()
        gumball_machine.insert_quarter()
        gumball_machine.turn_crank()
    print(gumball_machine.number_of_gumballs)


if __name__ == "__main__":
    main()