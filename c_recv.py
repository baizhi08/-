
import socket
import os


class Socket_Recv:
    def __init__(self, ip, port, save_folder):
        self.ip = ip
        self.port = port
        self.save_folder = save_folder
        self.socket = None

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((self.ip, self.port))
            print("Connected to the server.")
            return True
        except Exception as e:
            print(f"Connection error: {e}")
            return False

    def receive_files(self):
        if not self.socket:
            print("Socket not connected.")
            return False

        try:
            num_files_data = b''
            while True:
                data = self.socket.recv(1)
                if not data or data == b'\t':
                    break
                num_files_data += data
            if not num_files_data:
                return False
            num_files = int(num_files_data.decode().strip())
            print(f"文件数量：{num_files}")

            for _ in range(num_files):
                file_name = b''
                while True:
                    data = self.socket.recv(1)
                    if not data or data == b'\n':
                        break
                    file_name += data
                if not file_name:
                    break
                file_name = file_name.decode().strip()
                file_path = os.path.join(self.save_folder, file_name)

                with open(file_path, 'wb') as fw:
                    while True:
                        data = self.socket.recv(8192)
                        if not data:
                            break
                        fw.write(data)
                        if data.endswith(b'quit\n'):
                            break
                    self.socket.sendall(b'OK')
                print(f"接收到文件：{file_name}")

            print("recv over")
            return True
        except Exception as e:
            print(f"Error while receiving files: {e}")
            return False
        finally:
            self.socket.close()


# if __name__ == '__main__':
#     ip = '192.168.1.125'
#     port = 2
#     save_folder = r'C:\Users\DELL\Desktop\1'
#     recv_socket = Socket_Recv(ip, port, save_folder)
#     if recv_socket.connect():
#         recv_socket.receive_files()
#         print("recv over")
#     else:
#         print("Failed to connect to the server.")
