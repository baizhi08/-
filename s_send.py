import socket
import os
import glob


def send_files():
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip_port = ('192.168.1.125', 2)
    socket_server.bind(ip_port)
    socket_server.listen(5)
    print("等待连接...")
    while True:
        try:
            conn, address = socket_server.accept()
            print("连接成功:", address)

            path = r'C:\Users\DELL\Desktop\test'
            json_files = glob.glob(path + "/*.json")
            num_files = len(json_files)
            print(f"文件数量：{num_files}")

            conn.sendall(str(num_files).encode() + b'\t')
            for file_path in json_files:
                file_name = os.path.basename(file_path)
                conn.sendall(file_name.encode() + b'\n')
                with open(file_path, 'rb') as f:
                    while True:

                        data = f.read(8192)

                        if not data:
                            break
                        conn.sendall(data)
                conn.sendall(b'quit\n')
                response = conn.recv(1024)
                print(response)
                if response != b'OK':
                    print("错误：未能从客户端接收确认信号")
                    break
                f.close()
            pass
        except Exception as e:
            print(f"发送文件时出错: {e}")
        finally:
            conn.close()
            print("连接已关闭")


if __name__ == '__main__':
    send_files()

