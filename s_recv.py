import socket
import os


def server_recv():
    save_folder = r'C:\Users\DELL\Desktop\test'
    s_listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if not s_listen:
        print("Failed socket()")
        exit()
    ip_port = ('192.168.1.125', 1)
    s_listen.bind(ip_port)
    s_listen.listen(5)
    while True:
        cnn, address = s_listen.accept()
        print("接受到一个连接：%s" % str(address))
        num_files_data = b''
        while True:
            data = cnn.recv(1)
            if not data or data == b'\t':
                break
            num_files_data += data
        if not num_files_data:
            break
        num_files = int(num_files_data.decode().strip())
        print(num_files)
        for _ in range(num_files):
            file_name = b''
            while True:
                data = cnn.recv(1)
                if not data or data == b'\n':
                    break
                file_name += data
            if not file_name:
                break
            file_name = file_name.decode().strip()
            file_path = os.path.join(save_folder, file_name)
            with open(file_path, 'wb') as fw:
                while True:
                    data = cnn.recv(8192)
                    if not data:
                        break
                    if data.endswith(b'quit\n'):
                        fw.write(data[:-5])
                        break
                    else:
                        fw.write(data)
                cnn.sendall(b'OK')
            print(f"接收到文件：{file_name}")
        print("recv over")
        cnn.close()

    return num_files


while True:
    server_recv()
