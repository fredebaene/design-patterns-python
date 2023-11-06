#!/usr/bin/env python


from turkey import Turkey


class TurkeyAdapter:
    def __init__(self, turkey: Turkey):
        if not isinstance(turkey, Turkey):
            raise TypeError(
                "The argument passed to 'turkey' must be of type 'Turkey'."
            )
        self.turkey: Turkey = turkey

    def quack(self) -> None:
        self.turkey.gobble()

    def fly(self) -> None:
        self.turkey.fly() 