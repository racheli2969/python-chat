import msvcrt
import socket
import select
import sys
import threading

import protocol

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("127.0.0.1", protocol.PORT))
my_socket.setblocking(0)

user_input = ""


def handle_input():
    global user_input
    while True:
        if msvcrt.kbhit():
            user_char = msvcrt.getch().decode('ASCII')
            if user_char == '\r' or user_char == '\n':
                # Send the message to the server
                if user_input:
                    user_mes = protocol.create_msg(user_input)
                    my_socket.send(user_mes.encode())
                    if user_input == "EXIT":
                        break
                    user_input = ""
            else:
                user_input += user_char
                sys.stdout.write(user_char)
                sys.stdout.flush()


def main():
    inputs = [my_socket]
    outputs = []

    print("Enter commands")
    input_thread = threading.Thread(target=handle_input)
    input_thread.start()

    while True:
        readable, writable, _ = select.select(inputs, outputs, [], 0)

        for sock in readable:
            if sock == my_socket:
                try:
                    (valid_response, response) = protocol.get_msg(my_socket)
                    if valid_response:
                        print("\nServer response: ", response)
                    else:
                        print("\nResponse not valid")
                except socket.error:
                    print("\nConnection to the server closed.")
                    my_socket.close()
                    return

        for sock in writable:
            pass  # There's nothing to write in this client implementation.

    print("Closing\n")
    # Close socket
    my_socket.close()


if __name__ == "__main__":
    main()
