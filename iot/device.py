from abc import ABC, abstractmethod

from message import MessageType

class Device:
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def connect(self):
        return None

    @abstractmethod
    def disconnect(self):
        return None

    @abstractmethod
    def send_message(self, mt: MessageType, data: str):
        return None

    @abstractmethod
    def status_update(self, data) -> str:
        return data
