import os

import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut, QWidget
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from playsound import playsound


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(905, 541)
        Form.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), "
            "stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "font: 75 italic 12pt \"Times New Roman\";")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Инструкция"))
        self.textBrowser.setHtml(_translate("Form",
                                            "<!DOCTYPE HTML "
                                            "PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org"
                                            "/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><"
                                            "style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Times New Roman\';"
                                            " font-size:12pt; font-weight:72; font-style:italic;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;"
                                            " margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                                            "Данная программа предназначена "
                                            "для изучения аккордов на 6-ти струнной гитаре.</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;"
                                            " margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Для выбора "
                                            "аккорда нажмите соответствующую клавишу на клавиатуре:</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">С - "
                                            "аккорд C (до);</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">D - "
                                            "аккорд D (ре);</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;"
                                            " margin-right:0px; -qt-block-indent:0; text-indent:0px;\">E - "
                                            "аккорд E (ми);</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; "
                                            "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                            "text-indent:0px;\">F - аккорд F (фа);</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">G - "
                                            "аккорд G (соль);</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A - "
                                            "аккорд A (ля);</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">H - "
                                            "аккорд H (си);</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;"
                                            " margin-right:0px; -qt-block-indent:0; text-indent:0px;\">M - выбор "
                                            "минорности (мажорности) аккорда; </p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Выбранный "
                                            "вами аккорд отобразится на виртуальном грифе, а его название появится "
                                            "в специальном поле (Выбранный аккорд:).</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Для "
                                            "проигрывания струны (струн) выбранного аккорда нажмите соответствующую "
                                            "клавишу на клавиатуре:</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 - "
                                            "первая струна;</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 - "
                                            "вторая струна;</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 - "
                                            "третья струна;</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 - "
                                            "четвертая струна;</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 - "
                                            "пятая струна;</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 - "
                                            "шестая струна;</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PageUp "
                                            "- удар по всем струнам вверх;</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PageDown "
                                            "- удар по всем струнам вниз.</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Струна "
                                            "(струны), проигранная вами, подсветится на виртуальном грифе.</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                            "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                            "text-indent:0px;\"><br /></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px;"
                                            " margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                            "text-indent:0px;\"><br /></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px;"
                                            " margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                            "text-indent:0px;\"><br /></p></body></html>"))


