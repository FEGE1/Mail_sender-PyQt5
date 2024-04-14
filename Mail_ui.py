# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mail_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import time
from Mail_Data import *
from PyQt5 import QtCore, QtGui, QtWidgets
data=Data()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 449)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 20, 261, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 80, 261, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 170, 601, 171))
        self.textEdit2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit2.setGeometry(QtCore.QRect(700,70,461,271))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit2.setFont(font)
        self.textEdit2.setObjectName("textEdit2")

        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 120, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 350, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 20, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 80, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 682, 21))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_2.clicked.connect(self.ekle)
        self.retranslateUi(MainWindow)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 130, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)

        self.güncellendi = QtWidgets.QLabel(self.centralwidget)
        self.güncellendi.setGeometry(1060,340,171,61)
        self.güncellendi.setFont(font)
        self.güncellendi.setText("")

        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setText("Yenile")
        self.pushButton_3.clicked.connect(self.sil)
        self.pushButton_4.clicked.connect(self.yenile)
        self.pushButton_4.clicked.connect(self.temizle)
        self.pushButton.clicked.connect(self.gonder)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.gönderilecek = QtWidgets.QLabel(self.centralwidget)
        self.gönderilecek.setGeometry(820,20,231,41)
        self.gönderilecek.setFont(font)
        self.gönderilecek.setText("Gönderilecek Mesaj")
        self.pushButton5=QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(830,350,211,41))
        self.pushButton5.setFont(font)
        self.pushButton5.setObjectName("pushButton5")
        self.pushButton5.setText("Yazıyı Güncelle")
        self.pushButton5.clicked.connect(self.update)
        self.pushButton5.clicked.connect(self.tepki)

        self.textEdit2.setText(data.yazi_göster())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def temizle(self):
        self.güncellendi.setText("")
    def tepki(self):
        self.güncellendi.setText("Güncellendi")

    def update(self):
        yeni_yazi=self.textEdit2.toPlainText()


        data.yazi_değiştir(yeni_yazi)
        gösterilen=data.yazi_göster()

        self.textEdit2.setText(gösterilen)


    def gonder(self):
        data.mailleri_gönder()

    def ekle(self):
        mail=self.lineEdit.text()
        if mail.endswith(".com"):

            data.mail_ekle(mail)
            #time.sleep(2)
            self.lineEdit.clear()
        else:
            print("Geçersiz Mail Yapısı.")
            self.lineEdit.setText("Geçersiz Mail Yapısı.")
    def sil(self):
        mail=self.lineEdit_2.text()
        if mail.endswith(".com"):
            data.mail_sil(mail)
            #time.sleep(2)
            self.lineEdit_2.clear()
        else:
            print("Geçersiz Mail Yapısı.")
            self.lineEdit_2.setText("Geçersiz Mail Yapısı.")
    def yenile(self):
        self.textEdit.clear()
        for i in data.mailler():
            self.textEdit.append(i)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mail Gönderme Programi"))
        self.label.setText(_translate("MainWindow", "Mail Ekle:"))
        self.label_2.setText(_translate("MainWindow", "Mail Sil:"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Mevcut Mailler"))
        self.pushButton.setText(_translate("MainWindow", "Gönder"))
        self.pushButton_2.setText(_translate("MainWindow", "Ekle"))
        self.pushButton_3.setText(_translate("MainWindow", "Sil"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

