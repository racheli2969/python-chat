# Python Chat Application

## Project Overview
This project is a Python-based chat application that includes both server and client components. It allows multiple clients to communicate with each other through a central server. The application demonstrates the use of Python's socket programming and threading capabilities.

## Features
- **Server-Client Architecture**: The server handles multiple clients simultaneously.
- **Real-Time Communication**: Clients can send and receive messages in real-time.
- **Protocol Implementation**: A custom protocol is used for communication between the server and clients.
- **Ease of Use**: Simple and intuitive interface for both server and client.

## File Structure
- `server.py`: Contains the server-side implementation.
- `client_chat.py`: Contains the client-side implementation.
- `protocol.py`: Defines the communication protocol between the server and clients.
- `audio.py`, `c.py`, `p.py`, `practice.py`, `s.py`, `temp.py`: Additional scripts for various functionalities.
- `chat.txt`, `client chat.txt`: Text files for storing chat logs.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd ex26
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Running the Server
1. Open a terminal and navigate to the project directory.
2. Run the server script:
   ```bash
   python server.py
   ```

### Running the Client
1. Open another terminal and navigate to the project directory.
2. Run the client script:
   ```bash
   python client_chat.py
   ```
3. Follow the on-screen instructions to connect to the server and start chatting.

## Requirements
- Python 3.9 or higher
- Required libraries are listed in `requirements.txt`.

## License
This project is licensed under the MIT License. Feel free to use and modify it as per your needs.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for any bugs or feature requests.
