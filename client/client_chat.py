"""EX 2.6 client implementation
   Author: Rachel Pokroy
   Date: July 2023
"""
import msvcrt
import socket
import select
import sys
import threading
import signal
import utils.protocol as protocol

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("127.0.0.1", protocol.PORT))
my_socket.setblocking(0)

user_input = ""


def handle_input():
    global user_input
    while True:
        if msvcrt.kbhit():
            user_char = msvcrt.getch().decode()
            if user_char == '\r' or user_char == '\n':
                # Send the message to the server
                if user_input:
                    if len(user_input.split()) > 1 and not user_input.split()[1].isspace() or user_input == "EXIT":
                        user_mes = protocol.create_msg(user_input)
                        my_socket.send(user_mes.encode())
                    else:
                        print("\nOperation requires parameters")
                    user_input = ""  # Clear user_input after processing
                    if user_input == "EXIT":
                        break
            else:
                user_input += user_char
                sys.stdout.write(user_char)
                sys.stdout.flush()

    my_socket.close()
    print("Client terminated.")


def sigint_handler(sig, frame):
    handle_input()  # Send EXIT message before terminating on Ctrl+C


def main():
    signal.signal(signal.SIGINT, sigint_handler)

    inputs = [my_socket]

    print("Enter commands")
    input_thread = threading.Thread(target=handle_input)
    input_thread.start()

    while True:
        read_list, _, _ = select.select(inputs, [], [])

        for sock in read_list:
            if sock == my_socket:
                try:
                    (valid_response, response) = protocol.get_msg(my_socket)
                    if valid_response:
                        print("\nServer response: ", response)
                        if response.startswith("Goodbye"):
                            my_socket.close()
                            sys.exit(0)
                    else:
                        print("\nResponse not valid")
                except socket.error:
                    print("\nConnection to the server closed.")
                    my_socket.close()
                    sys.exit(0)

        print("Closing\n")
        # Close socket
        my_socket.close()


if __name__ == "__main__":
    main()
