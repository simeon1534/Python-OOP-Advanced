from abc import ABC, abstractmethod
import requests


class Command(ABC):
    def __init__(self, receiver):
        self._receiver = receiver

    @abstractmethod
    def execute(self):
        pass


class URLExecutor(Command):
    def execute(self):
        return requests.get(self._receiver).content


print(URLExecutor('http://youtube.com/').execute())
