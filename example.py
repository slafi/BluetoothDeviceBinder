from ble_binder import bluetooth_device_binder as binder

mybinder = binder.BluetoothDeviceBinder()

rcode = mybinder.bind(mac_address='AA:BB:CC:11:22:33', device=0)

print('Output: ' + mybinder.stderr_data.decode('ascii'))
print('Error: '  + mybinder.stdout_data.decode('ascii'))
print('code: ' + str(rcode))