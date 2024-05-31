# -*- coding: utf-8 -*-
import json
import os
import re
import sqlite3
import time
import serial
import socket
import pickle
from s_recv import server_recv

db_file = 'sensor_data.db'
file_path = r'C:\Users\DELL\Desktop\test'


class StateMachine:
    def __init__(self):
        self.state = "IDLE"
        self.collecting = False
        self.saving = False
        self.sensor_files = [os.path.join(file_path, json_file) for json_file in os.listdir(file_path) if
                             json_file.endswith('.json')]

    def set_state(self, state):
        self.state = state
        if state == "STOP":
            self.collecting = False
            self.saving = False
        return self.state

    def get_state(self):
        return self.state

    def collect_data(self):
        if self.state == "COLLECTING":
            self.collecting = True
            for sensor_file in self.sensor_files:
                sid, sname, location, port, baudrate, bytesize, stopbits, timeout, command, name1, range1_1, range1_2, name2, \
                    range2_1, range2_2, dlocation, z_ip, zport, unit1, unit2, dcompute, path = self.decode_path(
                    sensor_file)
                if path == "网口通信":
                    connect = self.zlan_connection(z_ip, int(zport))
                elif path == "串口通信":
                    connect = self.modbus_th(port, baudrate, bytesize, stopbits, command)
                sensor_num = server_recv()
                data = self.run_main(connect, command, name1, name2, range1_1, range1_2, range2_1, range2_2, dcompute,
                                     unit1, unit2,
                                     sname, sid, location, dlocation, sensor_num)
                if data:
                    return data
        return None

    def save_data(self, ip, port, num, name, sid, location, data1, data2):
        if self.state == "SAVING":
            self.saving = True
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
            return {"status": "data saved"}
        return None

    def stop(self):
        self.set_state("STOP")

    def handle_new_file(self, file_data):
        sensor_num = server_recv()
        return {"status": "new configuration applied"}

    def modbus_th(self, port, baud, data, stop, command):
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

    def zlan_connection(self, ip, port):
        zsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        zsocket.connect((ip, port))
        return zsocket

    def decode_path(self, jpath):
        with open(jpath, 'r') as f:
            data = json.load(f)
            sid = data["sensor"][0]["s_id"]
            sname = data["sensor"][0]["s_name"]
            location = data["sensor"][0]["s_location"]
            path = data["sensor"][0]["path"]
            port = data["sensor"][0]["s_port"]
            baudrate = data["sensor"][0]["s_baurd"]
            bytesize = data["sensor"][0]["s_data"]
            stopbits = data["sensor"][0]["s_stop"]
            rs_ip = data["sensor"][0]["rs_ip"]
            rs_port = data["sensor"][0]["rs_port"]
            dlocation = data["sensor"][0]["s_location"]
            query_command = data["command"][0]["query"]
            command_list = [int(x) for x in re.findall(r'\d+', query_command)]
            command = bytes(command_list)
            return_command = bytes(data["command"][0]["return"], 'utf-8')
            timeout = data["forward"][0]["f_timeout"]
            dname = data["decode"][0]["d_name"]
            drange = data["decode"][0]["d_range"]
            dcompute = data["decode"][0]["d_compute"]
            dunit = data["decode"][0]["d_unit"]
        names = dname.split("\n")
        ranges = drange.split("\n")
        unit = dunit.split("\n")
        for i, name in enumerate(names):
            ranges_list = ranges[i].split(',')
            range_start = int(ranges_list[0])
            range_end = int(ranges_list[1])
            if i == 0:
                name1 = name
                range1_1 = range_start - 1
                range1_2 = range_end
                unit1 = unit
            elif i == 1:
                name2 = name
                range2_1 = range_start - 1
                range2_2 = range_end
                unit2 = unit
        return sid, sname, location, port, baudrate, bytesize, stopbits, timeout, command, name1, range1_1, range1_2, \
            name2, range2_1, range2_2, dlocation, rs_ip, rs_port, unit1, unit2, dcompute, path

    def run_main(self, connect, command, name1, name2, range1_1, range1_2, range2_1, range2_2, dcompute, unit1, unit2,
                 sname, sid, location, dlocation, sensor_num):
        th_data = self.send_command(connect, command)
        if name2 is None:
            data1 = self.decode_test1(th_data, range1_1, range1_2, int(dcompute))
            sdata = f'{data1}{unit1}'
            print(name1, sdata)
            self.send_data('192.168.1.125', 3, sensor_num, sname, sid, location, sdata, None)
            self.save(name1, None, dlocation, data1, None)
            return sdata
        else:
            data1, data2 = self.decode_test(th_data, range1_1, range1_2, range2_1, range2_2, int(dcompute))
            sdata1 = f'{data1}{unit1}'
            sdata2 = f'{data2}{unit2}'
            print(sdata1)
            print(sdata2)
            self.send_data('192.168.1.125', 3, sensor_num, sname, sid, location, sdata1, sdata2)
            self.save(name1, name2, dlocation, data1, data2)
            return sdata1, sdata2

    def send_command(self, sc, command):
        sc.sendall(command)
        data = sc.recv(8192)
        return data

    def decode_test1(self, data, range1, range2, num):
        data1 = data[range1:range2]
        data_decode1 = int.from_bytes(data1, byteorder='big', signed=True) / num
        return data_decode1

    def decode_test(self, data, range1, range2, range3, range4, num):
        data1 = data[range1:range2]
        data2 = data[range3:range4]
        data_decode1 = int.from_bytes(data1, byteorder='big') / num
        data_decode2 = int.from_bytes(data2, byteorder='big', signed=True) / num
        return data_decode1, data_decode2

    def save(self, n, sid, dl, d1, d2):
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sensor_data (编号, 传感器, 位置, 数据) VALUES (?, ?, ?, ?)",
                       (n, sid, dl, d1, d2))
        conn.commit()
        conn.close()

    def send_data(self, ip, port, project_name, num, name, sid, location, data1, data2):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        data = [project_name, num, name, sid, location, data1]
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
