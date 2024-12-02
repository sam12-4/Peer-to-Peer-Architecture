import socket
import threading

def peer_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen(5)
    print(f"Peer server started on port {port}")
    
    while True:
        conn, addr = server.accept()
        print(f"Connection from {addr}")
        data = conn.recv(1024).decode()
        print(f"Received: {data}")
        conn.send("Data received!".encode())
        conn.close()


def peer_client(server_ip, server_port, message):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))
    client.send(message.encode())
    response = client.recv(1024).decode()
    print(f"Server response: {response}")
    client.close()

if __name__ == "__main__":
    port = 5000
    threading.Thread(target=peer_server, args=(port,)).start()
    
    # Simulating a client after the server starts
    peer_client("127.0.0.1", port, "Hello from Peer!")
