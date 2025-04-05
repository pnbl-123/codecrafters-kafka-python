# src/main.py
import socket
import struct

def parse_header(b_msg):
    pass

def handle_client(conn):
    try:
        REQUEST_SIZE = 4 * 3 # header size
        data = conn.recv(REQUEST_SIZE)
        print(f"Received: {data}")
        
        print("test unpack")
        msg_size, req_api_key, req_api_ver, cor_id = struct.unpack(">ihhi", data)

        response = struct.pack(">ii", msg_size, cor_id)

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
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(1)

    print(f"Listening on {host}:{port}")

    while True:
        conn, addr = sock.accept()
        print(f"Connection from: {addr}")
        handle_client(conn)


if __name__ == "__main__":
    main()
