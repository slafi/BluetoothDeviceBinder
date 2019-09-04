import re


def check_mac_address(mac_address):

    """ Checks if a string matches the pattern of a MAC address.
        :param mac_address: a string that represents a MAC address
    """

    mac_pattern = r'^[a-fA-F0-9]{2}[:][a-fA-F0-9]{2}[:][a-fA-F0-9]{2}[:][a-fA-F0-9]{2}[:][a-fA-F0-9]{2}[:][a-fA-F0-9]{2}$'

    if re.match(mac_pattern, str(mac_address)):
        return True
    else:
        return False