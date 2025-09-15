import select
import socket

import utils.protocol as protocol

clients = {}


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", protocol.PORT))
    server_socket.listen()
    print("Server is up and running")

    inputs = [server_socket]

    while True:
        read_list, _, _ = select.select(inputs, [], [])

        for current_socket in read_list:
            if current_socket == server_socket:
                (client_socket, client_address) = server_socket.accept()
                print("New client connected:", client_address)
                inputs.append(client_socket)
                clients[client_socket] = None
                send_welcome_message(client_socket)
            else:
                valid_msg, mes = protocol.get_msg(current_socket)
                if valid_msg:
                    handle_command(current_socket, mes)
                else:
                    handle_exit_command(current_socket)
                    inputs.remove(current_socket)

    print("Closing\n")
    # Close sockets
    server_socket.close()


def send_welcome_message(client_socket):
    response = "Welcome to the server! Please enter your name: "
    client_socket.send(protocol.create_msg(response).encode())


def handle_command(client_socket, message):
    arr = message.split()
    if protocol.check_cmd(arr[0]):
        if arr[0] == "NAME":
            handle_name_command(client_socket, arr[1])
        elif arr[0] == "GET_NAMES":
            handle_get_names_command(client_socket)
        elif arr[0] == "MSG":
            handle_msg_command(client_socket, arr[1], ' '.join(arr[2:]))
        elif arr[0] == "EXIT":
            handle_exit_command(client_socket)
    else:
        response = "INVALID COMMAND"
        client_socket.send(protocol.create_msg(response).encode())


def handle_name_command(client_socket, name):
    if name in [client_name for client_name in clients.values() if client_name is not None]:
        response = f"Error: The name '{name}' is already taken. Please choose a different name."
        client_socket.send(protocol.create_msg(response).encode())
    else:
        clients[client_socket] = name
        response = f"HELLO {name}"
        client_socket.send(protocol.create_msg(response).encode())


def handle_get_names_command(client_socket):
    names = ', '.join([client_name for client_name in clients.values() if client_name is not None])
    response = f"Connected clients: {names}"
    client_socket.send(protocol.create_msg(response).encode())


def handle_msg_command(client_socket, recipient, message):
    sender_name = clients[client_socket]
    for sock, name in clients.items():
        if name == recipient:
            response = f"Message from {sender_name}: {message}"
            sock.send(protocol.create_msg(response).encode())
            break
    else:
        response = f"Error: No client with the name '{recipient}' exists."
        client_socket.send(protocol.create_msg(response).encode())


def handle_exit_command(client_socket):
    name = clients.pop(client_socket)
    client_socket.close()
    response = f"Goodbye, {name}!"
    for sock in clients.keys():
        if sock != client_socket:
            sock.send(protocol.create_msg(response).encode())


if __name__ == "__main__":
    main()
