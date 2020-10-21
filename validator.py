from file_type import FileType
from abc import ABCMeta, abstractmethod


class Validator(metaclass=ABCMeta):
    def __init__(self) -> None:
        self._content = ""

    def set_content(self, content):
        self._content = content

    @abstractmethod
    def validate(self):
        ...
