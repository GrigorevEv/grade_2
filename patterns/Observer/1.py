from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List, Callable


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class ConcreteSubject(Subject):
    _state: int = None
    _observers: List[Callable] = []

    def attach(self, observer: Callable):
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Callable):
        self._observers.remove(observer)

    def notify(self):
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer(self)

    def some_business_logic(self):
        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


def react_on_state_1(subject: Subject):
    if subject._state < 3:
        print("ConcreteObserverA: Reacted to the event")


def react_on_state_2(subject: Subject):
    if subject._state == 0 or subject._state >= 2:
        print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    subject = ConcreteSubject()

    subject.attach(react_on_state_1)
    subject.attach(react_on_state_2)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(react_on_state_1)

    subject.some_business_logic()
