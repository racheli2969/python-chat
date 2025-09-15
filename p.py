"""EX 2.6 protocol implementation
   Author: Rachel Pokroy
   Date: June 2023
"""

LENGTH_FIELD_SIZE = 3
PORT = 8820


def check_cmd(data):
    """Check if the command is defined in the protocol (e.g NAME, GET_NAMES, MSG, EXIT)"""
    options = ["NAME", "GET_NAMES", "MSG", "EXIT"]
    if data in options:
        return True
    return False


def create_msg(data):
    """Create a valid protocol message, with length field"""
    length = str(len(data))
    zfill_length = length.zfill(LENGTH_FIELD_SIZE)
    return zfill_length + data


def get_msg(my_socket):
    """Extract message from protocol, without the length field
       If length field does not include a number, returns False, "Error" """
    length = my_socket.recv(LENGTH_FIELD_SIZE).decode()
    if length.isdigit():
        message = my_socket.recv(int(length)).decode()
        return True, message
    else:
        return False, "Error"

