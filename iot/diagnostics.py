from device import Device
import message

def collect_diagnostics(dev: Device):
    print("Connecting to diagnostics server.")
    x = dev.status_update()
    print(f"Sending status update <{x}> to server.")
    return None

