from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class SimpleCommand(Command):
    def __init__(self, payload: str):
        self.payload = payload

    def execute(self):
        print(f"SimpleCommand: See, I can do simple things like printing"
              f"({self.payload})")


class ComplexCommand(Command):
    def __init__(self, receiver: Receiver, a: str, b: str):
        self.receiver = receiver
        self.a = a
        self.b = b

    def execute(self):
        print("ComplexCommand: Complex stuff should be done by a receiver object", end="")
        self.receiver.do_something(self.a)
        self.receiver.do_something_else(self.b)


class Receiver:
    def do_something(self, a: str):
        print(f"\nReceiver: Working on ({a}.)", end="")

    def do_something_else(self, b: str):
        print(f"\nReceiver: Also working on ({b}.)", end="")


class Invoker:
    on_start = None
    on_finish = None

    def set_on_start(self, command: Command):
        self.on_start = command

    def set_on_finish(self, command: Command):
        self.on_finish = command

    def do_something_important(self):
        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self.on_start, Command):
            self.on_start.execute()

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self.on_finish, Command):
            self.on_finish.execute()


if __name__ == "__main__":
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say Hi!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(
        receiver, "Send email", "Save report"))

    invoker.do_something_important()
