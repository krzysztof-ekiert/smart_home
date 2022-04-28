import iot

def main():
    iotservice = iot.service.IOTService()

    huelight = iot.devices.HueLight()
    smartspeaker = iot.devices.SmartSpeaker()
    curtains = iot.devices.Curtains()

    iotservice.register_device(huelight)
    iotservice.register_device(smartspeaker)
    iotservice.register_device(curtains)

    iotservice.test_devices()

    wakeup=[]
    m1 = iot.message.Message(iotservice.deviceList[0][0], iot.message.MessageType(1))
    m2 = iot.message.Message(iotservice.deviceList[1][0], iot.message.MessageType(1))
    m3 = iot.message.Message(iotservice.deviceList[1][0], iot.message.MessageType(4),"Angel of Death")
    m4 = iot.message.Message(iotservice.deviceList[2][0], iot.message.MessageType(5))
    wakeup.append(m1)
    wakeup.append(m2)
    wakeup.append(m3)
    wakeup.append(m4)

    sleep = []
    m1 = iot.message.Message(iotservice.deviceList[0][0], iot.message.MessageType(2))
    m2 = iot.message.Message(iotservice.deviceList[1][0], iot.message.MessageType(2))
    m3 = iot.message.Message(iotservice.deviceList[2][0], iot.message.MessageType(6))
    sleep.append(m1)
    sleep.append(m2)
    sleep.append(m3)

    print("program Wake Up")
    iotservice.run_program(wakeup)
    print("program Sleep")
    iotservice.run_program(sleep)

    idsdel=[]

    for i in iotservice.deviceList:
        idsdel.append(i[0])

    for j in idsdel:
        iotservice.unregister_device(j)

    print("END OF OPERATIONS")

main()
