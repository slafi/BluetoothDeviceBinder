from .utils import check_mac_address
import subprocess


class BluetoothDeviceBinder():

    """ A class to create and release bindings with a BLE device """

    def __init__(self):
        self.stdout_data = None
        self.stderr_data = None


    def bind(self, mac_address, device=0, channel=1, timeout=15):
        
        """ Creates a binding with another device given its MAC address.
            :param mac_address: device MAC address
            :param device: device number
            :param channel: communication channel
            :param timeout: the maximum time period required for the process before it fails
            :return : an integer return code
        """

        if(mac_address == None or mac_address == '' or not check_mac_address(mac_address)):
            return -1
        else:
            proc = None
            try:
                cmd = ['rfcomm', 'bind', str(device), str(mac_address), str(channel)]

                proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                self.stdout_data, self.stderr_data = proc.communicate(timeout)
                return proc.returncode

            except Exception as e:
                print('An exception has occured: {}\n'.format(str(e)))
                if proc != None:
                    proc.kill()
                self.stdout_data, self.stderr_data = proc.communicate()
                return -2
    

    def release(self, device=0, timeout=15):

        """ Removes a current binding with another device.
            :param device: device number
            :param timeout: the maximum time period required for the process before it fails
        """

        cmd = ['rfcomm', 'release', str(device)]
        proc = None

        try:
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
            self.stdout_data, self.stderr_data = proc.communicate(timeout)
            return proc.returncode

        except Exception as e:
            print('An exception has occured: {}\n'.format(str(e)))
            if proc != None:
                proc.kill()
            self.stdout_data, self.stderr_data = proc.communicate()
            return -1
        
