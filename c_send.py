# -*- coding: utf-8 -*-
import socket
import os


class Socket_Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = None

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((self.ip, self.port))
            return True
        except Exception as e:
            print(f"Connection error: {e}")
            return False

    def send_files(self, file_paths):
        if not self.socket:
            print("Socket not connected.")
            return False

        try:
            num_files = len(file_paths)
            print(num_files)
            self.socket.sendall(str(num_files).encode() + b'\t')
            for file_path in file_paths:
                file_name = os.path.basename(file_path)
                self.socket.sendall(file_name.encode() + b'\n')
                with open(file_path, 'rb') as f:
                    while True:
                        data = f.read(8192)
                        if not data:
                            break
                        self.socket.sendall(data)
                self.socket.sendall(b'quit\n')
                response = self.socket.recv(1024)
                print(response)
                if response != b'OK':
                    print("Error: Failed to receive confirmation from the server.")
                    return False
                elif response == b'OK':
                    continue

        except Exception as e:
            print(f"Error while sending files: {e}")
            return False
        return True

    def disconnect(self):
        if self.socket:
            self.socket.close()
            self.socket = None
            print("Disconnected from the server.")

# def main_send():
#     client = Socket_Client('192.168.1.125', 1)
#
# if client.connect(): file_paths = [r'E:\pythonProject5\ldr.json', r'E:\pythonProject5\parameter.json',
# r'E:\pythonProject5\th1.json', r'E:\pythonProject5\th2.json'] if client.send_files(file_paths): print("All files
# send successfully.") client.close() else: print("Failed to connect to the server.")
