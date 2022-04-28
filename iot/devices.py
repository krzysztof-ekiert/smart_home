from iot.device import Device
from iot.message import MessageType

class HueLight(Device):

    def connect(self): print("Connecting Hue Light")

    def disconnect(self): print("Disconnecting Hue Light")

    def send_message(self, mt: MessageType, data: str):
        if data == "":
            print(f"Hue Light handling message of type {mt.name}.")
        else:
            print(f"Hue Light handling message of type {mt.name} with data [{data}].")

    def status_update(self): print("hue_light_status_ok")

class SmartSpeaker(Device):

    def connect(self): print("Connecting Smart Speaker")

    def disconnect(self): print("Disconnecting Smart Speaker")

    def send_message(self, mt: MessageType, data: str):
        if data == "":
            print(f"Smart Speaker handling message of type {mt.name}.")
        else:
            print(f"Smart Speaker handling message of type {mt.name} with data [{data}].")

    def status_update(self): print("smart_speaker_status_ok")

class Curtains(Device):

    def connect(self): print("Connecting curtains")

    def disconnect(self): print("Disconnecting curtains")

    def send_message(self, mt: MessageType, data: str):
        if data == "":
            print(f"Curtains handling message of type {mt.name}.")
        else:
            print(f"Curtains handling message of type {mt.name} with data [{data}].")

    def status_update(self): print("curtains_status_ok")


