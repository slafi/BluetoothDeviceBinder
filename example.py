from ble_binder import bluetooth_device_binder as binder
import time


if __name__ == "__main__":

    ## Instantiate the BluetoothDeviceBinder class
    mybinder = binder.BluetoothDeviceBinder()

    ## Sudo keyword allows to execute the binding command with root previliges
    rcode = mybinder.bind(mac_address='AA:BB:CC:11:22:33', device=0, sudo=True)

    print('Output: ' + mybinder.stderr_data.decode('ascii'))
    print('Error: '  + mybinder.stdout_data.decode('ascii'))
    print('code: ' + str(rcode))

    ## Main process is halting
    time.sleep(10)

    ## Release the binding
    mybinder.release(device=0, sudo=True)

    