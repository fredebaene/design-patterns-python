#!/usr/bin/env python


from duck import Duck


class DuckAdapter:
    def __init__(self, duck: Duck):
        if not isinstance(duck, Duck):
            raise TypeError(
                "The argument passed to `duck` must be of type `Duck`."
            )
        self.duck: Duck = duck

    def gobble(self) -> None:
        self.duck.quack()

    def fly(self) -> None:
        self.duck.fly()