# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kayitSayfa.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KayitWindow(object):
    def setupUi(self, KayitWindow):
        KayitWindow.setObjectName("KayitWindow")
        KayitWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(KayitWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.kayit_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.kayit_BTN.setGeometry(QtCore.QRect(450, 290, 151, 41))
        self.kayit_BTN.setStyleSheet("font: 20pt \".AppleSystemUIFont\";")
        self.kayit_BTN.setObjectName("kayit_BTN")
        self.sifirla_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.sifirla_BTN.setGeometry(QtCore.QRect(450, 330, 151, 41))
        self.sifirla_BTN.setStyleSheet("font: 20pt \".AppleSystemUIFont\";")
        self.sifirla_BTN.setObjectName("sifirla_BTN")
        self.anamenu_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.anamenu_BTN.setGeometry(QtCore.QRect(450, 370, 151, 41))
        self.anamenu_BTN.setStyleSheet("font: 16pt \".AppleSystemUIFont\";")
        self.anamenu_BTN.setObjectName("anamenu_BTN")
        self.tckn_Line = QtWidgets.QLineEdit(self.centralwidget)
        self.tckn_Line.setGeometry(QtCore.QRect(170, 60, 181, 31))
        self.tckn_Line.setObjectName("tckn_Line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 31))
        self.label.setStyleSheet("font: 28pt \".AppleSystemUIFont\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 101, 31))
        self.label_2.setStyleSheet("font: 22pt \".AppleSystemUIFont\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 101, 31))
        self.label_3.setStyleSheet("font: 22pt \".AppleSystemUIFont\";")
        self.label_3.setObjectName("label_3")
        self.isim_Line = QtWidgets.QLineEdit(self.centralwidget)
        self.isim_Line.setGeometry(QtCore.QRect(170, 100, 181, 31))
        self.isim_Line.setObjectName("isim_Line")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 101, 31))
        self.label_4.setStyleSheet("font: 22pt \".AppleSystemUIFont\";")
        self.label_4.setObjectName("label_4")
        self.soyisim_Line = QtWidgets.QLineEdit(self.centralwidget)
        self.soyisim_Line.setGeometry(QtCore.QRect(170, 140, 181, 31))
        self.soyisim_Line.setObjectName("soyisim_Line")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 180, 101, 31))
        self.label_5.setStyleSheet("font: 22pt \".AppleSystemUIFont\";")
        self.label_5.setObjectName("label_5")
        self.yas_Line = QtWidgets.QLineEdit(self.centralwidget)
        self.yas_Line.setGeometry(QtCore.QRect(170, 180, 181, 31))
        self.yas_Line.setObjectName("yas_Line")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 220, 151, 31))
        self.label_6.setStyleSheet("font: 22pt \".AppleSystemUIFont\";")
        self.label_6.setObjectName("label_6")
        self.rahatsizlik_Line = QtWidgets.QLineEdit(self.centralwidget)
        self.rahatsizlik_Line.setGeometry(QtCore.QRect(170, 220, 181, 31))
        self.rahatsizlik_Line.setObjectName("rahatsizlik_Line")
        self.polik_Line = QtWidgets.QLineEdit(self.centralwidget)
        self.polik_Line.setGeometry(QtCore.QRect(170, 260, 181, 31))
        self.polik_Line.setObjectName("polik_Line")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 260, 151, 31))
        self.label_7.setStyleSheet("font: 22pt \".AppleSystemUIFont\";")
        self.label_7.setObjectName("label_7")
        KayitWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(KayitWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 24))
        self.menubar.setObjectName("menubar")
        KayitWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(KayitWindow)
        self.statusbar.setObjectName("statusbar")
        KayitWindow.setStatusBar(self.statusbar)

        self.retranslateUi(KayitWindow)
        QtCore.QMetaObject.connectSlotsByName(KayitWindow)

    def retranslateUi(self, KayitWindow):
        _translate = QtCore.QCoreApplication.translate
        KayitWindow.setWindowTitle(_translate("KayitWindow", "MainWindow"))
        self.kayit_BTN.setText(_translate("KayitWindow", "Kayıt Ekle"))
        self.sifirla_BTN.setText(_translate("KayitWindow", "Sıfırla"))
        self.anamenu_BTN.setText(_translate("KayitWindow", "Ana Menüye Dön"))
        self.label.setText(_translate("KayitWindow", "Hasta Ekle"))
        self.label_2.setText(_translate("KayitWindow", "TCKN :"))
        self.label_3.setText(_translate("KayitWindow", "İSİM :"))
        self.label_4.setText(_translate("KayitWindow", "SOYİSİM :"))
        self.label_5.setText(_translate("KayitWindow", "YAŞ :"))
        self.label_6.setText(_translate("KayitWindow", "RAHATSIZLIK :"))
        self.label_7.setText(_translate("KayitWindow", "POLİKLİNİK : "))