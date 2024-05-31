# -*- coding: utf-8 -*-
import json
import sqlite3
import threading
from time import strftime
from PyQt5.QtCore import QDate, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QTableWidgetItem, QFileDialog, \
    QTableWidget, QAbstractItemView
from PyQt5.QtGui import QPixmap
import sys

from json_save import save_sensor_Data, import_sensor_Data
from mainwindow import Ui_MainWindow
from sensor_widget import Ui_sensor
from PyQt5 import QtCore
from c_send import *
from data_recv import recv_data
from c_recv import Socket_Recv
from move import move_json_files
from show_widget import Ui_Form

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)


class MainWindow(QMainWindow, Ui_MainWindow):
    _signal_path = QtCore.pyqtSignal(str)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.resize(1000, 800)
        self.swidget = sensor_widget()
        self.showwindow = show_widget()
        self.tableWidget_page4.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget_page4.setSelectionMode(QTableWidget.SingleSelection)
        self.tableWidget_page4.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.treeWidget.itemClicked.connect(self.on_tree_item_clicked)
        self.label_picture.setPixmap(QPixmap(r'C:\Users\DELL\Desktop\zx'))
        self.pushButton_cnn.clicked.connect(self.socket_connect)
        self.pushButton_close.clicked.connect(self.socket_close)
        self.pushButton_2apply.clicked.connect(self.iotE_apply)
        self.pushButton_4add.clicked.connect(self.signal_recive)
        self.pushButton_4edit.clicked.connect(self.edit_table)
        self.pushButton_4delet.clicked.connect(self.delete_item)
        self.pushButton_4import.clicked.connect(self.import_tabledata)
        self.pushButton_effctive.clicked.connect(self.showwindow.show)
        self.pushButton_5import.clicked.connect(self.import_project)
        self.pushButton_5save.clicked.connect(self.save_files)
        self.pushButton_5fetch.clicked.connect(self.fetch_parameter)

    def on_tree_item_clicked(self, item):
        if item.text(0) == "连接iotE":
            self.stackedWidget.setCurrentIndex(0)
        elif item.text(0) == "基本信息":
            self.stackedWidget.setCurrentIndex(1)
        elif item.text(0) == "服务状态":
            self.stackedWidget.setCurrentIndex(2)
        elif item.text(0) == "输入设备":
            self.stackedWidget.setCurrentIndex(3)
        elif item.text(0) == "功能":
            self.stackedWidget.setCurrentIndex(4)
        elif item.text(0) == "输入数据":
            self.showwindow.show()
        elif item.text(0) == "示意图":
            self.stackedWidget.setCurrentIndex(6)
        elif item.text(0) == "关于":
            self.stackedWidget.setCurrentIndex(7)

    def socket_connect(self):
        iot_ip = self.textEdit_ip.toPlainText()
        iot_port = self.textEdit_port.toPlainText()
        self.socket = Socket_Client(iot_ip, int(iot_port))
        if self.socket.connect:
            self.textBrowser_state.setText("连接成功")
        else:
            self.textBrowser_state.setText("连接失败")

    def socket_close(self):
        if self.socket:
            self.socket.disconnect()
            self.textBrowser_state.setText("已关闭")
        else:
            self.textBrowser_state.setText("未连接")

    def iotE_apply(self):
        iot_ip = self.textEdit_ip.toPlainText()
        iot_port = self.textEdit_port.toPlainText()
        iot_path = self.comboBox_SC.currentText()
        iot_id = self.textEdit_id.toPlainText()
        iot_project = self.textEdit_project.toPlainText()
        iot_lct1 = self.textEdit_location1.toPlainText()
        iot_lct2 = self.textEdit_location2.toPlainText()
        iot_date = self.dateEdit.date().toString("yyyy-MM-dd")
        iot_remark = self.textEdit_remark.toPlainText()
        self.project_path = os.path.join(r'E:\hyd_project', iot_project)
        path = os.path.join(self.project_path, "iot_information.json")
        try:
            os.makedirs(self.project_path, exist_ok=True)
            print(f"Directory '{self.project_path}' created successfully.")
        except OSError as e:
            print(f"Error: {e.strerror}")
            return None
        iotE_data = {
            "iotE": [
                {"ip": iot_ip, "port": iot_port, "path": iot_path, "id": iot_id, "project": iot_project,
                 "location1": iot_lct1, "location2": iot_lct2, "Activation_date": iot_date, "remark": iot_remark}
            ]
        }
        try:
            with open(path, 'w') as file:
                json.dump(iotE_data, file, ensure_ascii=False, indent=4)
            print(f"JSON data written to '{path}' successfully.")
        except IOError as e:
            print(f"Error writing to file: {e.strerror}")
            return None
        try:
            self.client = Socket_Client(iot_ip, int(iot_port))
        except ValueError:
            print("Invalid port number.")
            return None
        if self.client.connect():
            if self.client.send_files([path]):
                QMessageBox.information(self, "Success", "Files sent successfully.")
            else:
                print("Failed to send files.")
        else:
            print("Failed to connect to the server.")

    def iotE_import(self, file_path):
        if file_path:
            with open(file_path, 'r') as f:
                data = json.load(f)
                iot_ip = data["iotE"][0]["ip"]
                iot_port = data["iotE"][0]["port"]
                iot_path = data["iotE"][0]["path"]
                iot_id = data["iotE"][0]["id"]
                iot_project = data["iotE"][0]["project"]
                iot_lct1 = data["iotE"][0]["location1"]
                iot_lct2 = data["iotE"][0]["location2"]
                iot_date = data["iotE"][0]["Activation_date"]
                iot_remark = data["iotE"][0]["remark"]
            self.textEdit_ip.setText(iot_ip)
            self.textEdit_port.setText(iot_port)
            index = self.comboBox_SC.findText(iot_path)
            if index != -1:
                self.comboBox_SC.setCurrentIndex(index)
            self.textEdit_id.setText(iot_id)
            self.textEdit_project.setText(iot_project)
            self.textEdit_location1.setText(iot_lct1)
            self.textEdit_location2.setText(iot_lct2)
            self.dateEdit.setDate(QDate.fromString(iot_date, "yyyy-MM-dd"))
            self.textEdit_remark.setText(iot_remark)
        else:
            self.close()

    def signal_recive(self):
        if not hasattr(self, '_connected'):
            self.swidget._signal.connect(self.add_table)
            self._connected = True
        self.swidget.clear_data()
        self.swidget.show()

    def add_table(self, signal_path):
        file_path = signal_path
        self.swidget.show()
        with open(file_path, 'r') as f:
            data = json.load(f)
            sensor_info = data.get("sensor", [{}])[0]
            sid = sensor_info.get("s_id", "")
            sname = sensor_info.get("s_name", "")
            slocation = sensor_info.get("s_location", "")
            frequency = sensor_info.get("s_rate", "")
            sdate = sensor_info.get("s_date", "")
            so = sensor_info.get("s_remark", "")
        row_count = self.tableWidget_page4.rowCount()
        self.tableWidget_page4.insertRow(row_count)
        item1 = QTableWidgetItem(sid)
        item2 = QTableWidgetItem(sname)
        item3 = QTableWidgetItem(slocation)
        item4 = QTableWidgetItem(frequency)
        item5 = QTableWidgetItem(sdate)
        item6 = QTableWidgetItem(so)
        self.tableWidget_page4.setItem(row_count, 0, item1)
        self.tableWidget_page4.setItem(row_count, 1, item2)
        self.tableWidget_page4.setItem(row_count, 2, item3)
        self.tableWidget_page4.setItem(row_count, 3, item4)
        self.tableWidget_page4.setItem(row_count, 4, item5)
        self.tableWidget_page4.setItem(row_count, 5, item6)

    def edit_table(self):
        select_row = self.tableWidget_page4.currentRow()
        if select_row < 0:
            QMessageBox.warning(self, "Warning", "No row selected")
            return
        name = self.tableWidget_page4.item(select_row, 2).text()
        path = os.path.join(r"E:\hyd_project\temporary_files", name + ".json")
        self._signal_path.emit(path)
        self.swidget.show()
        self.swidget.signal_recv()

    def delete_item(self):
        current_row = self.tableWidget_page4.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Warning", "No row selected")
            return
        reply = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to delete the selected row?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.tableWidget_page4.removeRow(current_row)

    def import_tabledata(self):
        file_paths, _ = QFileDialog.getOpenFileNames(self, "Open JSON File", "", "JSON Files (*.json)")
        self.import_data(file_paths)

    def import_data(self, file_paths):
        if file_paths:
            for path in file_paths:
                with open(path, 'r') as f:
                    data = json.load(f)
                    sensor_info = data.get("sensor", [{}])[0]
                    sid = sensor_info.get("s_id", "")
                    sname = sensor_info.get("s_name", "")
                    slocation = sensor_info.get("s_location", "")
                    frequency = sensor_info.get("s_rate", "")
                    sdate = sensor_info.get("s_date", "")
                    so = sensor_info.get("s_remark", "")
                    self.import_sensor_data(sid, sname, slocation, frequency, sdate, so)
        else:
            self.close()

    def import_sensor_data(self, sid, sname, slocation, frequency, sdate, so):
        row_count = self.tableWidget_page4.rowCount()
        found = False
        for i in range(row_count):
            if sname == self.tableWidget_page4.item(i, 1).text():
                row_update = i
                found = True
                break
        if found:
            reply = QMessageBox.question(self, 'Replace', f'"{sname}" already exists. Do you want to replace it?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                for j in range(6):
                    self.tableWidget_page4.setItem(row_update, j, QTableWidgetItem(""))
            elif reply == QMessageBox.No:
                row_update = row_count
                self.tableWidget_page4.insertRow(row_update)
        if not found:
            row_update = row_count
            self.tableWidget_page4.insertRow(row_update)

        item1 = QTableWidgetItem(sid)
        item2 = QTableWidgetItem(sname)
        item3 = QTableWidgetItem(slocation)
        item4 = QTableWidgetItem(frequency)
        item5 = QTableWidgetItem(sdate)
        item6 = QTableWidgetItem(so)
        self.tableWidget_page4.setItem(row_update, 0, item1)
        self.tableWidget_page4.setItem(row_update, 1, item2)
        self.tableWidget_page4.setItem(row_update, 2, item3)
        self.tableWidget_page4.setItem(row_update, 3, item4)
        self.tableWidget_page4.setItem(row_update, 4, item5)
        self.tableWidget_page4.setItem(row_update, 5, item6)

    def fetch_parameter(self):
        ip = '192.168.1.125'
        fetch_path = r'E:\fetch'
        port2 = 2
        self.recv_socket = Socket_Recv(ip, port2, fetch_path)
        if self.recv_socket.connect():
            self.recv_socket.receive_files()
            QMessageBox.information(self, "Success", "Files received successfully.")
        else:
            print("Failed to connect to the server.")

    def import_project(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            folder_path = os.path.normpath(folder_path)
            files = os.listdir(folder_path)
            for file in files:
                file_path = os.path.join(folder_path, file)
                file_path = os.path.abspath(file_path)
                try:
                    if file == "iot_information.json":
                        self.iotE_import(file_path)
                    else:
                        self.import_data([file_path])
                except Exception as e:
                    print(f"Error processing file {file}: {e}")
        else:
            print("No folder selected.")

    def save_files(self):
        source_folder = r'E:\hyd_project\temporary_files'
        destination_folder = self.project_path
        move_json_files(source_folder, destination_folder)


class sensor_widget(QWidget, Ui_sensor):
    _signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(sensor_widget, self).__init__()
        self.setupUi(self)
        self.pushButton_save.clicked.connect(self.save_data)

    def clear_data(self):
        self.SID.clear()
        self.Sname.clear()
        self.Slocation.clear()
        self.SADC.clear()
        self.Sothers.clear()
        self.Sport.clear()
        self.baurd.clear()
        self.Sport.clear()
        self.baurd.clear()
        self.data_bit.clear()
        self.stop_bit.clear()
        self.check_bit.clear()
        self.RS_ID.clear()
        self.RS_IP.clear()
        self.RS_port.clear()
        self.query_command.clear()
        self.return_command.clear()
        self.turn_ip.clear()
        self.turn_port.clear()
        self.timeout.clear()
        self.turn_path.clear()
        self.order.clear()
        self.dnum.clear()
        self.dname.clear()
        self.drange.clear()
        self.dcompute.clear()
        self.textEdit_unit.clear()

    def save_data(self):
        sname = self.Sname.toPlainText()
        QMessageBox.question(self, '保存', '是否确定保存文件', QMessageBox.Yes | QMessageBox.No)
        file_path = os.path.join(r'E:\hyd_project\temporary_files', sname + ".json")
        sid = self.SID.toPlainText()
        slocation = self.Slocation.toPlainText()
        frequency = self.SADC.toPlainText()
        sdate = self.Sdata.date().toString("yyyy-MM-dd")
        so = self.Sothers.toPlainText()
        path1 = self.modbus.isChecked()
        path2 = self.socket.isChecked()
        sport = self.Sport.toPlainText()
        baurd = self.baurd.toPlainText()
        data_bit = self.data_bit.toPlainText()
        stop_bit = self.stop_bit.toPlainText()
        check_bit = self.check_bit.toPlainText()
        rs_id = self.RS_ID.toPlainText()
        rs_ip = self.RS_IP.toPlainText()
        rs_port = self.RS_port.toPlainText()
        query_command = self.query_command.toPlainText()
        return_command = self.return_command.toPlainText()
        turn_ip = self.turn_ip.toPlainText()
        turn_port = self.turn_port.toPlainText()
        timeout = self.timeout.toPlainText()
        turn_path = self.turn_path.toPlainText()
        dorder = self.order.currentText()
        dnum = self.dnum.toPlainText()
        dname = self.dname.toPlainText()
        drange = self.drange.toPlainText()
        dcompute = self.dcompute.toPlainText()
        dunit = self.textEdit_unit.toPlainText()
        if path1:
            path = self.modbus.text()
        elif path2:
            path = self.socket.text()
        else:
            path = ''

        save_sensor_Data(sid, sname, slocation, frequency, sdate, so, path, sport, baurd, data_bit, stop_bit, check_bit,
                         rs_id, rs_ip, rs_port, query_command, return_command, turn_ip, turn_port, timeout,
                         turn_path, file_path, dorder, dnum, dname, drange, dcompute, dunit)
        QMessageBox.information(self, "Success", "Data saved successfully.")
        self._signal.emit(file_path)
        self.close()

    def signal_recv(self):
        main_window._signal_path.connect(self.import_data)

    def import_data(self, path):
        file_path = path
        if file_path:
            sid, sname, slocation, frequency, sdate, so, path, sport, baurd, data_bit, stop_bit, check_bit, rs_id, \
                rs_ip, rs_port, query_command, return_command, d_order, d_num, d_name, d_range, d_compute, d_unit, \
                target, turn_ip, turn_port, timeout, turn_path = import_sensor_Data(file_path)
            self.SID.setText(sid)
            self.Sname.setText(sname)
            self.Slocation.setText(slocation)
            self.SADC.setText(frequency)
            self.Sdata.setDate(QDate.fromString(sdate, "yyyy-MM-dd"))
            self.Sothers.setText(so)
            self.Sport.toPlainText(sport)
            self.baurd.toPlainText(baurd)
            if path == "串口通信":
                self.modbus.setChecked(True)
            elif path == "网口通信":
                self.socket.setChecked(True)
            self.Sport.toPlainText(sport)
            self.baurd.toPlainText(baurd)
            self.data_bit.toPlainText(data_bit)
            self.stop_bit.toPlainText(stop_bit)
            self.check_bit.toPlainText(check_bit)
            self.RS_ID.toPlainText(rs_id)
            self.RS_IP.toPlainText(rs_ip)
            self.RS_port.toPlainText(rs_port)
            self.query_command.toPlainText(query_command)
            self.return_command.toPlainText(return_command)
            self.turn_ip.toPlainText(turn_ip)
            self.turn_port.toPlainText(turn_port)
            self.timeout.toPlainText(timeout)
            self.turn_path.toPlainText(turn_path)
            self.order.currentText(d_order)
            self.dnum.toPlainText(d_num)
            self.dname.toPlainText(d_name)
            self.drange.toPlainText(d_range)
            self.dcompute.toPlainText(d_compute)
            self.textEdit_unit.toPlinText(d_unit)
        else:
            QMessageBox.warning(self, "Warning", "Cannot find file")


class show_widget(QWidget, Ui_Form):
    def __init__(self):
        super(show_widget, self).__init__()
        self.setupUi(self)
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.recv_thread = threading.Thread(target=self.update_table_from_recv_data)
        self.recv_thread.start()

    def send_files(self):
        send_paths, _ = QFileDialog.getOpenFileNames(self, "Open JSON Files", "", "JSON Files (*.json)")
        if send_paths:
            reply = QMessageBox.question(self, '选择', '是否确定发送这些文件', QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.send_data(send_paths)

    def send_data(self, paths):
        self.client = Socket_Client('192.168.1.125', 1)
        if self.client.connect():
            if self.client.send_files(paths):
                QMessageBox.information(self, "Success", "Files sent successfully.")
        else:
            print("Failed to connect to the server.")

    def update_table_from_recv_data(self):
        while True:
            rdata = recv_data()
            self.update_table(rdata)

    def update_table(self, rdata):
        project, num, name, sid, location, data = rdata
        self.textBrowser_6data.setText(f'项目：{project}   {num}个设备')

        current_time = strftime("%H:%M:%S")

        existing_row = None
        for row in range(self.tableWidget_page6.rowCount()):
            item = self.tableWidget_page6.item(row, 1)
            if item is not None and item.text() == sid:
                existing_row = row
                break

        if existing_row is None:
            existing_row = self.tableWidget_page6.rowCount()
            self.tableWidget_page6.insertRow(existing_row)

        self.tableWidget_page6.setItem(existing_row, 0, QTableWidgetItem(name))
        self.tableWidget_page6.setItem(existing_row, 1, QTableWidgetItem(sid))
        self.tableWidget_page6.setItem(existing_row, 2, QTableWidgetItem(location))
        self.tableWidget_page6.setItem(existing_row, 3, QTableWidgetItem(data))
        self.tableWidget_page6.setItem(existing_row, 4, QTableWidgetItem(current_time))

    def db(self):
        db_file = 'sensor_data.db'

        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS sensor_data
                          (编号 REAL,
                           传感器 REAL,
                           位置 REAL,
                           数据 REAL,
                           timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()
        conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    s_window = sensor_widget()
    main_window.show()
    sys.exit(app.exec_())
