# -*- coding: utf-8 -*-
import socket
import pickle


def decode_data():
    data = recv_data()
    if len(data) == 6:
        project_name, num, name, sid, location, data1 = data
        print(project_name, num, name, sid, location, data1)
        return project_name, num, name, sid, location, data1
    elif len(data) == 7:
        project_name, num, name, sid, location, data1, data2 = data
        data = f'{data1}   {data2}'
        print(project_name, num, name, sid, location, data)
        return project_name, num, name, sid, location, data
    else:
        print("Received data in unexpected format")
        return


def recv_data():
    s_listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if not s_listen:
        print("Failed socket()")
        exit()
    ip_port = ('192.168.1.125', 3)
    s_listen.bind(ip_port)
    s_listen.listen(5)

    while True:
        cnn, address = s_listen.accept()
        try:
            data = cnn.recv(1024)
            if not data:
                break
            received_data = pickle.loads(data)
            print(f"Received data: {received_data}")
        except Exception as e:
            print(f"Error receiving data: {e}")
        finally:
            cnn.close()

        return received_data