class InstructionWidget(QWidget, Ui_Form):
    def __init__(self):
        super(InstructionWidget, self).__init__()
        self.setupUi(self)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1386, 422)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255),"
            " stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 1371, 196))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                 "font: 12pt \"MS Shell Dlg 2\";\n"
                                 "font: 10pt \"MS Shell Dlg 2\";\n"
                                 "color: rgb(85, 255, 127);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                   "color: rgb(0, 255, 0);")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_26.setEnabled(False)
        self.pushButton_26.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_26.setText("")
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout.addWidget(self.pushButton_26, 2, 2, 1, 1)
        self.pushButton_43 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_43.setEnabled(False)
        self.pushButton_43.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_43.setText("")
        self.pushButton_43.setObjectName("pushButton_43")
        self.gridLayout.addWidget(self.pushButton_43, 3, 3, 1, 1)
        self.pushButton_52 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_52.setEnabled(False)
        self.pushButton_52.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_52.setText("")
        self.pushButton_52.setObjectName("pushButton_52")
        self.gridLayout.addWidget(self.pushButton_52, 3, 6, 1, 1)
        self.pushButton_38 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_38.setEnabled(False)
        self.pushButton_38.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_38.setText("")
        self.pushButton_38.setObjectName("pushButton_38")
        self.gridLayout.addWidget(self.pushButton_38, 4, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "color: rgb(0, 255, 0);")
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 6, 10, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setEnabled(False)
        self.pushButton_10.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 0, 9, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setEnabled(False)
        self.pushButton_8.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                        "color: rgb(0, 255, 0);")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 0, 7, 1, 1)
        self.pushButton_32 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_32.setEnabled(False)
        self.pushButton_32.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_32.setText("")
        self.pushButton_32.setObjectName("pushButton_32")
        self.gridLayout.addWidget(self.pushButton_32, 2, 8, 1, 1)
        self.pushButton_72 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_72.setEnabled(False)
        self.pushButton_72.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_72.setText("")
        self.pushButton_72.setObjectName("pushButton_72")
        self.gridLayout.addWidget(self.pushButton_72, 5, 12, 1, 1)
        self.pushButton_51 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_51.setEnabled(False)
        self.pushButton_51.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_51.setText("")
        self.pushButton_51.setObjectName("pushButton_51")
        self.gridLayout.addWidget(self.pushButton_51, 5, 5, 1, 1)
        self.pushButton_50 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_50.setEnabled(False)
        self.pushButton_50.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_50.setText("")
        self.pushButton_50.setObjectName("pushButton_50")
        self.gridLayout.addWidget(self.pushButton_50, 4, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                   "color: rgb(0, 255, 0);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_23.setEnabled(False)
        self.pushButton_23.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_23.setText("")
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout.addWidget(self.pushButton_23, 1, 11, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "color: rgb(0, 255, 0);")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 4, 1, 1)
        self.pushButton_54 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_54.setEnabled(False)
        self.pushButton_54.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_54.setText("")
        self.pushButton_54.setObjectName("pushButton_54")
        self.gridLayout.addWidget(self.pushButton_54, 5, 6, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "color: rgb(0, 255, 0);")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 6, 5, 1, 1)
        self.pushButton_39 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_39.setEnabled(False)
        self.pushButton_39.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_39.setText("")
        self.pushButton_39.setObjectName("pushButton_39")
        self.gridLayout.addWidget(self.pushButton_39, 5, 1, 1, 1)
        self.pushButton_55 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_55.setEnabled(False)
        self.pushButton_55.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_55.setText("")
        self.pushButton_55.setObjectName("pushButton_55")
        self.gridLayout.addWidget(self.pushButton_55, 3, 7, 1, 1)
        self.pushButton_63 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_63.setEnabled(False)
        self.pushButton_63.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_63.setText("")
        self.pushButton_63.setObjectName("pushButton_63")
        self.gridLayout.addWidget(self.pushButton_63, 5, 9, 1, 1)
        self.pushButton_41 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_41.setEnabled(False)
        self.pushButton_41.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_41.setText("")
        self.pushButton_41.setObjectName("pushButton_41")
        self.gridLayout.addWidget(self.pushButton_41, 4, 2, 1, 1)
        self.pushButton_67 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_67.setEnabled(False)
        self.pushButton_67.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_67.setText("")
        self.pushButton_67.setObjectName("pushButton_67")
        self.gridLayout.addWidget(self.pushButton_67, 3, 11, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                        "color: rgb(0, 255, 0);")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 0, 6, 1, 1)
        self.pushButton_64 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_64.setEnabled(False)
        self.pushButton_64.setStyleSheet("background-color: rgb(170, 85, 0);")
        self.pushButton_64.setText("")
        self.pushButton_64.setObjectName("pushButton_64")
        self.gridLayout.addWidget(self.pushButton_64, 3, 10, 1, 1)
        self.pushButton_30 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_30.setEnabled(False)
        self.pushButton_30.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_30.setText("")
        self.pushButton_30.setObjectName("pushButton_30")
        self.gridLayout.addWidget(self.pushButton_30, 2, 6, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_14.setEnabled(False)
        self.pushButton_14.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 1, 2, 1, 1)
        self.pushButton_31 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_31.setEnabled(False)
        self.pushButton_31.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_31.setText("")
        self.pushButton_31.setObjectName("pushButton_31")
        self.gridLayout.addWidget(self.pushButton_31, 2, 7, 1, 1)
        self.pushButton_71 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_71.setEnabled(False)
        self.pushButton_71.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_71.setText("")
        self.pushButton_71.setObjectName("pushButton_71")
        self.gridLayout.addWidget(self.pushButton_71, 4, 12, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                   "color: rgb(0, 255, 0);")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                        "color: rgb(0, 255, 0);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "color: rgb(0, 255, 0);")
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 6, 9, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                        "color: rgb(0, 255, 0);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 3, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_15.setEnabled(False)
        self.pushButton_15.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 1, 3, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_25.setEnabled(False)
        self.pushButton_25.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_25.setText("")
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout.addWidget(self.pushButton_25, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                   "color: rgb(0, 255, 0);")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 1, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_16.setEnabled(False)
        self.pushButton_16.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_16.setText("")
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 1, 4, 1, 1)
        self.pushButton_53 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_53.setEnabled(False)
        self.pushButton_53.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_53.setText("")
        self.pushButton_53.setObjectName("pushButton_53")
        self.gridLayout.addWidget(self.pushButton_53, 4, 6, 1, 1)
        self.pushButton_42 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_42.setEnabled(False)
        self.pushButton_42.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_42.setText("")
        self.pushButton_42.setObjectName("pushButton_42")
        self.gridLayout.addWidget(self.pushButton_42, 5, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "color: rgb(0, 255, 0);")
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 6, 11, 1, 1)
        self.pushButton_61 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_61.setEnabled(False)
        self.pushButton_61.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_61.setText("")
        self.pushButton_61.setObjectName("pushButton_61")
        self.gridLayout.addWidget(self.pushButton_61, 3, 9, 1, 1)
        self.pushButton_49 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_49.setEnabled(False)
        self.pushButton_49.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_49.setText("")
        self.pushButton_49.setObjectName("pushButton_49")
        self.gridLayout.addWidget(self.pushButton_49, 3, 5, 1, 1)
        self.pushButton_59 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_59.setEnabled(False)
        self.pushButton_59.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_59.setText("")
        self.pushButton_59.setObjectName("pushButton_59")
        self.gridLayout.addWidget(self.pushButton_59, 4, 8, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_18.setEnabled(False)
        self.pushButton_18.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_18.setText("")
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout.addWidget(self.pushButton_18, 1, 6, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_22.setEnabled(False)
        self.pushButton_22.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_22.setText("")
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout.addWidget(self.pushButton_22, 1, 10, 1, 1)
        self.pushButton_48 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_48.setEnabled(False)
        self.pushButton_48.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_48.setText("")
        self.pushButton_48.setObjectName("pushButton_48")
        self.gridLayout.addWidget(self.pushButton_48, 5, 4, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setEnabled(False)
        self.pushButton_11.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 0, 10, 1, 1)
        self.pushButton_28 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_28.setEnabled(False)
        self.pushButton_28.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_28.setText("")
        self.pushButton_28.setObjectName("pushButton_28")
        self.gridLayout.addWidget(self.pushButton_28, 2, 4, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "color: rgb(0, 255, 0);")
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 6, 8, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_24.setEnabled(False)
        self.pushButton_24.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_24.setText("")
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout.addWidget(self.pushButton_24, 1, 12, 1, 1)
        self.pushButton_35 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_35.setEnabled(False)
        self.pushButton_35.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_35.setText("")
        self.pushButton_35.setObjectName("pushButton_35")
        self.gridLayout.addWidget(self.pushButton_35, 2, 11, 1, 1)
        self.pushButton_29 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_29.setEnabled(False)
        self.pushButton_29.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_29.setText("")
        self.pushButton_29.setObjectName("pushButton_29")
        self.gridLayout.addWidget(self.pushButton_29, 2, 5, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_18.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "color: rgb(0, 255, 0);")
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 6, 12, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_13.setEnabled(False)
        self.pushButton_13.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 0, 12, 1, 1)
        self.pushButton_36 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_36.setEnabled(False)
        self.pushButton_36.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_36.setText("")
        self.pushButton_36.setObjectName("pushButton_36")
        self.gridLayout.addWidget(self.pushButton_36, 2, 12, 1, 1)
        self.pushButton_45 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_45.setEnabled(False)
        self.pushButton_45.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_45.setText("")
        self.pushButton_45.setObjectName("pushButton_45")
        self.gridLayout.addWidget(self.pushButton_45, 5, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                   "color: rgb(0, 255, 0);")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.pushButton_34 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_34.setEnabled(False)
        self.pushButton_34.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_34.setText("")
        self.pushButton_34.setObjectName("pushButton_34")
        self.gridLayout.addWidget(self.pushButton_34, 2, 10, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                      "color: rgb(0, 255, 0);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton_62 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_62.setEnabled(False)
        self.pushButton_62.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_62.setText("")
        self.pushButton_62.setObjectName("pushButton_62")
        self.gridLayout.addWidget(self.pushButton_62, 4, 9, 1, 1)
        self.pushButton_46 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_46.setEnabled(False)
        self.pushButton_46.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_46.setText("")
        self.pushButton_46.setObjectName("pushButton_46")
        self.gridLayout.addWidget(self.pushButton_46, 3, 4, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_20.setEnabled(False)
        self.pushButton_20.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_20.setText("")
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout.addWidget(self.pushButton_20, 1, 8, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setEnabled(False)
        self.pushButton_6.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                        "color: rgb(0, 255, 0);")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 0, 5, 1, 1)
        self.pushButton_66 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_66.setEnabled(False)
        self.pushButton_66.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_66.setText("")
        self.pushButton_66.setObjectName("pushButton_66")
        self.gridLayout.addWidget(self.pushButton_66, 5, 10, 1, 1)
        self.pushButton_57 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_57.setEnabled(False)
        self.pushButton_57.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_57.setText("")
        self.pushButton_57.setObjectName("pushButton_57")
        self.gridLayout.addWidget(self.pushButton_57, 5, 7, 1, 1)
        self.pushButton_70 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_70.setEnabled(False)
        self.pushButton_70.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_70.setText("")
        self.pushButton_70.setObjectName("pushButton_70")
        self.gridLayout.addWidget(self.pushButton_70, 3, 12, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "color: rgb(0, 255, 0);")
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 6, 7, 1, 1)
        self.pushButton_60 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_60.setEnabled(False)
        self.pushButton_60.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_60.setText("")
        self.pushButton_60.setObjectName("pushButton_60")
        self.gridLayout.addWidget(self.pushButton_60, 5, 8, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "color: rgb(0, 255, 0);")
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 6, 6, 1, 1)
        self.pushButton_47 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_47.setEnabled(False)
        self.pushButton_47.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_47.setText("")
        self.pushButton_47.setObjectName("pushButton_47")
        self.gridLayout.addWidget(self.pushButton_47, 4, 4, 1, 1)
        self.pushButton_37 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_37.setEnabled(False)
        self.pushButton_37.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_37.setText("")
        self.pushButton_37.setObjectName("pushButton_37")
        self.gridLayout.addWidget(self.pushButton_37, 3, 1, 1, 1)
        self.pushButton_58 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_58.setEnabled(False)
        self.pushButton_58.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_58.setText("")
        self.pushButton_58.setObjectName("pushButton_58")
        self.gridLayout.addWidget(self.pushButton_58, 3, 8, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                   "font: 10pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(0, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButton_40 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_40.setEnabled(False)
        self.pushButton_40.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_40.setText("")
        self.pushButton_40.setObjectName("pushButton_40")
        self.gridLayout.addWidget(self.pushButton_40, 3, 2, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setEnabled(False)
        self.pushButton_12.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 0, 11, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                   "color: rgb(0, 255, 0);")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 2, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_19.setEnabled(False)
        self.pushButton_19.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_19.setText("")
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout.addWidget(self.pushButton_19, 1, 7, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                   "color: rgb(0, 255, 0);")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                        "color: rgb(0, 255, 0);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 4, 1, 1)
        self.pushButton_68 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_68.setEnabled(False)
        self.pushButton_68.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_68.setText("")
        self.pushButton_68.setObjectName("pushButton_68")
        self.gridLayout.addWidget(self.pushButton_68, 4, 11, 1, 1)
        self.pushButton_69 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_69.setEnabled(False)
        self.pushButton_69.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_69.setText("")
        self.pushButton_69.setObjectName("pushButton_69")
        self.gridLayout.addWidget(self.pushButton_69, 5, 11, 1, 1)
        self.pushButton_44 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_44.setEnabled(False)
        self.pushButton_44.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_44.setText("")
        self.pushButton_44.setObjectName("pushButton_44")
        self.gridLayout.addWidget(self.pushButton_44, 4, 3, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setEnabled(False)
        self.pushButton_9.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                        "color: rgb(0, 255, 0);")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 0, 8, 1, 1)
        self.pushButton_65 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_65.setEnabled(False)
        self.pushButton_65.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_65.setText("")
        self.pushButton_65.setObjectName("pushButton_65")
        self.gridLayout.addWidget(self.pushButton_65, 4, 10, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                        "color: rgb(0, 255, 0);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_56 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_56.setEnabled(False)
        self.pushButton_56.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_56.setText("")
        self.pushButton_56.setObjectName("pushButton_56")
        self.gridLayout.addWidget(self.pushButton_56, 4, 7, 1, 1)
        self.pushButton_27 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_27.setEnabled(False)
        self.pushButton_27.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_27.setText("")
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout.addWidget(self.pushButton_27, 2, 3, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_17.setEnabled(False)
        self.pushButton_17.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_17.setText("")
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_17, 1, 5, 1, 1)
        self.pushButton_33 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_33.setEnabled(False)
        self.pushButton_33.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_33.setText("")
        self.pushButton_33.setObjectName("pushButton_33")
        self.gridLayout.addWidget(self.pushButton_33, 2, 9, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_21.setEnabled(False)
        self.pushButton_21.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(0, 255, 0);")
        self.pushButton_21.setText("")
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout.addWidget(self.pushButton_21, 1, 9, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(10, 210, 221, 81))
        self.label_19.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(230, 210, 50, 81))
        self.label_20.setStyleSheet("background-color: rgba(255, 255, 255б 0);font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(290, 210, 300, 81))
        self.label_21.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(590, 210, 50, 81))
        self.label_22.setStyleSheet("background-color: rgba(255, 255, 255б 0);font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.pushButton_74 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_74.setGeometry(QtCore.QRect(40, 370, 101, 21))
        self.pushButton_74.setStyleSheet("background-color: rgb(255, 215, 147);font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton_74.setObjectName("pushButton_74")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Гитара"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"right\"><span style="
                                      "\" font-size:12pt; font-weight:600;\">6</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"right\"><span style="
                                        "\" font-size:12pt; font-weight:600;\">2</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow",
                                         "<html><head/><body><p align=\"center\"><span style="
                                         "\" font-size:12pt; font-weight:600; font-style:italic;"
                                         "\">3</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"right\"><span style="
                                        "\" font-size:12pt; font-weight:600;\">4</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow",
                                         "<html><head/><body><p align=\"center\"><span style="
                                         "\" font-size:12pt; font-weight:600; font-style:italic;"
                                         "\">9</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow",
                                         "<html><head/><body><p align=\"center\"><span style="
                                         "\" font-size:12pt; font-weight:600; font-style:italic;"
                                         "\">8</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"right\"><span style="
                                        "\" font-size:12pt; font-weight:600;\">3</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow",
                                         "<html><head/><body><p align=\"center\"><span style="
                                         "\" font-size:12pt; font-weight:600; font-style:italic;"
                                         "\">4</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style="
                                        "\" font-size:12pt; font-weight:600; font-style:italic;"
                                        "\">12</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow",
                                         "<html><head/><body><p align=\"center\"><span style="
                                         "\" font-size:12pt; font-weight:600; font-style:italic;"
                                         "\">2</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow",
                                         "<html><head/><body><p align=\"center\"><span style="
                                         "\" font-size:12pt; font-weight:600; font-style:italic;"
                                         "\">5</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow",
                                         "<html><head/><body><p align=\"center\"><span style="
                                         "\" font-size:12pt; font-weight:600; font-style:italic;"
                                         "\">1</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"right\"><span style="
                                        "\" font-size:12pt; font-weight:600;\">1</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow",
                                         "<html><head/><body><p align=\"center\"><span style="
                                         "\" font-size:12pt; font-weight:600; font-style:italic;"
                                         "\">6</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow",
                                         "<html><head/><body><p align=\"center\"><span style="
                                         "\" font-size:12pt; font-weight:600; font-style:italic;"
                                         "\">7</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"right\"><span style="
                                        "\" font-size:12pt; font-weight:600;\">5</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style="
                                        "\" font-size:12pt; font-weight:600; font-style:italic;"
                                        "\">11</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style="
                                        "\" font-size:12pt; font-weight:600; font-style:italic;"
                                        "\">10</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow",
                                         "<html><head/><body><p align=\"center\"><span style="
                                         "\" font-size:12pt; font-weight:600;\">Выбранный аккорд:"
                                         "</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow",
                                         "<html><head/><body><p align=\"center\"><span style="
                                         "\" font-size:12pt; font-weight:600;\">Последняя извлеченная струна:"
                                         "</span></p></body></html>"))
        self.pushButton_74.setText(_translate("MainWindow", "Инструкция (F1)"))


class GuitarWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(GuitarWidget, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.M = 0
        self.n_cur_chord = ''

        result1 = cur.execute("""SELECT * FROM CHORDS""").fetchall()
        self.chords = {}
        for elem in result1:
            self.chords[elem[0]] = [el for el in elem[1:]]

        result2 = cur.execute("""SELECT S_1, S_2, S_3, S_4, S_5, S_6 FROM SOUNDS""").fetchall()
        self.sounds = [[] for i in range(6)]
        for i in range(len(result2)):
            self.sounds[0].append(result2[i][0])
            self.sounds[1].append(result2[i][1])
            self.sounds[2].append(result2[i][2])
            self.sounds[3].append(result2[i][3])
            self.sounds[4].append(result2[i][4])
            self.sounds[5].append(result2[i][5])

        self.neck = [
            [self.pushButton_72, self.pushButton_69, self.pushButton_66, self.pushButton_63, self.pushButton_60,
             self.pushButton_57, self.pushButton_54, self.pushButton_51, self.pushButton_48, self.pushButton_45,
             self.pushButton_42, self.pushButton_39],
            [self.pushButton_71, self.pushButton_68, self.pushButton_65, self.pushButton_62, self.pushButton_59,
             self.pushButton_56, self.pushButton_53, self.pushButton_50, self.pushButton_47, self.pushButton_44,
             self.pushButton_41, self.pushButton_38],
            [self.pushButton_70, self.pushButton_67, self.pushButton_64, self.pushButton_61, self.pushButton_58,
             self.pushButton_55, self.pushButton_52, self.pushButton_49, self.pushButton_46, self.pushButton_43,
             self.pushButton_40, self.pushButton_37],
            [self.pushButton_36, self.pushButton_35, self.pushButton_34, self.pushButton_33, self.pushButton_32,
             self.pushButton_31, self.pushButton_30, self.pushButton_29, self.pushButton_28, self.pushButton_27,
             self.pushButton_26, self.pushButton_25],
            [self.pushButton_24, self.pushButton_23, self.pushButton_22, self.pushButton_21, self.pushButton_20,
             self.pushButton_19, self.pushButton_18, self.pushButton_17, self.pushButton_16, self.pushButton_15,
             self.pushButton_14, self.pushButton_2],
            [self.pushButton_13, self.pushButton_12, self.pushButton_11, self.pushButton_10, self.pushButton_9,
             self.pushButton_8, self.pushButton_7, self.pushButton_6, self.pushButton_5, self.pushButton_4,
             self.pushButton_3, self.pushButton]
        ]

        for el1 in self.neck:
            for el2 in el1:
                el2.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                  "font: 75 22pt \"MS Shell Dlg 2\";\n"
                                  "color: rgb(0, 255, 0);")

        self.previous_chord = [0 for i in range(6)]

        self.current_string = 0
        self.previous_string = 0

        self.pushButton_74.setShortcut(Qt.Key_F1)

        self.pushButton_74.clicked.connect(self.instruction)

    def keyPressEvent(self, event):
        if self.previous_string != 0:
            if self.previous_string == 'all':
                for el1 in self.neck:
                    for el2 in el1:
                        el2.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                          "font: 75 22pt \"MS Shell Dlg 2\";\n"
                                          "color: rgb(0, 255, 0);")
            else:
                for elem in self.neck[self.previous_string - 1]:
                    elem.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                       "font: 75 22pt \"MS Shell Dlg 2\";\n"
                                       "color: rgb(0, 255, 0);")
            self.label_22.setText('')
        if event.key() == Qt.Key_C:
            self.n_cur_chord = 'C'
            self.M = 0
        if event.key() == Qt.Key_D:
            self.n_cur_chord = 'D'
            self.M = 0
        if event.key() == Qt.Key_E:
            self.n_cur_chord = 'E'
            self.M = 0
        if event.key() == Qt.Key_F:
            self.n_cur_chord = 'F'
            self.M = 0
        if event.key() == Qt.Key_G:
            self.n_cur_chord = 'G'
            self.M = 0
        if event.key() == Qt.Key_A:
            self.n_cur_chord = 'A'
            self.M = 0
        if event.key() == Qt.Key_H:
            self.n_cur_chord = 'H'
            self.M = 0
        if event.key() == Qt.Key_M:
            if self.M == 0:
                self.M = 1
                self.n_cur_chord = self.n_cur_chord + 'm'
            else:
                self.M = 0
                self.n_cur_chord = self.n_cur_chord[:-1]
        if self.n_cur_chord != '':
            if event.key() == Qt.Key_1:
                fret = self.chords[self.n_cur_chord][0]
                sound = self.sounds[0][fret]
                self.current_string = 1
                filename = 'audio/' + str(sound) + '.mp3'
                playsound(filename, block=False)

            if event.key() == Qt.Key_2:
                fret = self.chords[self.n_cur_chord][1]
                sound = self.sounds[1][fret]
                self.current_string = 2
                filename = 'audio/' + str(sound) + '.mp3'
                playsound(filename, block=False)

            if event.key() == Qt.Key_3:
                fret = self.chords[self.n_cur_chord][2]
                sound = self.sounds[2][fret]
                self.current_string = 3
                filename = 'audio/' + str(sound) + '.mp3'
                playsound(filename, block=False)

            if event.key() == Qt.Key_4:
                fret = self.chords[self.n_cur_chord][3]
                sound = self.sounds[3][fret]
                self.current_string = 4
                filename = 'audio/' + str(sound) + '.mp3'
                playsound(filename, block=False)

            if event.key() == Qt.Key_5:
                fret = self.chords[self.n_cur_chord][4]
                sound = self.sounds[4][fret]
                self.current_string = 5
                filename = 'audio/' + str(sound) + '.mp3'
                playsound(filename, block=False)

            if event.key() == Qt.Key_6:
                fret = self.chords[self.n_cur_chord][5]
                sound = self.sounds[5][fret]
                self.current_string = 6
                filename = 'audio/' + str(sound) + '.mp3'
                playsound(filename, block=False)

            if event.key() == Qt.Key_PageDown:
                self.current_string = 'all'
                filename = 'audio/' + self.n_cur_chord + '_bd.mp3'
                playsound(filename, block=False)

            if event.key() == Qt.Key_PageUp:
                self.current_string = 'all'
                filename = 'audio/' + self.n_cur_chord + '_bu.mp3'
                playsound(filename, block=False)

            self.label_20.setText(self.n_cur_chord)

            if self.current_string != 0:
                if self.current_string == 'all':
                    for el1 in self.neck:
                        for el2 in el1:
                            el2.setStyleSheet("background-color: rgb(0, 255, 0);\n"
                                              "font: 75 22pt \"MS Shell Dlg 2\";\n"
                                              "color: rgb(0, 0, 0);")
                else:
                    for elem in self.neck[self.current_string - 1]:
                        elem.setStyleSheet("background-color: rgb(0, 255, 0);\n"
                                           "font: 75 22pt \"MS Shell Dlg 2\";\n"
                                           "color: rgb(0, 0, 0);")
                self.label_22.setText(str(self.current_string))
            self.previous_string = self.current_string
            self.current_string = 0

            self.current_chord = self.chords[self.n_cur_chord]
            for i in range(len(self.previous_chord)):
                if self.previous_chord[i] != 0:
                    self.neck[i][self.previous_chord[i] - 1].setText('')
            for i in range(len(self.current_chord)):
                if self.current_chord[i] != 0:
                    self.neck[i][self.current_chord[i] - 1].setText('*')
            self.previous_chord = self.current_chord
        else:
            pass

    def closeEvent(self, event):
        con.close()

    def instruction(self):
        self.ex1 = InstructionWidget()
        self.ex1.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    con = sqlite3.connect("database/guitar_base.db")
    cur = con.cursor()
    ex = GuitarWidget()
    ex.show()
    sys.exit(app.exec_())
