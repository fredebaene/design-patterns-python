#!/usr/bin/env python


from gumball_machine import GumballMachine


def main() -> None:
    gumball_machine: GumballMachine = GumballMachine(20)
    gumball_machine.insert_quarter()
    gumball_machine.insert_quarter()
    gumball_machine.eject_quarter()
    print(gumball_machine.machine_state)


if __name__ == "__main__":
    main()