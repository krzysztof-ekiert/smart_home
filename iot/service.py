from iot.message import Message
from iot.device import Device
from iot.diagnostics import collect_diagnostics
import random

def generate_id(len):
    ciag=""
    for i in range(len):
        x = random.randint(65, 90)
        n = chr(x)
        ciag +=n
    return ciag

class IOTService:

    deviceList=[]

    def register_device(self, dev: Device):
        dev.connect()
        id=generate_id(10)
        print(f"Added device with the id {id}")
        global deviceList
        self.deviceList.append([id, dev])

    def unregister_device(self, id):
        global deviceList
        for i in self.deviceList:
            if i[0] == id:
                i[1].disconnect()
                self.deviceList.remove(i)
                print(f"Removed device with the id {id}")

    def get_device(self, id):
        global deviceList
        x = "NONE"
        for i in self.deviceList:
            if i[0] == id:
                x = i[1]
        return x

    def run_program(self, list):
        print("=====RUNNING PROGRAM======")
        global deviceList
        for i in list:
            for j in self.deviceList:
                if j[0] == i.device_id:
                    j[1].send_message(i.msg_type, i.data)
        print("=====END OF PROGRAM======")

    def test_devices(self):
        print("Start test devices")
        global deviceList
        for i in self.deviceList:
            collect_diagnostics(i[1])
