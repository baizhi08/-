# -*- coding: utf-8 -*-
import socket
import pickle


def send_data(ip, port, num, name, sid, location, data1, data2):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data = [num, name, sid, location, data1]
    if data2 is not None:
        data.append(data2)
    try:
        client_socket.connect((ip, int(port)))
        serialized_data = pickle.dumps(data)
        client_socket.sendall(serialized_data)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()


if __name__ == '__main__':
    sip = '192.168.1.125'
    sport = 3
    sname = "test"
    s_id = "1-1"
    slocation = "测试"
    sdata1 = 19.2
    unit = '℃'
    sdata2 = None
    while True:
        send_data(sip, sport, sname, s_id, slocation, sdata1, sdata2, unit)
