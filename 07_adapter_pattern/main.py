#!/usr/bin/env python


from duck import Duck
from duck_adapter import DuckAdapter
from turkey import Turkey
from turkey_adapter import TurkeyAdapter


class MallardDuck:
    def quack(self) -> None:
        print("I am a mallard duck and I am quacking!")

    def fly(self) -> None:
        print("I am a mallard duck and I am flying!")


class WildTurkey:
    def gobble(self) -> None:
        print("I am a turkey and I am gobbling!")

    def fly(self) -> None:
        print("I am a turkey and I am flying!")


def main() -> None:
    duck: Duck = MallardDuck()
    turkey: Turkey = WildTurkey()
    adapted_turkey: Duck = TurkeyAdapter(turkey)
    turkey.gobble()
    adapted_turkey.quack()
    print(isinstance(adapted_turkey, Duck))


if __name__ == "__main__":
    main()