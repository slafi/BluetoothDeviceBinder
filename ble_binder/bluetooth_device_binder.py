from .utils import check_mac_address
import subprocess
import logging


logger = logging.getLogger(__name__)


class BluetoothDeviceBinder():
    
    """ A class to create and release bindings with a BLE device """

    def __init__(self):
        self.stdout_data = None
        self.stderr_data = None


    def bind(self, mac_address, device=0, channel=1, timeout=15, sudo=False):
        
        """ Creates a binding with another device given its MAC address.

            :param mac_address: device MAC address
            :param device: device number
            :param channel: communication channel
            :param timeout: the maximum time period required for the process before it fails
            :param sudo: execute the command with root privileges
            :return : an integer return code: -1 if MAC address invalid, -2 if exception, 
                      process.returncode otherwise
        """

        if(mac_address == None or mac_address == '' or not check_mac_address(mac_address)):
            return -1
        else:
            proc = None
            try:
                if sudo:
                    cmd = ['sudo', 'rfcomm', 'bind', str(device), str(mac_address), str(channel)]
                else:
                    cmd = ['rfcomm', 'bind', str(device), str(mac_address), str(channel)]

                proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                self.stdout_data, self.stderr_data = proc.communicate(timeout)
                return proc.returncode

            except Exception as e:
                logger.error(f'An exception has occured: {str(e)}\n')
                if proc != None:
                    proc.kill()
                self.stdout_data, self.stderr_data = proc.communicate()
                return -2
    

    def release(self, device=0, timeout=15, sudo=False):

        """ Removes a current binding with another device.

            :param device: device number
            :param timeout: the maximum time period required for the process before it fails
            :param sudo: execute the command with root privileges
            :return : -1 if exception, process.returncode otherwise
        """

        if sudo:
            cmd = ['sudo', 'rfcomm', 'release', str(device)]
        else:
            cmd = ['rfcomm', 'release', str(device)]

        proc = None

        try:
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
            self.stdout_data, self.stderr_data = proc.communicate(timeout)
            return proc.returncode

        except Exception as e:
            logger.error(f'An exception has occured: {str(e)}\n')
            if proc != None:
                proc.kill()
            self.stdout_data, self.stderr_data = proc.communicate()
            return -1
        