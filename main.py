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

    for i in iotservice.deviceList:
        id = i[0]
        iotservice.unregister_device(id)

    for i in iotservice.deviceList:
        id = i[0]
        iotservice.unregister_device(id)


main()
