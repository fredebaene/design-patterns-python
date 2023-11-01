#!/usr/bin/env python


from duck import (
    Duck,
    MallardDuck,
    RubberDuck,
    DecoyDuck,
)
from _fly_behavior import (
    IFlyBehavior,
    RegularFlying,
    NoFlying,
    JetPackFlying,
)
from _quack_behavior import (
    IQuackBehavior,
    RegularQuacking,
    NoQuacking,
    SqueakQuacking,
)


def main() -> None:
    mallard_duck: Duck = MallardDuck()

    mallard_duck.set_fly_behavior(RegularFlying())
    mallard_duck.set_quack_behavior(NoQuacking())
    mallard_duck.fly()
    mallard_duck.quack()

    mallard_duck.set_fly_behavior(JetPackFlying())
    mallard_duck.set_quack_behavior(RegularQuacking())
    mallard_duck.fly()
    mallard_duck.quack()


if __name__ == "__main__":
    main()
