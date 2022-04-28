from abc import ABC, abstractmethod

from iot.message import MessageType

class Device:

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
    def status_update(self):
        return "Status OK"
