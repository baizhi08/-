# -*- coding: utf-8 -*-
import json
import os
import re

from modbus_th import *
from data_send import *
from s_recv import server_recv

file_path = r'C:\Users\DELL\Desktop\test'


def decode_path(jpath):
    name1 = None
    name2 = None
    range1_1 = None
    range1_2 = None
    range2_1 = None
    range2_2 = None
    unit1 = None
    unit2 = None
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


def run_main():
    th_data = send_command(connect, command)
    if name2 is None:
        data1 = decode_test1(th_data, range1_1, range1_2, int(dcompute))
        sdata = f'{data1}{unit1}'
        print(name1, sdata)
        send_data('192.168.1.125', 3, sensor_num, sname, sid, location, sdata, None)
        save(name1, None, dlocation, data1, None)
    else:
        data1, data2 = decode_test(th_data, range1_1, range1_2, range2_1, range2_2, int(dcompute))
        sdata1 = f'{data1}{unit1}'
        sdata2 = f'{data2}{unit2}'
        print(sdata1)
        print(sdata2)
        send_data('192.168.1.125', 3, sensor_num, sname, sid, location, sdata1, sdata2)
        save(name1, name2, dlocation, data1, data2)

    time.sleep(2)


sensor_files = [os.path.join(file_path, json_file) for json_file in os.listdir(file_path) if
                json_file.endswith('.json')]

while True:
    sensor_num = server_recv()
    for sensor_file in sensor_files:
        sid, sname, location, port, baudrate, bytesize, stopbits, timeout, command, name1, range1_1, range1_2, name2, \
            range2_1, range2_2, dlocation, z_ip, zport, unit1, unit2, dcompute, path = decode_path(sensor_file)
        if path == "网口通信":
            connect = zlan_connection(z_ip, int(zport))
        elif path == "串口通信":
            connect = modbus_th(port, baudrate, bytesize, stopbits, command)
        run_main()
