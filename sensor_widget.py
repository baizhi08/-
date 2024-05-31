# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sensor_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sensor(object):
    def setupUi(self, sensor):
        sensor.setObjectName("sensor")
        sensor.resize(767, 676)
        sensor.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(74, 147, 221)")
        self.layoutWidget = QtWidgets.QWidget(sensor)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 741, 651))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 12, 6, 1, 1)
        self.turn_ip_3 = QtWidgets.QTextEdit(self.layoutWidget)
        self.turn_ip_3.setObjectName("turn_ip_3")
        self.gridLayout.addWidget(self.turn_ip_3, 14, 2, 1, 1)
        self.data_bit = QtWidgets.QTextEdit(self.layoutWidget)
        self.data_bit.setObjectName("data_bit")
        self.gridLayout.addWidget(self.data_bit, 4, 4, 1, 1)
        self.socket = QtWidgets.QRadioButton(self.layoutWidget)
        self.socket.setObjectName("socket")
        self.gridLayout.addWidget(self.socket, 5, 1, 2, 1)
        self.label_33 = QtWidgets.QLabel(self.layoutWidget)
        self.label_33.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.label_33.setObjectName("label_33")
        self.gridLayout.addWidget(self.label_33, 3, 3, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.layoutWidget)
        self.label_37.setStyleSheet("font-family: Times New Roman ;\n"
"background-color: rgb(227, 227, 227);")
        self.label_37.setObjectName("label_37")
        self.gridLayout.addWidget(self.label_37, 5, 4, 1, 1)
        self.RS_port = QtWidgets.QTextEdit(self.layoutWidget)
        self.RS_port.setObjectName("RS_port")
        self.gridLayout.addWidget(self.RS_port, 6, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 9, 5, 1, 1)
        self.modbus = QtWidgets.QRadioButton(self.layoutWidget)
        self.modbus.setStyleSheet("")
        self.modbus.setObjectName("modbus")
        self.gridLayout.addWidget(self.modbus, 3, 1, 2, 1)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 13, 6, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.layoutWidget)
        self.label_42.setStyleSheet("font-family: Times New Roman ;\n"
"background-color: rgb(227, 227, 227);")
        self.label_42.setObjectName("label_42")
        self.gridLayout.addWidget(self.label_42, 12, 3, 1, 1)
        self.return_command = QtWidgets.QTextEdit(self.layoutWidget)
        self.return_command.setObjectName("return_command")
        self.gridLayout.addWidget(self.return_command, 8, 1, 1, 6)
        self.dname = QtWidgets.QTextEdit(self.layoutWidget)
        self.dname.setObjectName("dname")
        self.gridLayout.addWidget(self.dname, 10, 3, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget)
        self.label_29.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 1, 2, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.layoutWidget)
        self.label_44.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.label_44.setObjectName("label_44")
        self.gridLayout.addWidget(self.label_44, 12, 5, 1, 1)
        self.turn_port = QtWidgets.QTextEdit(self.layoutWidget)
        self.turn_port.setObjectName("turn_port")
        self.gridLayout.addWidget(self.turn_port, 13, 3, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget)
        self.label_28.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 1, 6, 1, 1)
        self.dnum = QtWidgets.QTextEdit(self.layoutWidget)
        self.dnum.setObjectName("dnum")
        self.gridLayout.addWidget(self.dnum, 10, 2, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.layoutWidget)
        self.label_30.setStyleSheet("background-color: rgb(227, 227, 227);\n"
"font: 12pt \"华文宋体\";")
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 1, 1, 1, 1)
        self.dcompute = QtWidgets.QTextEdit(self.layoutWidget)
        self.dcompute.setObjectName("dcompute")
        self.gridLayout.addWidget(self.dcompute, 10, 5, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget)
        self.label_20.setStyleSheet("background-color: rgb(220, 242, 255);\n"
"font: 14pt \"华文中宋\";\n"
"color: rgb(57, 57, 57);\n"
"")
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 1, 0, 2, 1)
        self.label_43 = QtWidgets.QLabel(self.layoutWidget)
        self.label_43.setStyleSheet("font-family: Times New Roman ;\n"
"background-color: rgb(227, 227, 227);")
        self.label_43.setObjectName("label_43")
        self.gridLayout.addWidget(self.label_43, 12, 4, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget)
        self.label_24.setStyleSheet("background-color: rgb(220, 242, 255);\n"
"font: 14pt \"华文中宋\";\n"
"color: rgb(57, 57, 57);\n"
"")
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 9, 0, 2, 1)
        self.RS_IP = QtWidgets.QTextEdit(self.layoutWidget)
        self.RS_IP.setObjectName("RS_IP")
        self.gridLayout.addWidget(self.RS_IP, 6, 3, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.layoutWidget)
        self.label_31.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 1, 3, 1, 1)
        self.textEdit_3 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout.addWidget(self.textEdit_3, 14, 6, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 13, 1, 1, 1)
        self.SID = QtWidgets.QTextEdit(self.layoutWidget)
        self.SID.setObjectName("SID")
        self.gridLayout.addWidget(self.SID, 2, 1, 1, 1)
        self.turn_ip = QtWidgets.QTextEdit(self.layoutWidget)
        self.turn_ip.setObjectName("turn_ip")
        self.gridLayout.addWidget(self.turn_ip, 13, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 9, 2, 1, 1)
        self.SADC = QtWidgets.QTextEdit(self.layoutWidget)
        self.SADC.setObjectName("SADC")
        self.gridLayout.addWidget(self.SADC, 2, 4, 1, 1)
        self.order = QtWidgets.QComboBox(self.layoutWidget)
        self.order.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.order.setObjectName("order")
        self.order.addItem("")
        self.order.addItem("")
        self.gridLayout.addWidget(self.order, 10, 1, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.layoutWidget)
        self.label_38.setStyleSheet("font-family: Times New Roman ;\n"
"background-color: rgb(227, 227, 227);")
        self.label_38.setObjectName("label_38")
        self.gridLayout.addWidget(self.label_38, 5, 3, 1, 1)
        self.Slocation = QtWidgets.QTextEdit(self.layoutWidget)
        self.Slocation.setObjectName("Slocation")
        self.gridLayout.addWidget(self.Slocation, 2, 3, 1, 1)
        self.Sdata = QtWidgets.QDateEdit(self.layoutWidget)
        self.Sdata.setStyleSheet("border:  solid rgb(107, 151, 255);")
        self.Sdata.setObjectName("Sdata")
        self.gridLayout.addWidget(self.Sdata, 2, 5, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.layoutWidget)
        self.label_36.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.label_36.setObjectName("label_36")
        self.gridLayout.addWidget(self.label_36, 3, 6, 1, 1)
        self.turn_port_3 = QtWidgets.QTextEdit(self.layoutWidget)
        self.turn_port_3.setObjectName("turn_port_3")
        self.gridLayout.addWidget(self.turn_port_3, 14, 3, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget)
        self.label_27.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 1, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 9, 4, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.layoutWidget)
        self.label_32.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 3, 4, 1, 1)
        self.baurd = QtWidgets.QTextEdit(self.layoutWidget)
        self.baurd.setObjectName("baurd")
        self.gridLayout.addWidget(self.baurd, 4, 3, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.layoutWidget)
        self.label_39.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.label_39.setObjectName("label_39")
        self.gridLayout.addWidget(self.label_39, 5, 2, 1, 1)
        self.timeout_3 = QtWidgets.QTextEdit(self.layoutWidget)
        self.timeout_3.setObjectName("timeout_3")
        self.gridLayout.addWidget(self.timeout_3, 14, 4, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget)
        self.label_21.setStyleSheet("background-color: rgb(220, 242, 255);\n"
"font: 14pt \"华文中宋\";\n"
"color: rgb(57, 57, 57);\n"
"")
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 3, 0, 4, 1)
        self.drange = QtWidgets.QTextEdit(self.layoutWidget)
        self.drange.setObjectName("drange")
        self.gridLayout.addWidget(self.drange, 10, 4, 1, 1)
        self.turn_path_3 = QtWidgets.QTextEdit(self.layoutWidget)
        self.turn_path_3.setObjectName("turn_path_3")
        self.gridLayout.addWidget(self.turn_path_3, 14, 5, 1, 1)
        self.query_command = QtWidgets.QTextEdit(self.layoutWidget)
        self.query_command.setObjectName("query_command")
        self.gridLayout.addWidget(self.query_command, 7, 1, 1, 6)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 9, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("background-color: rgb(220, 242, 255);\n"
"font: 14pt \"华文中宋\";\n"
"color: rgb(57, 57, 57);\n"
"")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 12, 0, 3, 1)
        self.RS_ID = QtWidgets.QTextEdit(self.layoutWidget)
        self.RS_ID.setObjectName("RS_ID")
        self.gridLayout.addWidget(self.RS_ID, 6, 2, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.layoutWidget)
        self.label_35.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.label_35.setObjectName("label_35")
        self.gridLayout.addWidget(self.label_35, 3, 2, 1, 1)
        self.stop_bit = QtWidgets.QTextEdit(self.layoutWidget)
        self.stop_bit.setObjectName("stop_bit")
        self.gridLayout.addWidget(self.stop_bit, 4, 5, 1, 1)
        self.Sport = QtWidgets.QTextEdit(self.layoutWidget)
        self.Sport.setObjectName("Sport")
        self.gridLayout.addWidget(self.Sport, 4, 2, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget)
        self.label_26.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 1, 5, 1, 1)
        self.Sothers = QtWidgets.QTextEdit(self.layoutWidget)
        self.Sothers.setObjectName("Sothers")
        self.gridLayout.addWidget(self.Sothers, 2, 6, 1, 1)
        self.check_bit = QtWidgets.QTextEdit(self.layoutWidget)
        self.check_bit.setObjectName("check_bit")
        self.gridLayout.addWidget(self.check_bit, 4, 6, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget)
        self.label_22.setStyleSheet("background-color: rgb(220, 242, 255);\n"
"font: 14pt \"华文中宋\";\n"
"color: rgb(57, 57, 57);\n"
"")
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 7, 0, 1, 1)
        self.timeout = QtWidgets.QTextEdit(self.layoutWidget)
        self.timeout.setObjectName("timeout")
        self.gridLayout.addWidget(self.timeout, 13, 4, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.layoutWidget)
        self.label_34.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.label_34.setObjectName("label_34")
        self.gridLayout.addWidget(self.label_34, 3, 5, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.layoutWidget)
        self.label_41.setStyleSheet("font-family: Times New Roman ;\n"
"background-color: rgb(227, 227, 227);")
        self.label_41.setObjectName("label_41")
        self.gridLayout.addWidget(self.label_41, 12, 2, 1, 1)
        self.turn_path = QtWidgets.QTextEdit(self.layoutWidget)
        self.turn_path.setObjectName("turn_path")
        self.gridLayout.addWidget(self.turn_path, 13, 5, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget)
        self.label_25.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 9, 1, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.layoutWidget)
        self.label_40.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.label_40.setObjectName("label_40")
        self.gridLayout.addWidget(self.label_40, 12, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget)
        self.label_23.setStyleSheet("background-color: rgb(220, 242, 255);\n"
"font: 14pt \"华文中宋\";\n"
"color: rgb(57, 57, 57);\n"
"")
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 8, 0, 1, 1)
        self.pushButton_save = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_save.setStyleSheet("background-color: rgb(57, 79, 131);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"黑体\";")
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout.addWidget(self.pushButton_save, 15, 2, 1, 1)
        self.pushButton_test = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_test.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_test.setStyleSheet("background-color: rgb(57, 79, 131);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"黑体\";")
        self.pushButton_test.setObjectName("pushButton_test")
        self.gridLayout.addWidget(self.pushButton_test, 15, 3, 1, 1)
        self.Sname = QtWidgets.QTextEdit(self.layoutWidget)
        self.Sname.setObjectName("Sname")
        self.gridLayout.addWidget(self.Sname, 2, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 14, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 9, 6, 1, 1)
        self.textEdit_unit = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_unit.setObjectName("textEdit_unit")
        self.gridLayout.addWidget(self.textEdit_unit, 10, 6, 1, 1)

        self.retranslateUi(sensor)
        QtCore.QMetaObject.connectSlotsByName(sensor)

    def retranslateUi(self, sensor):
        _translate = QtCore.QCoreApplication.translate
        sensor.setWindowTitle(_translate("sensor", "Form"))
        self.label_3.setText(_translate("sensor", "是否启用"))
        self.data_bit.setHtml(_translate("sensor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.socket.setText(_translate("sensor", "网口通信"))
        self.label_33.setText(_translate("sensor", "波特率"))
        self.label_37.setText(_translate("sensor", "Port"))
        self.label_6.setText(_translate("sensor", "量程"))
        self.modbus.setText(_translate("sensor", "串口通信"))
        self.label_42.setText(_translate("sensor", "Port"))
        self.return_command.setHtml(_translate("sensor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.dname.setHtml(_translate("sensor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana\';\">nam1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana\';\">nam2</span></p></body></html>"))
        self.label_29.setText(_translate("sensor", "名称"))
        self.label_44.setText(_translate("sensor", "连接协议"))
        self.label_28.setText(_translate("sensor", "备注"))
        self.label_30.setText(_translate("sensor", "编号"))
        self.label_20.setText(_translate("sensor", "基本信息"))
        self.label_43.setText(_translate("sensor", "Time Out"))
        self.label_24.setText(_translate("sensor", "解析参数"))
        self.label_31.setText(_translate("sensor", "部署详细位置"))
        self.label.setText(_translate("sensor", "1"))
        self.label_7.setText(_translate("sensor", "数据数量"))
        self.order.setItemText(0, _translate("sensor", "高"))
        self.order.setItemText(1, _translate("sensor", "低"))
        self.label_38.setText(_translate("sensor", "IP"))
        self.label_36.setText(_translate("sensor", "校验位"))
        self.label_27.setText(_translate("sensor", " 采集周期"))
        self.label_5.setText(_translate("sensor", "数据位置"))
        self.label_32.setText(_translate("sensor", "数据位"))
        self.baurd.setHtml(_translate("sensor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_39.setText(_translate("sensor", "串口服务器编号"))
        self.label_21.setText(_translate("sensor", "接口参数     "))
        self.drange.setHtml(_translate("sensor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana\';\">4,5</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana\';\">5,6</span></p></body></html>"))
        self.query_command.setHtml(_translate("sensor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.label_2.setText(_translate("sensor", "数据名字"))
        self.label_4.setText(_translate("sensor", "数据转发"))
        self.label_35.setText(_translate("sensor", "串口号"))
        self.stop_bit.setHtml(_translate("sensor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_26.setText(_translate("sensor", "启用日期"))
        self.Sothers.setHtml(_translate("sensor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana\';\">无</span></p></body></html>"))
        self.check_bit.setHtml(_translate("sensor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_22.setText(_translate("sensor", "查询指令"))
        self.label_34.setText(_translate("sensor", "停止位"))
        self.label_41.setText(_translate("sensor", "IP"))
        self.label_25.setText(_translate("sensor", "高/低位"))
        self.label_40.setText(_translate("sensor", "转发目标"))
        self.label_23.setText(_translate("sensor", "返回指令"))
        self.pushButton_save.setText(_translate("sensor", "保存"))
        self.pushButton_test.setText(_translate("sensor", "测试"))
        self.label_9.setText(_translate("sensor", "2"))
        self.label_8.setText(_translate("sensor", "单位"))
