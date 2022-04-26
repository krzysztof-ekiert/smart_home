from device import Device
import message

def collect_diagnostics(dev: Device, status):
    print("Connecting to diagnostics server.")
    dev.status_update(status)
    print(f"Sending status update <{status}> to server.")
    return None

