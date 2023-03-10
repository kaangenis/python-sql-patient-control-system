from PyQt5 import QtCore, QtGui, QtWidgets
from mainPage import *
from kayitSayfa import *
from deletePage import Ui_DeleteWindow
from goruntuleSayfa import Ui_WindowGoruntule
from duzenlePage import *
import sqlite3 as sql



############################Database##############################


conn = sql.connect("HastaDatabase.db")
print("Database Bağlandı.")

cursor = conn.cursor()
print("Cursor Oluşturuldu. ")

conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS HASTAKAYIT(  
    TCKN integer,
    İsim  text,
    Soyisim  text,
    Yaş  integer,
    Şikayet text,
    Poliklinik text


) """)

conn.commit()

print("Table Olusturuldu.")


##################################################################


############################Fonksiyonlar##############################

def anasayfaHide():
    MainWindow.hide()

def anasayfaShow():
    MainWindow.show()


def kayitSayfa():
    ui.window = QtWidgets.QMainWindow()
    ui.ui = Ui_KayitWindow()
    ui.ui.setupUi(ui.window)
    ui.window.show()

    def kayitHide():
        ui.window.hide()

    def kayitDatabase():

        hasta_Tckn = int(ui.ui.tckn_Line.text())
        hasta_Isim = ui.ui.isim_Line.text()
        hasta_Soyisim = ui.ui.soyisim_Line.text()
        hasta_Yas = int(ui.ui.yas_Line.text())
        hasta_Rahatsizlik = ui.ui.rahatsizlik_Line.text()
        hasta_Polik = ui.ui.polik_Line.text()

        try:
            ekle = ("""INSERT INTO HASTAKAYIT (TCKN, İsim, Soyisim, Yaş, Şikayet, Poliklinik) 
             values (?,?,?,?,?,?) """)
            cursor.execute(ekle, (hasta_Tckn, hasta_Isim, hasta_Soyisim, hasta_Yas, hasta_Rahatsizlik, hasta_Polik))
            conn.commit()
            ui.ui.statusbar.showMessage("Kayıt Ekleme Başarılı.", 5000)

        except:
            ui.ui.statusbar.showMessage("Lütfen Tüm Boşlukları Doldurduğunuzdan Emin Olun.")


    def kayitSifirla():
        ui.ui.tckn_Line.clear()
        ui.ui.isim_Line.clear()
        ui.ui.soyisim_Line.clear()
        ui.ui.yas_Line.clear()
        ui.ui.rahatsizlik_Line.clear()
        ui.ui.polik_Line.clear()


    ui.ui.anamenu_BTN.clicked.connect(anasayfaShow)
    ui.ui.anamenu_BTN.clicked.connect(kayitHide)
    ui.ui.kayit_BTN.clicked.connect(kayitDatabase)
    ui.ui.sifirla_BTN.clicked.connect(kayitSifirla)


def goruntuleSayfa():
    ui.window = QtWidgets.QMainWindow()
    ui.ui = Ui_WindowGoruntule()
    ui.ui.setupUi(ui.window)
    ui.window.show()

    def goruntuleHide():
        ui.window.hide()

    def goruntuleDatabase():
        ui.ui.tableWidget.clear()
        ui.ui.tableWidget.setHorizontalHeaderLabels(("TCKN", "İsim", "Soyisim", "Yaş", "Rahatsızlık", "Poliklinik"))

        sorgu = """select * from HASTAKAYIT"""
        cursor.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(cursor):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                ui.ui.tableWidget.setItem(indexSatir, indexSutun, QtWidgets.QTableWidgetItem(str(kayitSutun)))

        print("Başarılı.")

    goruntuleDatabase()
    ui.ui.goruntuleAnaSayfa.clicked.connect(goruntuleHide)
    ui.ui.goruntuleAnaSayfa.clicked.connect(anasayfaShow)



def deleteShow():
    ui.window = QtWidgets.QMainWindow()
    ui.ui = Ui_DeleteWindow()
    ui.ui.setupUi(ui.window)
    ui.window.show()

    def silVeriDatabase():
        ui.ui.tableWidget.clear()
        ui.ui.tableWidget.setHorizontalHeaderLabels(("TCKN", "İsim", "Soyisim", "Yaş", "Rahatsızlık", "Poliklinik"))

        sorgu = "SELECT * FROM HASTAKAYIT"
        cursor.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(cursor):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                ui.ui.tableWidget.setItem(indexSatir, indexSutun, QtWidgets.QTableWidgetItem(str(kayitSutun)))

        print("Başarılı.")

    silVeriDatabase()

    def deleteHide():
        ui.window.hide()

    def kayitSil():
        sil = "DELETE FROM HASTAKAYIT WHERE TCKN = ?"
        input1 = ui.ui.lineEdit.text()
        cursor.execute(sil, (input1,))
        conn.commit()
        ui.ui.statusbar.showMessage(input1 + " " + "TCKN'li hastanın kaydı silinmiştir", 5000)
        print("Girdiğiniz Değer Silinmiştir.")

    def satirTemizle():
        ui.ui.lineEdit.clear()

    ui.ui.pushButton.clicked.connect(kayitSil)
    ui.ui.pushButton.clicked.connect(silVeriDatabase)
    ui.ui.pushButton.clicked.connect(satirTemizle)
    ui.ui.pushButton_2.clicked.connect(deleteHide)
    ui.ui.pushButton_2.clicked.connect(anasayfaShow)


def kayitDuzenle():
    ui.window = QtWidgets.QMainWindow()
    ui.ui = Ui_DuzenleWindow()
    ui.ui.setupUi(ui.window)
    ui.window.show()

    def duzenlePageKapat():
        ui.window.hide()

    def duzenleDatabase():
        ui.ui.tableDuzenle.clear()
        ui.ui.tableDuzenle.setHorizontalHeaderLabels(("TCKN", "İsim", "Soyisim", "Yaş", "Rahatsızlık", "Poliklinik"))

        sorgu = "SELECT * FROM HASTAKAYIT"
        cursor.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(cursor):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                ui.ui.tableDuzenle.setItem(indexSatir, indexSutun, QtWidgets.QTableWidgetItem(str(kayitSutun)))

        print("Başarılı.")

    duzenleDatabase()

    def kayitDuzenle():
        #duzenle = "UPDATE HASTAKAYIT SET TCKN = 25066068162 WHERE TCKN = 25066068160 "
        #duzenle = "UPDATE HASTAKAYIT SET İsim = 'Mehmet Kaan' WHERE İsim = 25066068161 "
        duzenle = "UPDATE HASTAKAYIT SET TCKN = ? WHERE TCKN = ? "
        #input2 = ui.ui.lineDuzenle.text()
        i1 = ui.ui.lineDuzenle_2.text()
        i2 = ui.ui.lineDuzenle.text()
        cursor.execute(duzenle, (i1,i2))
        conn.commit()
        ui.ui.lineDuzenle.clear()
        ui.ui.lineDuzenle_2.clear()
        print("Duzenlendi.")


    ui.ui.btnAnaSayfa.clicked.connect(anasayfaShow)
    ui.ui.btnAnaSayfa.clicked.connect(duzenlePageKapat)
    ui.ui.btnDuzenle.clicked.connect(kayitDuzenle)
    ui.ui.btnDuzenle.clicked.connect(duzenleDatabase)




def uygulamaKapat():
    sys.exit(app.exec_)


############################Run##############################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.btn_Cikis.clicked.connect(uygulamaKapat)
    ui.btn_Yeni.clicked.connect(kayitSayfa)
    ui.btn_Yeni.clicked.connect(anasayfaHide)
    ui.btn_Goruntule.clicked.connect(goruntuleSayfa)
    ui.btn_Goruntule.clicked.connect(anasayfaHide)
    ui.btn_Sil.clicked.connect(deleteShow)
    ui.btn_Sil.clicked.connect(anasayfaHide)
    ui.btn_Duzenle.clicked.connect(kayitDuzenle)
    ui.btn_Duzenle.clicked.connect(anasayfaHide)


    sys.exit(app.exec_())