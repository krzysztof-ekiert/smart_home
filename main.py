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

    idsdel=[]

    for i in iotservice.deviceList:
        idsdel.append(i[0])

    for j in idsdel:
        iotservice.unregister_device(j)


main()
