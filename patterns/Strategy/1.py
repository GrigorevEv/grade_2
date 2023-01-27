from __future__ import annotations
from typing import List, Callable


class Context:
    def __init__(self, strategy: Callable[list, list]):
        self.strategy = strategy

    def do_some_business_logic(self, data: list):
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self.strategy(data)
        print(",".join(result))


def do_algorithm_1(data: List) -> List:
    return sorted(data)


def do_algorithm_2(data: List) -> List:
    return reversed(sorted(data))


if __name__ == "__main__":
    context = Context(do_algorithm_1)
    print("Client: Strategy is set to normal sorting.")

    data = ["a", "b", "c", "d", "e"]
    context.do_some_business_logic(data)
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = do_algorithm_2
    context.do_some_business_logic(data)
