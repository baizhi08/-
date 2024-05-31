import json


def save_iotE_Data(cip, cport, cpath, tid, tname, tproject, tlocation, tdate, to, save_iotE_path):
    i_data = \
        {"cnn": [
            {"cnn_ip": cip, "cnn_port": cport, "cnn_path": cpath}
        ],
            "iot": [
                {"t_id": tid, "t_name": tname, "t_belong": tproject, "t_location": tlocation, "t_date": tdate,
                 "t_remark": to}
            ]
        }
    # save_iotE_path = "E:\\pythonProject5\\" + tname + ".json"
    with open(save_iotE_path, 'w') as file:
        json.dump(i_data, file, ensure_ascii=False, indent=4)


def import_iotE_Data(save_iotE_path):
    with open(save_iotE_path, 'r') as f:
        data = json.load(f)
        cip = data["cnn"][0]["cnn_ip"]
        cport = data["cnn"][0]["cnn_port"]
        cpath = data["cnn"][0]["cnn_path"]
        tid = data["iot"][0]["t_id"]
        tname = data["iot"][0]["t_name"]
        tproject = data["iot"][0]["t_belong"]
        tlocation = data["iot"][0]["t_location"]
        tdate = data["iot"][0]["t_date"]
        to = data["iot"][0]["t_remark"]
    return cip, cport, cpath, tid, tname, tproject, tlocation, tdate, to


def save_sensor_Data(sid, sname, slocation, frequency, sdate, so, path, sport, baurd, data_bit, stop_bit, check_bit,
                         rs_id, rs_ip, rs_port, query_command, return_command, turn_ip, turn_port, timeout,
                         turn_path, save_sensor_path, dorder, dnum, dname, drange, dcompute, unit):
    s_data = \
        {
            "sensor": [
                {"s_id": sid, "s_name": sname, "s_location": slocation, "s_rate": frequency, "s_date": sdate,
                 "s_remark": so, "s_port": sport, "path": path, "s_baurd": baurd, "s_data": data_bit, "s_stop": stop_bit,
                 "s_check": check_bit, "rs_id": rs_id, "rs_ip": rs_ip, "rs_port": rs_port}
            ],
            "command": [
                {"query": query_command, "return": return_command}
            ],
            "decode": [
                {"d_order": dorder, "d_num": dnum, "d_name": dname, "d_range": drange, "d_compute": dcompute, "d_unit": unit}
            ],
            "forward": [
                {"f_ip": turn_ip, "f_port": turn_port, "f_timeout": timeout, "f_path": turn_path}
            ]
        }
    # save_sensor_path = "E:\\pythonProject5\\" + sname + ".json"
    with open(save_sensor_path, 'w') as file:
        json.dump(s_data, file, ensure_ascii=False, indent=4)


def import_sensor_Data(save_sensor_path):
    with open(save_sensor_path, 'r') as f:
        data = json.load(f)
        sid = data["sensor"][0]["s_id"]
        sname = data["sensor"][0]["s_name"]
        slocation = data["sensor"][0]["s_location"]
        frequency = data["sensor"][0]["s_rate"]
        sdate = data["sensor"][0]["s_date"]
        so = data["sensor"][0]["s_remark"]
        sport = data["sensor"][0]["s_port"]
        path = data["sensor"][0]["path"]
        baurd = data["sensor"][0]["s_baurd"]
        data_bit = data["sensor"][0]["s_data"]
        stop_bit = data["sensor"][0]["s_stop"]
        check_bit = data["sensor"][0]["s_check"]
        rs_id = data["sensor"][0]["rs_id"]
        rs_ip = data["sensor"][0]["rs_ip"]
        rs_port = data["sensor"][0]["rs_port"]
        query_command = data["command"][0]["query"]
        return_command = data["command"][0]["return"]
        d_order = data["decode"][0]["d_order"]
        d_num = data["decode"][0]["d_num"]
        d_name = data["decode"][0]["d_name"]
        d_range = data["decode"][0]["d_range"]
        d_compute = data["decode"][0]["d_compute"]
        d_unit = data["decode"][0]["d_unit"]
        target = data["forward"][0]["f_target"]
        turn_ip = data["forward"][0]["f_ip"]
        turn_port = data["forward"][0]["f_port"]
        timeout = data["forward"][0]["f_timeout"]
        turn_path = data["forward"][0]["f_path"]

    return sid, sname, slocation, frequency, sdate, so, path, sport, baurd, data_bit, stop_bit, check_bit, rs_id, \
        rs_ip, rs_port, query_command, return_command, d_order, d_num, d_name, d_range, d_compute, d_unit, \
        target, turn_ip, turn_port, timeout, turn_path
