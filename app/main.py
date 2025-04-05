# src/main.py
import socket
import struct


def handle_client(conn):
    try:
        size_data = conn.recv(4)
        msg_size = struct.unpack(">i", size_data)[0]
        
        body = conn.recv(msg_size)
        
        api_key, api_version = struct.unpack(">hh", body[:4])
        correlation_id = struct.unpack(">i", body[4:8])[0]
        
        err_code = 35
        
        response = struct.pack(">iih", msg_size, correlation_id, err_code)
        conn.sendall(response)
        
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
