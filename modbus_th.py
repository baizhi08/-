# -*- coding: utf-8 -*-
import socket
import sqlite3

import serial
import time

db_file = 'sensor_data.db'


def modbus_th(port, baud, data, stop, command):
    serialport = serial.Serial()
    serialport.port = port
    serialport.baudrate = baud
    serialport.bytesize = int(data)
    serialport.parity = serial.PARITY_NONE
    serialport.stopbits = int(stop)
    serialport.close()
    send_data = bytes(command)
    if not serialport.is_open:
        serialport.open()
    serialport.write(send_data)
    time.sleep(5)
    num = serialport.inWaiting()
    while num == 0:
        time.sleep(0.5)
        num = serialport.inWaiting()
    if num > 0:
        data = serialport.read(num)
        return data


def zlan_connection(ip, port):
    zsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    zsocket.connect((ip, port))
    return zsocket


def send_command(sc, command):
    sc.sendall(command)
    data = sc.recv(8192)
    return data


def decode_test1(data, range1, range2, num):
    data1 = data[range1:range2]
    data_decode1 = int.from_bytes(data1, byteorder='big', signed=True) / num
    return data_decode1


def decode_test(data, range1, range2, range3, range4, num):
    data1 = data[range1:range2]
    data2 = data[range3:range4]
    data_decode1 = int.from_bytes(data1, byteorder='big') / num
    data_decode2 = int.from_bytes(data2, byteorder='big', signed=True) / num
    return data_decode1, data_decode2


def save(n, sid, dl, d1, d2):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sensor_data (编号, 传感器, 位置, 数据) VALUES (?, ?, ?, ?)",
                   (n, sid, dl, d1, d2))
    conn.commit()
    conn.close()
