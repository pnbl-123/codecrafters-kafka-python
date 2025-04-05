# src/main.py
import socket
import struct

def handle_client(conn):
    try:
        # Receive data (we don't care about the content for this task)
        data = conn.recv(1024)
        print(f"Received: {data}")

        # Construct the response
        message_size = 0
        correlation_id = 7

        # Pack the response in big-endian order
        response = struct.pack(">ii", message_size, correlation_id) # ii = integer, integer

        # Send the response
        conn.sendall(response)
        print(f"Sent: {response}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()


def main():
    host = "localhost"
    port = 9092

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Avoid "Address already in use"
    sock.bind((host, port))
    sock.listen(1)

    print(f"Listening on {host}:{port}")

    while True:
        conn, addr = sock.accept()
        print(f"Connection from: {addr}")
        handle_client(conn)


if __name__ == "__main__":
    main()