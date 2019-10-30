# Project Description

This project uses the [RFCOMM tool](https://linux.die.net/man/1/rfcomm) to automatically create a binding with a remote Bluetooth device. This code is particularly useful if you wish to automatically communicate with a previously paired Bluetooth device. The `BluetoothDeviceBinder` class makes it trivial to do so from a Python script.

## Getting Started

### Binding Establishment
To successfully create a binding with a remote Bluetooth device, an instance of `BluetoothDeviceBinder` class can be used as follows:

```python
from ble_binder import bluetooth_device_binder as binder

# Initializes the binding instance
mybinder = binder.BluetoothDeviceBinder()

# Attempts the binding procedure
rcode = mybinder.bind(mac_address='XX:XX:XX:XX:XX:XX', device=0)

# if rcode == 0  : the binding command is successful
# if rcode == -1 : the provided MAC address is not valid
# if rcode == -2 : an exception has occured
# if rcode == ?  : a return code proper to the RFCOMM command
```
### Binding Release

Similarly to the binding establishment, one can use the class method `release` to release any existent binding. The device identifier should be provided to properly identify which binding should be released.

```python
from ble_binder import bluetooth_device_binder as binder

# Initializes the binding instance
mybinder = binder.BluetoothDeviceBinder()

# Release the binding
rcode = mybinder.release(device=0, sudo=True)

# if rcode == 0  : the binding command is successful
# if rcode == -1 : the provided MAC address is not valid
# if rcode == -2 : an exception has occured
# if rcode == ?  : a return code proper to the RFCOMM command
```

### Prerequisites

This code is platform-specific because the RFCOMM tool is available only on Linux-based systems. However, no specific Python libraries are required to use it.

### Usage Example

A code example is provided in [example.py](example.py). This example file runs successfully under Ubuntu 18.04 and Raspbian 10 (kernel v4.19).

## Root Privileges

To successfully run this code (and the underlying RFCOMM tool), elevated privileges might be required. If automation is a must, the script can be granted higher privileges in one of two *trivial* but <span style="color:red">*potentially insecure*</span> ways:

1. Provide user password in a shell script: The script can be directly called from Python or wrapped into a Python structure similar to `BluetoothDeviceBinder` class.

```bash
#!/bin/bash
echo user_password | sudo -S python python_script.py
```

2. Grant higher privileges to Python runtime: This means that you either *temporarily* or *permanently* grant `/usr/bin/python3` superuser priviliges so all the Python scripts will execute without asking for root / superuser credentials.

<span style="color:red">**WARNING:** In both cases, the security of your system may be breached. You **should not** grant any process, command, script or executable root priviliges if you are not sure that this will not affect your system's integrity and security. Providing your password in **clear** to any program or script must also be avoided unless you take the required measures in order to protect it on disk and in memory.</span>

## Built With:

* [Python 3.7](https://www.python.org/downloads/release/python-374/)

## Tested Under:
* [Ubuntu 18.04](http://releases.ubuntu.com/18.04/)
* [Raspian 10](https://www.raspberrypi.org/downloads/raspbian/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.