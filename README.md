# Socket Chat Application

This is a simple chat application implemented using sockets in Python. It allows clients to connect to a server and exchange messages in real-time.

## Prerequisites

- Python 3.x
- tkinter (for the client GUI)

## Usage

1. Start the server by running the `server.py` script:

   ```bash
   $ python server.py

2. Start the client application by running the client.py script:

   ```bash
   $ python client.py
   ```

The client GUI window will open.

3. Enter a username in the client GUI and click the "Enter" button. This will connect the client to the server with the specified username.

4. Start sending and receiving messages in the chat window. Type your message in the input field at the bottom and click the "Send" button to send it. The messages will appear in the chat window.

## File Descriptions

- `server.py`: The server-side script that handles client connections and message broadcasting.
- `client.py`: The client-side script that provides a GUI interface for the chat application.

## License

This project is licensed under the MIT License.
