# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\tux.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# Author : Mehmet Eroğlu

from PyQt5 import QtCore, QtGui, QtWidgets
from vtbgln import VbagKur
import mesajlar as mes
import os
import webbrowser
import tslmt


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(417, 341)
        Dialog.setMinimumSize(QtCore.QSize(417, 341))
        Dialog.setMaximumSize(QtCore.QSize(417, 341))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(115, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setMinimumSize(QtCore.QSize(151, 80))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(6, 2, 151, 80))
        self.label.setMinimumSize(QtCore.QSize(151, 80))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("lib/gplv3-with-text-136x68.png"))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(115, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setStyleSheet("background-color: rgb(89, 89, 89);\n"
"color: rgb(255, 255, 255);")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tux Lisans"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "Tux özgür bir yazılımdır, Özgür Yazılım Vakfı\'nın yayınladığı GNU Genel Kamu Lisansı\'nın 3. veya daha sonraki sürümlerindeki şartlar altında dağıtılabilir ve/veya değiştirilebilir. \n"
"\n"
"Tux faydalı olacağı umut edilerek dağıtılmaktadır, fakat HİÇBİR GARANTİSİ YOKTUR; hatta ÜRÜN DEĞERİ ya da BİR AMACA UYGUNLUK gibi garantiler de vermez. Lütfen daha çok ayrıntı için GNU Genel Kamu Lisansı\'nı inceleyin. \n"
"\n"
"Tux ile beraber GNU Genel Kamu Lisansını da almış olmalısınız; eğer almadıysanız, https://www.gnu.org/licenses/ adresine bakın."))


class Ui_Firmaolustur(VbagKur):
    def __init__(self):
        self.yaz = VbagKur()

    def setupUi(self, Firmaolustur):
        Firmaolustur.setObjectName("Firmaolustur")
        Firmaolustur.resize(400, 318)
        self.label = QtWidgets.QLabel(Firmaolustur)
        self.label.setGeometry(QtCore.QRect(16, 10, 68, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Firmaolustur)
        self.lineEdit.setGeometry(QtCore.QRect(90, 10, 281, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Firmaolustur)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 40, 281, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Firmaolustur)
        self.label_2.setGeometry(QtCore.QRect(16, 40, 68, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Firmaolustur)
        self.label_3.setGeometry(QtCore.QRect(16, 70, 68, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Firmaolustur)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 70, 281, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Firmaolustur)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 100, 281, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(Firmaolustur)
        self.label_4.setGeometry(QtCore.QRect(16, 100, 68, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Firmaolustur)
        self.label_5.setGeometry(QtCore.QRect(16, 160, 68, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Firmaolustur)
        self.label_6.setGeometry(QtCore.QRect(16, 130, 68, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(Firmaolustur)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 130, 281, 20))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.textEdit = QtWidgets.QTextEdit(Firmaolustur)
        self.textEdit.setGeometry(QtCore.QRect(90, 160, 281, 111))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Firmaolustur)
        self.pushButton.setGeometry(QtCore.QRect(300, 280, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Firmaolustur)
        self.pushButton.clicked.connect(self.firmabilgisiyaz)
        QtCore.QMetaObject.connectSlotsByName(Firmaolustur)

    def firmabilgisiyaz(self):
        kod = self.lineEdit.text()
        ad = self.lineEdit_2.text()
        vergidairesi = self.lineEdit_3.text()
        vergino = self.lineEdit_4.text()
        telefon = self.lineEdit_5.text()
        adres = self.textEdit.toPlainText()
        self.yaz.firma_ekle(kod, ad, vergidairesi, vergino, telefon, adres)
        mesaj = ad + " Firmasının veritabanı kaydı başarıyla yapıldı"

        mes.uyari(mesaj, "Bilgilendirme")

        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.textEdit.clear()




    def retranslateUi(self, Firmaolustur):
        _translate = QtCore.QCoreApplication.translate
        Firmaolustur.setWindowTitle(_translate("Firmaolustur", "Müşteri Oluştur"))
        self.label.setText(_translate("Firmaolustur", "Müşteri Kodu"))
        self.label_2.setText(_translate("Firmaolustur", "Müşteri Adı"))
        self.label_3.setText(_translate("Firmaolustur", "Vergi Dairesi"))
        self.label_4.setText(_translate("Firmaolustur", "Vergi No"))
        self.label_5.setText(_translate("Firmaolustur", "Adres"))
        self.label_6.setText(_translate("Firmaolustur", "Telefon"))
        self.pushButton.setText(_translate("Firmaolustur", "OLUŞTUR"))


class Ui_Firmaguncelle(VbagKur):
    def __init__(self):
        self.yaz = VbagKur
        self.change_no = 0
        self.eski_kod = 0
        self.yeni_kod = 0

    def setupUi(self, Firmaguncelle):
        self.yaz = VbagKur()
        Firmaguncelle.setObjectName("Firmaguncelle")
        Firmaguncelle.resize(683, 457)
        self.gridLayout_2 = QtWidgets.QGridLayout(Firmaguncelle)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(Firmaguncelle)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(Firmaguncelle)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 0, 1, 1, 2)
        self.listWidget = QtWidgets.QListWidget(Firmaguncelle)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 1, 0, 1, 2)
        self.frame = QtWidgets.QFrame(Firmaguncelle)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 5, 1, 2, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 212, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(264, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 7, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 7, 2, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 2, 1, 1)

        self.retranslateUi(Firmaguncelle)
        self.lineEdit_6.textChanged['QString'].connect(self.bul)
        self.listWidget.doubleClicked['QModelIndex'].connect(self.doldur)
        self.pushButton.clicked.connect(self.guncelle)
        QtCore.QMetaObject.connectSlotsByName(Firmaguncelle)

    def retranslateUi(self, Firmaguncelle):
        _translate = QtCore.QCoreApplication.translate
        Firmaguncelle.setWindowTitle(_translate("Firmaguncelle", "Müşteri Bilgisi Güncelle"))
        self.label_7.setText(_translate("Firmaguncelle", "Firma Ara"))
        self.label.setText(_translate("Firmaguncelle", "Müşteri Kodu"))
        self.label_2.setText(_translate("Firmaguncelle", "Müşteri Adı"))
        self.label_3.setText(_translate("Firmaguncelle", "Vergi Dairesi"))
        self.label_4.setText(_translate("Firmaguncelle", "Vergi No"))
        self.label_6.setText(_translate("Firmaguncelle", "Telefon"))
        self.label_5.setText(_translate("Firmaguncelle", "Adres"))
        self.pushButton.setText(_translate("Firmaguncelle", "GÜNCELLE"))

    def guncelle(self):
        kod = self.lineEdit.text()
        self.yeni_kod = kod
        ad = self.lineEdit_2.text()
        vergidairesi = self.lineEdit_3.text()
        vergino = self.lineEdit_4.text()
        telefon = self.lineEdit_5.text()
        adres = self.textEdit.toPlainText()
        if kod == " ":
            mesaj = ad + "Lütfen Müşteri Ad bilgisini doldurun"
            mes.uyari(mesaj, "Uyarı")
        elif ad ==" ":
            mesaj = ad + "Lütfen Müşteri Ad bilgisini doldurun"
            mes.uyari(mesaj, "Uyarı")
        elif vergidairesi == " ":
            mesaj = ad + "Lütfen Müşteri Vergi Dairesi bilgisini doldurun"
            mes.uyari(mesaj, "Uyarı")
        elif vergino == " ":
            mesaj = ad + "Lütfen Müşteri Vergi No bilgisini doldurun"
            mes.uyari(mesaj, "Uyarı")
        elif adres == " ":
            mesaj = ad + "Lütfen Müşteri Adres bilgisini doldurun"
            mes.uyari(mesaj, "Uyarı")
        else:
            self.yaz.firma_guncelle(kod, ad, vergidairesi, vergino, telefon, adres, self.change_no)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.textEdit.clear()
            mesaj = ad + "Müşteri Bilgileri Güncellenmiştir"
            mes.uyari(mesaj, "Bilgilendirme")
            if self.eski_kod != self.yeni_kod:
                liste = self.yaz.hepsini_oku("id", "gemiler", "kod", self.eski_kod)
                if len(liste) == 0:
                    pass
                else:
                    mesaj = """Veritabanında bu Müşteri için çalışan {} adet gemi bulundu.
                    Bu değişiklik müşteriye bağlı gemilerin listelenmesini engeller.\n
                    Müşteriye bağlı gemilerin firma kodunuda değiştirmek istiyor musunuz ?
                    Eğer değiştirmek istemezseniz gemilerin firma bağlantı kodu etkisiz hale getirilecek ve
                    yeniden düzenlenene kadar teslimat dosyasında listelenmeyecekler.\n
                    (Gemi düzenleme sayfasından yeni bir müşteri kodu ile aktif hale getirebilirsiniz.)
                        """.format(len(liste))
                    sor = mes.soru("Müşteri Kodunu Değiştirdiniz !!", mesaj,
                                   "Gemilerin kodları, müşterinin yeni koduna göre düzenleniyor",
                                   "Gemilerin kod değişimi iptal edildi")
                    if sor == True:
                        for i in range(len(liste)):
                            self.yaz.gemi_kod_guncelle(self.yeni_kod, liste[i][0])
                    else:
                        for i in range(len(liste)):
                            self.yaz.gemi_kod_guncelle("000000", liste[i][0])
            else:
                pass
            self.bul()

    def bul(self):
        self.listWidget.clear()
        sonuc = self.yaz.coklu_komut("SELECT ad FROM firmalar WHERE ad LIKE '{}'".format(self.lineEdit_6.text()+"%"))
        if len(sonuc) == 0:
            self.listWidget.addItem("Sonuç Bulunamadı")
        else:
            for i in range(len(sonuc)):
                self.listWidget.addItem(sonuc[i][0])

    def doldur(self):
        veri = self.yaz.komut("SELECT * FROM firmalar WHERE ad='{}'".format(self.listWidget.currentItem().text()))
        self.eski_kod =veri[1]
        self.lineEdit.setText(str(veri[1]))
        self.lineEdit_2.setText(veri[2])
        self.lineEdit_3.setText(veri[3])
        self.lineEdit_4.setText(str(veri[4]))
        self.lineEdit_5.setText(str(veri[5]))
        self.textEdit.setPlainText(veri[6])
        self.change_no = veri[0]


class Ui_Firmasil(VbagKur):
    def __init__(self):
        self.yaz = VbagKur()
        self.firma_id = 0
        self.firma_kod = 0
        self.firma_ad = ""

    def setupUi(self, Firmasil):
        Firmasil.setObjectName("Firmasil")
        Firmasil.resize(639, 419)
        self.gridLayout_2 = QtWidgets.QGridLayout(Firmasil)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(Firmasil)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(Firmasil)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 0, 1, 1, 2)
        self.listWidget = QtWidgets.QListWidget(Firmasil)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 1, 0, 1, 2)
        self.frame = QtWidgets.QFrame(Firmasil)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 5, 1, 2, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 174, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 7, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 7, 2, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 2, 1, 1)

        self.retranslateUi(Firmasil)
        self.lineEdit_6.textChanged['QString'].connect(self.bul)
        self.listWidget.doubleClicked['QModelIndex'].connect(self.doldur)
        self.pushButton.clicked.connect(self.sil)
        QtCore.QMetaObject.connectSlotsByName(Firmasil)

    def retranslateUi(self, Firmasil):
        _translate = QtCore.QCoreApplication.translate
        Firmasil.setWindowTitle(_translate("Firmasil", "Müşteri Sil"))
        self.label_7.setText(_translate("Firmasil", "Firma Bul"))
        self.label.setText(_translate("Firmasil", "Müşteri Kodu"))
        self.label_2.setText(_translate("Firmasil", "Müşteri Adı"))
        self.label_3.setText(_translate("Firmasil", "Vergi Dairesi"))
        self.label_4.setText(_translate("Firmasil", "Vergi No"))
        self.label_5.setText(_translate("Firmasil", "Telefon"))
        self.label_6.setText(_translate("Firmasil", "Adres"))
        self.pushButton.setText(_translate("Firmasil", "Sil"))

    def bul(self):
        self.listWidget.clear()
        sonuc = self.yaz.coklu_komut("SELECT ad FROM firmalar WHERE ad LIKE '{}'".format(self.lineEdit_6.text()+"%"))
        if len(sonuc) == 0:
            self.listWidget.addItem("Sonuç Bulunamadı")
        else:
            for i in range(len(sonuc)):
                self.listWidget.addItem(sonuc[i][0])

    def doldur(self):
        veri = self.yaz.komut("SELECT * FROM firmalar WHERE ad='{}'".format(self.listWidget.currentItem().text()))
        self.eski_kod =veri[1]
        self.lineEdit.setText(str(veri[1]))
        self.lineEdit_2.setText(veri[2])
        self.lineEdit_3.setText(veri[3])
        self.lineEdit_4.setText(str(veri[4]))
        self.lineEdit_5.setText(str(veri[5]))
        self.textEdit.setPlainText(veri[6])
        self.firma_id = veri[0]
        self.firma_kod = veri[1]
        self.firma_ad = veri[2]

    def sil(self):
        mesaj = """{} firmasının bilgilerini silmek istediğinizden emin misiniz ? """.format(self.lineEdit_2.text())
        sor = mes.soru("Firma Bilgilerini Silmek Üzeresiniz !!", mesaj,
                       "Firma Bilgileri Siliniyor",
                       "İşlem  iptal edildi")
        if sor == True:
            id = self.firma_id
            self.yaz.kayit_sil("firmalar", "id", id)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.textEdit.clear()
            liste = self.yaz.hepsini_oku("id", "gemiler", "kod", self.firma_kod)
            mesaj = """Veritabanında {} firmasına ait {} adet gemi kaydı bulundu.
             Firma ile birlikte firmaya ait gemi kayıtlarınıda silmek ister misiniz?\n
              (Eğer gemi kayıtlarını silmezseniz, gemiler otomatik olarak pasif furuma getirilecektir.
              Gemi bilgisi düzenleme kısmından yeni bir müşteri ile ilişkilendirebilirsiniz)""".format(self.lineEdit_2.text(),
                                                                                                len(liste))
            sor = mes.soru("Firma Bağlantılı Gemiler !!", mesaj,
                           "Firma bağlantılı gemi kayıtları siliniyor",
                           "İşlem  iptal edildi")
            if sor == True:
                for i in range(len(liste)):
                    self.yaz.kayit_sil("gemiler", "id", liste[i][0])
            else:
                for i in range(len(liste)):
                    self.yaz.gemi_kod_guncelle("000000", liste[i][0])
        else:
            pass
        self.bul()


class Ui_GemiEkle(VbagKur):
    def __init__(self):
        self.yaz = VbagKur()
        self.firma_ad = ""
        self.firma_kod = 0

    def setupUi(self, GemiEkle):
        GemiEkle.setObjectName("GemiEkle")
        GemiEkle.resize(617, 369)
        self.gridLayout_2 = QtWidgets.QGridLayout(GemiEkle)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(GemiEkle)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(GemiEkle)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 1, 0, 1, 2)
        self.frame = QtWidgets.QFrame(GemiEkle)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 5, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 6, 1, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 7, 1, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 8, 1, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 9, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 10, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 10, 2, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 2, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(GemiEkle)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_2.addWidget(self.lineEdit_11, 0, 1, 1, 1)

        self.retranslateUi(GemiEkle)
        QtCore.QMetaObject.connectSlotsByName(GemiEkle)
        self.lineEdit_11.textChanged['QString'].connect(self.bul)
        self.listWidget.doubleClicked['QModelIndex'].connect(self.doldur)
        self.pushButton.clicked.connect(self.ekle)

    def retranslateUi(self, GemiEkle):
        _translate = QtCore.QCoreApplication.translate
        GemiEkle.setWindowTitle(_translate("GemiEkle", "Gemi Ekle"))
        self.label_11.setText(_translate("GemiEkle", "Firma Bul"))
        self.label.setText(_translate("GemiEkle", "Müşteri Kodu"))
        self.label_2.setText(_translate("GemiEkle", "Gemi Adı"))
        self.label_3.setText(_translate("GemiEkle", "Gemi Kodu"))
        self.label_4.setText(_translate("GemiEkle", "Gemi Cinsi"))
        self.label_5.setText(_translate("GemiEkle", "Defter No"))
        self.label_6.setText(_translate("GemiEkle", "Belge No"))
        self.label_7.setText(_translate("GemiEkle", "Sicil No"))
        self.label_8.setText(_translate("GemiEkle", "İmo / Çağrı İşareti"))
        self.label_9.setText(_translate("GemiEkle", "Acenta"))
        self.label_10.setText(_translate("GemiEkle", "Acenta Tel"))
        self.pushButton.setText(_translate("GemiEkle", "Gemi Ekle"))

    def bul(self):
        self.listWidget.clear()
        sonuc = self.yaz.coklu_komut("SELECT ad, kod FROM firmalar WHERE ad LIKE '{}'".format(self.lineEdit_11.text()+"%"))
        if len(sonuc) == 0:
            self.listWidget.addItem("Sonuç Bulunamadı")
        else:
            for i in range(len(sonuc)):
                self.listWidget.addItem(sonuc[i][0])
                self.firma_ad = sonuc[i][0]
                self.firma_kod = sonuc[i][1]

    def doldur(self):
        self.lineEdit.setText(self.firma_kod)

    def ekle(self):
        if self.lineEdit.text() == "":
            mesaj = "Lütfen Müşteri kod bilgisini doldurun"
            mes.uyari(mesaj, "Uyarı")
        elif self.lineEdit_2.text() == "":
            mesaj = "Lütfen gemi ad bilgisini doldurun"
            mes.uyari(mesaj, "Uyarı")
        elif self.lineEdit_3.text() == "":
            mesaj = "Lütfen gemi kod bilgisini doldurun"
            mes.uyari(mesaj, "Uyarı")
        elif self.lineEdit_4.text() == "":
            mesaj = "Lütfen gemi cins bilgisini doldurun"
            mes.uyari(mesaj, "Uyarı")
        elif self.lineEdit_5.text() == "":
            mesaj = "Lütfen gemi defter no bilgisini doldurun"
            mes.uyari(mesaj, "Uyarı")
        elif self.lineEdit_6.text() == "":
            mesaj = "Lütfen gemi defter belge no bilgisini doldurun"
            mes.uyari(mesaj, "Uyarı")
        elif self.lineEdit_7.text() == "":
            mesaj = "Lütfen gemi sicil no bilgisini doldurun"
            mes.uyari(mesaj, "Uyarı")
        elif self.lineEdit_8.text() == "":
            mesaj = "Lütfen gemi İmo/Çağrı işareti bilgisini doldurun"
            mes.uyari(mesaj, "Uyarı")
        else:
            liste = []
            liste.append(self.lineEdit.text())
            liste.append(self.lineEdit_2.text())
            liste.append(self.lineEdit_3.text())
            liste.append(self.lineEdit_4.text())
            liste.append(self.lineEdit_5.text())
            liste.append(self.lineEdit_6.text())
            liste.append(self.lineEdit_7.text())
            liste.append(self.lineEdit_8.text())
            liste.append(self.lineEdit_9.text())
            liste.append(self.lineEdit_10.text())

            self.yaz.gemi_ekle(liste)
            mesaj = self.lineEdit_2.text() + " gemisinin veritabanı kaydı başarıyla yapıldı"
            mes.uyari(mesaj, "Bilgilendirme")
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
            self.lineEdit_8.clear()
            self.lineEdit_9.clear()
            self.lineEdit_10.clear()


class Ui_Fg(VbagKur):
    def __init__(self):
        self.yaz = VbagKur()
        self.gemi_id = 0
        self.firma_ad = ""
        self.firma_kod = 0

    def setupUi(self, Fg):
        Fg.setObjectName("Fg")
        Fg.resize(455, 399)
        self.gridLayout_2 = QtWidgets.QGridLayout(Fg)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(Fg)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Fg)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.listWidget = QtWidgets.QListWidget(Fg)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 1, 0, 1, 2)
        self.frame = QtWidgets.QFrame(Fg)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 5, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 6, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 7, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 7, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 8, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 8, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 9, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 9, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(53, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 10, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 10, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 2, 1, 1)

        self.retranslateUi(Fg)
        self.lineEdit.textChanged['QString'].connect(self.bul)
        self.listWidget.doubleClicked['QModelIndex'].connect(self.doldur)
        self.pushButton_2.clicked.connect(self.guncelle)
        QtCore.QMetaObject.connectSlotsByName(Fg)

    def retranslateUi(self, Fg):
        _translate = QtCore.QCoreApplication.translate
        Fg.setWindowTitle(_translate("Fg", "Gemi Bilgisi Düzenle"))
        self.label.setText(_translate("Fg", "Gemi Adı"))
        self.label_3.setText(_translate("Fg", "Müşteri Kod"))
        self.label_4.setText(_translate("Fg", "Gemi Adı"))
        self.label_5.setText(_translate("Fg", "Gemi No"))
        self.label_6.setText(_translate("Fg", "Gemi Cinsi"))
        self.label_7.setText(_translate("Fg", "Defter No"))
        self.label_8.setText(_translate("Fg", "Belge No"))
        self.label_9.setText(_translate("Fg", "Sicil No"))
        self.label_10.setText(_translate("Fg", "İmo / Çağrı"))
        self.label_12.setText(_translate("Fg", "Acenta "))
        self.label_13.setText(_translate("Fg", "Acenta Tel"))
        self.pushButton_2.setText(_translate("Fg", "Güncelle"))

    def bul(self):
        self.listWidget.clear()
        sonuc = self.yaz.coklu_komut("SELECT gad FROM gemiler WHERE gad LIKE '{}'".format(self.lineEdit.text() + "%"))
        if len(sonuc) == 0:
            self.listWidget.addItem("Sonuç Bulunamadı")
        else:
            for i in range(len(sonuc)):
                self.listWidget.addItem(sonuc[i][0])

    def doldur(self):
        soru = self.yaz.tek_oku("gemiler", "gad", self.listWidget.currentItem().text())
        self.lineEdit_2.setText(str(soru[0][1]))
        self.lineEdit_3.setText(soru[0][2])
        self.lineEdit_4.setText(soru[0][3])
        self.lineEdit_5.setText(soru[0][4])
        self.lineEdit_6.setText(soru[0][5])
        self.lineEdit_7.setText(soru[0][6])
        self.lineEdit_8.setText(soru[0][7])
        self.lineEdit_9.setText(soru[0][8])
        self.lineEdit_10.setText(soru[0][9])
        self.lineEdit_11.setText(soru[0][10])
        self.gemi_id = soru[0][0]

        self.firma_kod =soru[0][1]
        fad = self.yaz.komut("select ad from firmalar where kod='{}'".format(self.firma_kod))
        self.firma_ad = fad[0]


    def guncelle(self):
        if self.firma_kod != int(self.lineEdit_2.text()):
            mesaj = """Geminin müşteri kodunu değiştirdiniz.
            Devam ederseniz geminin {} ile olan bağlantısı kesilip yeni müşteri koduna göre ilişkilendirilecektir""".format(self.firma_ad)
            sor = mes.soru("Müşteri Kodunu Değiştirdiniz !!", mesaj,
                           "Gemi yeni müşterinin  koduna ilişkilendiriliyor",
                           "Müşteri kod değişimi iptal edildi")
            if sor == True:
                kontrol = self.yaz.komut("select kod from firmalar where kod='{}'".format(self.lineEdit_2.text()))
                if kontrol == None:
                    mesaj = "Yazdığınız koda sahip bir müşteri bulunamadı.Gemiyi bir müşteriyle ilişkilendirebilmek için" \
                            "öncelikle müşteri eklemesi yapmanız gerekir.Müşteri kodunu kontrol de edebilirsiniz "
                    mes.uyari(mesaj, "Bilgilendirme")
                    return
                else:
                    self.yaz.gemi_guncelle(self.lineEdit_2.text(),
                                           self.lineEdit_3.text(),
                                           self.lineEdit_4.text(),
                                           self.lineEdit_5.text(),
                                           self.lineEdit_6.text(),
                                           self.lineEdit_7.text(),
                                           self.lineEdit_8.text(),
                                           self.lineEdit_9.text(),
                                           self.lineEdit_10.text(),
                                           self.lineEdit_11.text(),
                                           self.gemi_id
                                           )
                    mesaj = self.lineEdit_3.text() + " Gemisinin Kaydı Başarıyla Değiştirildi"
                    mes.uyari(mesaj, "Bilgilendirme")
                    self.lineEdit_2.clear()
                    self.lineEdit_3.clear()
                    self.lineEdit_4.clear()
                    self.lineEdit_5.clear()
                    self.lineEdit_6.clear()
                    self.lineEdit_7.clear()
                    self.lineEdit_8.clear()
                    self.lineEdit_9.clear()
                    self.lineEdit_10.clear()
                    self.lineEdit_11.clear()
                    self.bul()
            else:
                pass
        else:
            self.yaz.gemi_guncelle(self.lineEdit_2.text(),
                                   self.lineEdit_3.text(),
                                   self.lineEdit_4.text(),
                                   self.lineEdit_5.text(),
                                   self.lineEdit_6.text(),
                                   self.lineEdit_7.text(),
                                   self.lineEdit_8.text(),
                                   self.lineEdit_9.text(),
                                   self.lineEdit_10.text(),
                                   self.lineEdit_11.text(),
                                   self.gemi_id
                                   )
            mesaj = self.lineEdit_3.text() + " Gemisinin Kaydı Başarıyla Değiştirildi"
            mes.uyari(mesaj, "Bilgilendirme")
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
            self.lineEdit_8.clear()
            self.lineEdit_9.clear()
            self.lineEdit_10.clear()
            self.lineEdit_11.clear()


class Ui_GemiSil(VbagKur):
    def __init__(self):
        self.yaz = VbagKur()
        self.gemi_id = 0

    def setupUi(self, GemiSil):
        GemiSil.setObjectName("GemiSil")
        GemiSil.resize(456, 399)
        self.gridLayout_2 = QtWidgets.QGridLayout(GemiSil)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(GemiSil)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(GemiSil)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.listWidget = QtWidgets.QListWidget(GemiSil)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 1, 0, 1, 2)
        self.frame = QtWidgets.QFrame(GemiSil)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 5, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 6, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 7, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 7, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 8, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 8, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 9, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 9, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(53, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 10, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 10, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 2, 1, 1)

        self.retranslateUi(GemiSil)
        QtCore.QMetaObject.connectSlotsByName(GemiSil)
        self.lineEdit.textChanged['QString'].connect(self.bul)
        self.listWidget.doubleClicked['QModelIndex'].connect(self.doldur)
        self.pushButton_2.clicked.connect(self.sil)

    def retranslateUi(self, GemiSil):
        _translate = QtCore.QCoreApplication.translate
        GemiSil.setWindowTitle(_translate("GemiSil", "Gemi Kaydı Sil"))
        self.label.setText(_translate("GemiSil", "Gemi Adı"))
        self.label_3.setText(_translate("GemiSil", "Müşteri Kod"))
        self.label_4.setText(_translate("GemiSil", "Gemi Adı"))
        self.label_5.setText(_translate("GemiSil", "Gemi No"))
        self.label_6.setText(_translate("GemiSil", "Gemi Cinsi"))
        self.label_7.setText(_translate("GemiSil", "Defter No"))
        self.label_8.setText(_translate("GemiSil", "Belge No"))
        self.label_9.setText(_translate("GemiSil", "Sicil No"))
        self.label_10.setText(_translate("GemiSil", "İmo / Çağrı"))
        self.label_12.setText(_translate("GemiSil", "Acenta "))
        self.label_13.setText(_translate("GemiSil", "Acenta Tel"))
        self.pushButton_2.setText(_translate("GemiSil", "Sil"))

    def bul(self):
        self.listWidget.clear()
        sonuc = self.yaz.coklu_komut("SELECT gad FROM gemiler WHERE gad LIKE '{}'".format(self.lineEdit.text() + "%"))
        if len(sonuc) == 0:
            self.listWidget.addItem("Sonuç Bulunamadı")
        else:
            for i in range(len(sonuc)):
                self.listWidget.addItem(sonuc[i][0])

    def doldur(self):
        soru = self.yaz.tek_oku("gemiler", "gad", self.listWidget.currentItem().text())
        self.lineEdit_2.setText(str(soru[0][1]))
        self.lineEdit_3.setText(soru[0][2])
        self.lineEdit_4.setText(soru[0][3])
        self.lineEdit_5.setText(soru[0][4])
        self.lineEdit_6.setText(soru[0][5])
        self.lineEdit_7.setText(soru[0][6])
        self.lineEdit_8.setText(soru[0][7])
        self.lineEdit_9.setText(soru[0][8])
        self.lineEdit_10.setText(soru[0][9])
        self.lineEdit_11.setText(soru[0][10])
        self.gemi_id = soru[0][0]

    def sil(self):
        mesaj = """{} gemisinin bilgilerini silmek istediğinizden emin misiniz ? """.format(self.lineEdit_3.text())
        sor = mes.soru("Gemi Bilgilerini Silmek Üzeresiniz !!", mesaj,
                       "Gemi Bilgileri Siliniyor",
                       "İşlem  iptal edildi")
        if sor == True:
            self.yaz.kayit_sil("gemiler", "id", self.gemi_id)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
            self.lineEdit_8.clear()
            self.lineEdit_9.clear()
            self.lineEdit_10.clear()
            self.lineEdit_11.clear()
            self.bul()
        else:
            pass


class Ui_BolgeEkle(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_BolgeEkle, self).__init__()
        self.yaz = VbagKur()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("BolgeEkle")
        self.resize(366, 133)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/rolix/docky.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, -1, 100, 100))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/rolix/docky.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(140, 20, 60, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(210, 20, 130, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 50, 130, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(140, 50, 60, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(270, 90, 72, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi()
        self.pushButton.clicked.connect(self.ekle)
        QtCore.QMetaObject.connectSlotsByName(self)

    def ekle(self):
        if self.lineEdit.text() =="" or self.lineEdit_2.text() == "":
            mesaj = " Bilgileri tam olarak giriniz"
            mes.uyari(mesaj, "Uyarı")
        else:
            self.yaz.bolge_ekle(self.lineEdit.text(), self.lineEdit_2.text())
            mesaj = self.lineEdit_2.text() + " Bölgesi Veritanına eklendi"
            mes.uyari(mesaj, "Bilgilendirme")
            self.lineEdit.clear()
            self.lineEdit_2.clear()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("BolgeEkle", "Bölge Ekle"))
        self.label_2.setText(_translate("BolgeEkle", "Bölge Kodu"))
        self.label_3.setText(_translate("BolgeEkle", "Bölge Adı"))
        self.pushButton.setText(_translate("BolgeEkle", "Ekle"))


class Ui_BolgeYerSil(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_BolgeYerSil, self).__init__()
        self.yaz = VbagKur()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("BolgeSil")
        self.resize(416, 316)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/rolix/docky.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/rolix/scalable/package-remove.svg"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.bilgi_listele()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.listWidget.doubleClicked['QModelIndex'].connect(self.sil)

    def retranslateUi(self, BolgeYerSil):
        _translate = QtCore.QCoreApplication.translate
        BolgeYerSil.setWindowTitle(_translate("BolgeYerSil", "Bölge Ve Yer Sil"))
        self.groupBox.setTitle(_translate("BolgeYerSil", "Bölge Listesi"))
        self.label_2.setText(_translate("BolgeYerSil", "Veritabanından silmek istediğiniz Bölgeye çift tıklayınız."))

    def bilgi_listele(self):
        self.listWidget.addItems(self.yaz.coklu_tup_temizle(self.yaz.kolon_oku("ad, kod", "bolge")))

    def sil(self):
        if mes.yerbolsil(self.listWidget.currentItem().text()) == True:
            self.yaz.kayit_sil("bolge", "ad", self.listWidget.currentItem().text())
            self.listWidget.clear()
            self.bilgi_listele()
        else:
            pass


class Ui_PersonelEkle(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_PersonelEkle, self).__init__()
        self.yaz = VbagKur()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("PersonelEkle")
        self.resize(430, 148)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(150, 20, 90, 20))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(250, 20, 150, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(250, 50, 150, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(150, 50, 90, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(300, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 121, 121))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/rolix/config-users.png"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi()
        self.pushButton.clicked.connect(self.persekle)
        QtCore.QMetaObject.connectSlotsByName(self)

    def persekle(self):
        if self.lineEdit.text() == "":
            mesaj = "Hayaletler teslimat yapamaz"
            mes.uyari(mesaj, "Oppss")
        else:
            self.yaz.personel_ekle(self.comboBox.currentIndex(),
                               self.lineEdit.text())
            mesaj = self.lineEdit.text() + " "  + self.comboBox.currentText() +" olarak veritabanına eklendi"
            mes.uyari(mesaj, "Bilgilendirme")
            self.lineEdit.clear()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("PersonelEkle", "Personel Ekle"))
        self.label.setText(_translate("PersonelEkle", "Bağlı Olduğu Yer"))
        self.comboBox.setItemText(0, _translate("PersonelEkle", "İntertek çalışanı"))
        self.comboBox.setItemText(1, _translate("PersonelEkle", "Barge/Terminal çalışanı"))
        self.label_2.setText(_translate("PersonelEkle", "Ad Soyad"))
        self.pushButton.setText(_translate("PersonelEkle", "Ekle"))


class Ui_PersonelSil(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_PersonelSil, self).__init__()
        self.yaz = VbagKur()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("PersonelSil")
        self.resize(452, 197)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/rolix/dialog-error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/rolix/dialog-error.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setGeometry(QtCore.QRect(120, 10, 311, 141))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(360, 160, 73, 23))
        self.pushButton.setObjectName("pushButton")
        self.personel_bul()

        self.retranslateUi()
        self.pushButton.clicked.connect(self.perisil)
        self.listWidget.itemDoubleClicked['QListWidgetItem*'].connect(self.perisil)
        QtCore.QMetaObject.connectSlotsByName(self)

    def personel_bul(self):
        sorgu = self.yaz.kolon_oku("ad", "personel")
        for i in range(len(sorgu)):
            self.listWidget.addItem(sorgu[i][0])

    def perisil(self):
        if mes.per_sil(self.listWidget.currentItem().text()) == True:
            self.yaz.kayit_sil("personel", "ad", self.listWidget.currentItem().text())
            self.listWidget.clear()
            self.personel_bul()
        else:
            pass


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("PersonelSil", "Personel Sil"))
        self.pushButton.setText(_translate("PersonelSil", "Sil"))


class Ui_UrunEkle(object):
    def setupUi(self, UrunEkle):
        UrunEkle.setObjectName("UrunEkle")
        UrunEkle.resize(260, 160)
        UrunEkle.setMinimumSize(QtCore.QSize(260, 160))
        UrunEkle.setMaximumSize(QtCore.QSize(260, 160))
        self.gridLayout = QtWidgets.QGridLayout(UrunEkle)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(UrunEkle)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(UrunEkle)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(UrunEkle)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(UrunEkle)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(UrunEkle)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(UrunEkle)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(156, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(UrunEkle)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 2, 1, 1)

        self.retranslateUi(UrunEkle)
        self.pushButton.clicked.connect(self.ekle)
        QtCore.QMetaObject.connectSlotsByName(UrunEkle)

    def retranslateUi(self, UrunEkle):
        _translate = QtCore.QCoreApplication.translate
        UrunEkle.setWindowTitle(_translate("UrunEkle", "Ürün Ekle"))
        self.label.setText(_translate("UrunEkle", "Ürün Adı"))
        self.label_2.setText(_translate("UrunEkle", "Ürün Kodu"))
        self.label_3.setText(_translate("UrunEkle", "Açıklama"))
        self.pushButton.setText(_translate("UrunEkle", "Ekle"))

    def ekle(self):
        self.yaz = VbagKur()
        if self.lineEdit.text() == "" or self.lineEdit_2.text() == "":
            mesaj = "Ürün kodu ve ürün adını tam olarak doldurunuz"
            mes.uyari(mesaj, "Eksik Bilgi")
        else:
            self.yaz.urun_ekle(self.lineEdit_2.text(), self.lineEdit.text(), self.lineEdit_3.text())
            mesaj = self.lineEdit.text() + " veritabanına kaydedildi"
            mes.uyari(mesaj, "Veritabanına Ürün Ekleme")
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()


class Ui_UrunSil(object):
    def __init__(self):
        self.yaz = VbagKur()

    def setupUi(self, UrunSil):
        UrunSil.setObjectName("UrunSil")
        UrunSil.resize(351, 238)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../../logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UrunSil.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(UrunSil)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(UrunSil)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(UrunSil)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.bul()


        self.retranslateUi(UrunSil)
        self.listWidget.doubleClicked['QModelIndex'].connect(self.sil)
        QtCore.QMetaObject.connectSlotsByName(UrunSil)

    def retranslateUi(self, UrunSil):
        _translate = QtCore.QCoreApplication.translate
        UrunSil.setWindowTitle(_translate("UrunSil", "Ürün Sil"))
        self.label.setText(_translate("UrunSil", "Silmek istediğiniz ürününe çift tıklayınız"))

    def bul(self):
        self.listWidget.clear()
        sorgu = self.yaz.kolon_oku("ad", "urun")
        for i in range(len(sorgu)):
            self.listWidget.addItem(sorgu[i][0])

    def sil(self):
        if mes.urun_sil(self.listWidget.currentItem().text()) == True:
            self.yaz.kayit_sil("urun", "ad", self.listWidget.currentItem().text())
            self.listWidget.clear()
            self.bul()
        else:
            pass


class Ui_Settings(object):
    def setupUi(self, Settings):
        self.db = VbagKur()
        Settings.setObjectName("Settings")
        Settings.resize(478, 182)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../../logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Settings.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Settings)
        self.label.setGeometry(QtCore.QRect(10, 10, 100, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Settings)
        self.lineEdit.setGeometry(QtCore.QRect(130, 10, 291, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Settings)
        self.pushButton.setGeometry(QtCore.QRect(430, 9, 41, 22))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Settings)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 110, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Settings)
        self.pushButton.clicked.connect(self.dosya_kayit_yeri)
        # self.pushButton_2.clicked.connect(self.bilgi_guncelle)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Ayarlar"))
        self.label.setText(_translate("Settings", "Dosya Kayıt Yeri"))
        self.pushButton.setText(_translate("Settings", "Seç"))
        self.pushButton_2.setText(_translate("Settings", "Kaydet"))

    def veritabani_bilgisi_cek(self):
        sql_yer = "select * from ayarlar"
        sonuc = self.db.komut(sql_yer)
        self.lineEdit.setText(sonuc[0][2])
        self.lineEdit_2.setText(sonuc[0][0])
        self.lineEdit_3.setText(sonuc[0][1])

    def dosya_kayit_yeri(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory()
        if directory:
            self.lineEdit.setText(directory)

    def bilgi_guncelle(self):
        yer = self.lineEdit.text()
        ts = self.lineEdit_2.text()
        us = self.lineEdit_3.text()
        sql = "update ayarlar set teslim_suresi = '{}'," \
              "uzatma_suresi = '{}'," \
              "kayit_yeri = '{}'".format(ts, us, yer)
        if self.db.yapistir(sql) == True:
            baslik = "Veritabanı Güncellendi"
            mesaj = "Yapılan değişiklikler veritabanına başarıyla kaydedildi"
            mico.bilgilendir(mesaj, baslik)
        else:
            baslik = "Veritabanı Bağlantı Hatası"
            mesaj = "Veritabanı bağlantı sorunu nedeniyle değişiklikler kaydedilemedi."
            mico.bilgilendir(mesaj, baslik)


class Ui_MainWindow(object):
    def lisans_gui(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    def Folustur(self):
        Firmaolustur = QtWidgets.QDialog()
        ui = Ui_Firmaolustur()
        ui.setupUi(Firmaolustur)
        Firmaolustur.show()
        Firmaolustur.exec_()

    def Fguncelle(self):
        Firmaguncelle = QtWidgets.QDialog()
        ui = Ui_Firmaguncelle()
        ui.setupUi(Firmaguncelle)
        Firmaguncelle.show()
        Firmaguncelle.exec_()

    def Fsil(self):
        Firmasil = QtWidgets.QDialog()
        ui = Ui_Firmasil()
        ui.setupUi(Firmasil)
        Firmasil.show()
        Firmasil.exec_()

    def Gekle(self):
        GemiEkle = QtWidgets.QDialog()
        ui = Ui_GemiEkle()
        ui.setupUi(GemiEkle)
        GemiEkle.show()
        GemiEkle.exec()

    def Gduz(self):
        Fg = QtWidgets.QDialog()
        ui = Ui_Fg()
        ui.setupUi(Fg)
        Fg.show()
        Fg.exec_()

    def Gsil(self):
        GemiSil = QtWidgets.QDialog()
        ui = Ui_GemiSil()
        ui.setupUi(GemiSil)
        GemiSil.show()
        GemiSil.exec_()

    def gui_bolge_ekle(self):
        self.ppp = Ui_BolgeEkle()
        self.ppp.show()
        self.ppp.exec_()
        self.comboBox_30.clear()
        self.comboBox_30.addItems(tslmt.bolge_hazirla())

    def gui_bolge_sil(self):
        ppp = Ui_BolgeYerSil()
        ppp.show()
        ppp.exec_()
        self.comboBox_30.clear()
        self.comboBox_30.addItems(tslmt.bolge_hazirla())

    def gui_personel_ekle(self):
        ppp = Ui_PersonelEkle()
        ppp.show()
        ppp.exec_()
        self.comboBox_10.clear()
        self.comboBox_10.addItems(tslmt.personel_hazirla("0"))
        self.comboBox_16.clear()
        self.comboBox_16.addItems(tslmt.personel_hazirla("1"))

    def gui_personel_sil(self):
        ppp = Ui_PersonelSil()
        ppp.show()
        ppp.exec_()
        self.comboBox_10.clear()
        self.comboBox_10.addItems(tslmt.personel_hazirla("0"))
        self.comboBox_16.clear()
        self.comboBox_16.addItems(tslmt.personel_hazirla("1"))

    def gui_urunekle(self):
        UrunEkle = QtWidgets.QDialog()
        ui = Ui_UrunEkle()
        ui.setupUi(UrunEkle)
        UrunEkle.show()
        UrunEkle.exec_()
        self.comboBox_4.clear()
        self.comboBox_4.addItems(tslmt.urun_hazirla())

    def gui_urunsil(self):
        UrunSil = QtWidgets.QDialog()
        ui = Ui_UrunSil()
        ui.setupUi(UrunSil)
        UrunSil.show()
        UrunSil.exec_()
        self.comboBox_4.clear()
        self.comboBox_4.addItems(tslmt.urun_hazirla())

    def gui_settings(self):
        Settings = QtWidgets.QDialog()
        ui = Ui_Settings()
        ui.setupUi(Settings)
        Settings.show()
        Settings.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(451, 550)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 2, 1, 1, 2)
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 3, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout.addWidget(self.comboBox_4, 3, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 4, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 5, 1, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 6, 1, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 7, 1, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 8, 1, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 9, 1, 1, 2)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 10, 0, 1, 1)
        self.comboBox_10 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_10.setObjectName("comboBox_10")
        self.gridLayout.addWidget(self.comboBox_10, 10, 1, 1, 2)
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 11, 0, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout.addWidget(self.lineEdit_16, 11, 1, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 12, 0, 1, 1)
        self.comboBox_16 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_16.setObjectName("comboBox_16")
        self.gridLayout.addWidget(self.comboBox_16, 12, 1, 1, 2)
        self.label_67 = QtWidgets.QLabel(self.centralwidget)
        self.label_67.setObjectName("label_67")
        self.gridLayout.addWidget(self.label_67, 13, 0, 1, 1)
        self.comboBox_30 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_30.setObjectName("comboBox_30")
        self.gridLayout.addWidget(self.comboBox_30, 13, 1, 1, 2)
        self.label_65 = QtWidgets.QLabel(self.centralwidget)
        self.label_65.setObjectName("label_65")
        self.gridLayout.addWidget(self.label_65, 14, 0, 1, 1)
        self.lineEdit_34 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.gridLayout.addWidget(self.lineEdit_34, 14, 1, 1, 2)
        self.label_61 = QtWidgets.QLabel(self.centralwidget)
        self.label_61.setObjectName("label_61")
        self.gridLayout.addWidget(self.label_61, 15, 0, 1, 1)
        self.lineEdit_33 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.gridLayout.addWidget(self.lineEdit_33, 15, 1, 1, 2)
        self.label_62 = QtWidgets.QLabel(self.centralwidget)
        self.label_62.setObjectName("label_62")
        self.gridLayout.addWidget(self.label_62, 16, 0, 1, 1)
        self.lineEdit_35 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.gridLayout.addWidget(self.lineEdit_35, 16, 1, 1, 2)
        self.label_63 = QtWidgets.QLabel(self.centralwidget)
        self.label_63.setObjectName("label_63")
        self.gridLayout.addWidget(self.label_63, 17, 0, 1, 1)
        self.lineEdit_37 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.gridLayout.addWidget(self.lineEdit_37, 17, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(292, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 18, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 18, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 451, 21))
        self.menubar.setObjectName("menubar")
        self.menuM_teriler = QtWidgets.QMenu(self.menubar)
        self.menuM_teriler.setObjectName("menuM_teriler")
        self.menuGemiler = QtWidgets.QMenu(self.menubar)
        self.menuGemiler.setObjectName("menuGemiler")
        self.menuB_lgeler = QtWidgets.QMenu(self.menubar)
        self.menuB_lgeler.setObjectName("menuB_lgeler")
        self.menuPersonel_Bilgisi = QtWidgets.QMenu(self.menubar)
        self.menuPersonel_Bilgisi.setObjectName("menuPersonel_Bilgisi")
        self.menuAyarlar = QtWidgets.QMenu(self.menubar)
        self.menuAyarlar.setObjectName("menuAyarlar")
        self.menuYak_tlar = QtWidgets.QMenu(self.menubar)
        self.menuYak_tlar.setObjectName("menuYak_tlar")
        self.menuTeslimat = QtWidgets.QMenu(self.menubar)
        self.menuTeslimat.setObjectName("menuTeslimat")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionYeni_M_teri_Ekle = QtWidgets.QAction(MainWindow)
        self.actionYeni_M_teri_Ekle.setObjectName("actionYeni_M_teri_Ekle")
        self.actionM_teri_D_zenle = QtWidgets.QAction(MainWindow)
        self.actionM_teri_D_zenle.setObjectName("actionM_teri_D_zenle")
        self.actionM_teri_Sil = QtWidgets.QAction(MainWindow)
        self.actionM_teri_Sil.setObjectName("actionM_teri_Sil")
        self.actionGemi_Ekle = QtWidgets.QAction(MainWindow)
        self.actionGemi_Ekle.setObjectName("actionGemi_Ekle")
        self.actionGemi_Bilgii_D_zenle = QtWidgets.QAction(MainWindow)
        self.actionGemi_Bilgii_D_zenle.setObjectName("actionGemi_Bilgii_D_zenle")
        self.actionGemi_Sil = QtWidgets.QAction(MainWindow)
        self.actionGemi_Sil.setObjectName("actionGemi_Sil")
        self.actionB_lge_Ekle = QtWidgets.QAction(MainWindow)
        self.actionB_lge_Ekle.setObjectName("actionB_lge_Ekle")
        self.actionYer_Ekle = QtWidgets.QAction(MainWindow)
        self.actionYer_Ekle.setObjectName("actionYer_Ekle")
        self.actionB_lge_Yer_Sil = QtWidgets.QAction(MainWindow)
        self.actionB_lge_Yer_Sil.setObjectName("actionB_lge_Yer_Sil")
        self.actionPersonel_Ekle = QtWidgets.QAction(MainWindow)
        self.actionPersonel_Ekle.setObjectName("actionPersonel_Ekle")
        self.actionPersonel_Sil = QtWidgets.QAction(MainWindow)
        self.actionPersonel_Sil.setObjectName("actionPersonel_Sil")
        self.actionAyarlar_D_zenle = QtWidgets.QAction(MainWindow)
        self.actionAyarlar_D_zenle.setObjectName("actionAyarlar_D_zenle")
        self.actionYak_t_Ekle = QtWidgets.QAction(MainWindow)
        self.actionYak_t_Ekle.setObjectName("actionYak_t_Ekle")
        self.actionYak_t_Sil = QtWidgets.QAction(MainWindow)
        self.actionYak_t_Sil.setObjectName("actionYak_t_Sil")
        self.actionYard_m = QtWidgets.QAction(MainWindow)
        self.actionYard_m.setObjectName("actionYard_m")
        self.actionHakk_nda = QtWidgets.QAction(MainWindow)
        self.actionHakk_nda.setObjectName("actionHakk_nda")
        self.menuM_teriler.addAction(self.actionYeni_M_teri_Ekle)
        self.menuM_teriler.addAction(self.actionM_teri_D_zenle)
        self.menuM_teriler.addAction(self.actionM_teri_Sil)
        self.menuGemiler.addAction(self.actionGemi_Ekle)
        self.menuGemiler.addAction(self.actionGemi_Bilgii_D_zenle)
        self.menuGemiler.addAction(self.actionGemi_Sil)
        self.menuB_lgeler.addAction(self.actionB_lge_Ekle)
        self.menuB_lgeler.addAction(self.actionB_lge_Yer_Sil)
        self.menuPersonel_Bilgisi.addAction(self.actionPersonel_Ekle)
        self.menuPersonel_Bilgisi.addAction(self.actionPersonel_Sil)
        self.menuAyarlar.addAction(self.actionAyarlar_D_zenle)
        self.menuYak_tlar.addAction(self.actionYak_t_Ekle)
        self.menuYak_tlar.addAction(self.actionYak_t_Sil)
        self.menuTeslimat.addAction(self.actionYard_m)
        self.menuTeslimat.addAction(self.actionHakk_nda)
        self.menubar.addAction(self.menuM_teriler.menuAction())
        self.menubar.addAction(self.menuGemiler.menuAction())
        self.menubar.addAction(self.menuB_lgeler.menuAction())
        self.menubar.addAction(self.menuPersonel_Bilgisi.menuAction())
        self.menubar.addAction(self.menuYak_tlar.menuAction())
        self.menubar.addAction(self.menuAyarlar.menuAction())
        self.menubar.addAction(self.menuTeslimat.menuAction())

        #tetikleme
        self.hazirlik()
        self.triggerfinger()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionYeni_M_teri_Ekle.triggered.connect(self.Folustur)
        self.actionM_teri_D_zenle.triggered.connect(self.Fguncelle)
        self.actionM_teri_Sil.triggered.connect(self.Fsil)
        self.actionGemi_Ekle.triggered.connect(self.Gekle)
        self.actionGemi_Bilgii_D_zenle.triggered.connect(self.Gduz)
        self.actionGemi_Sil.triggered.connect(self.Gsil)
        self.actionB_lge_Ekle.triggered.connect(self.gui_bolge_ekle)
        self.actionB_lge_Yer_Sil.triggered.connect(self.gui_bolge_sil)
        self.actionPersonel_Ekle.triggered.connect(self.gui_personel_ekle)
        self.actionPersonel_Sil.triggered.connect(self.gui_personel_sil)
        self.actionYak_t_Ekle.triggered.connect(self.gui_urunekle)
        self.actionYak_t_Sil.triggered.connect(self.gui_urunsil)
        self.actionAyarlar_D_zenle.triggered.connect(self.gui_settings)
        self.actionYard_m.triggered.connect(self.help)
        self.actionHakk_nda.triggered.connect(self.lisans_gui)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tux"))
        self.label_14.setText(_translate("MainWindow", "Danışman"))
        self.comboBox.setItemText(0, _translate("MainWindow", "OPET"))
        self.comboBox.setItemText(1, _translate("MainWindow", "ARMARİN"))
        self.label.setText(_translate("MainWindow", "Müşteri Kodu"))
        self.label_3.setText(_translate("MainWindow", "Gemi Adı"))
        self.label_27.setText(_translate("MainWindow", "Yakıt Türü"))
        self.label_4.setText(_translate("MainWindow", "Yoğunluk"))
        self.label_5.setText(_translate("MainWindow", "Sipariş Miktarı"))
        self.label_11.setText(_translate("MainWindow", "Sıcaklık"))
        self.label_8.setText(_translate("MainWindow", "V.C.F  (T54)"))
        self.label_9.setText(_translate("MainWindow", "Litre"))
        self.label_10.setText(_translate("MainWindow", "Kilogram"))
        self.label_18.setText(_translate("MainWindow", "Teslimatçı"))
        self.label_30.setText(_translate("MainWindow", "Yakıt Alan Gemi C/E"))
        self.label_12.setText(_translate("MainWindow", "Terminal Yetkilisi"))
        self.label_67.setText(_translate("MainWindow", "Bölge"))
        self.label_65.setText(_translate("MainWindow", "Başlama Saati"))
        self.label_61.setText(_translate("MainWindow", "Bitiş Saati"))
        self.label_62.setText(_translate("MainWindow", "Opet Numune Mühür"))
        self.label_63.setText(_translate("MainWindow", "Müşteri Numune Mühür"))
        self.pushButton.setText(_translate("MainWindow", "Oluştur"))
        self.menuM_teriler.setTitle(_translate("MainWindow", "Müşteriler"))
        self.menuGemiler.setTitle(_translate("MainWindow", "Gemiler"))
        self.menuB_lgeler.setTitle(_translate("MainWindow", "Bölgeler"))
        self.menuPersonel_Bilgisi.setTitle(_translate("MainWindow", "Personel Bilgisi"))
        self.menuAyarlar.setTitle(_translate("MainWindow", "Ayarlar"))
        self.menuYak_tlar.setTitle(_translate("MainWindow", "Ürünler"))
        self.menuTeslimat.setTitle(_translate("MainWindow", "Yardım"))
        self.actionYeni_M_teri_Ekle.setText(_translate("MainWindow", "Yeni Müşteri Ekle"))
        self.actionM_teri_D_zenle.setText(_translate("MainWindow", "Müşteri Düzenle"))
        self.actionM_teri_Sil.setText(_translate("MainWindow", "Müşteri Sil"))
        self.actionGemi_Ekle.setText(_translate("MainWindow", "Gemi Ekle"))
        self.actionGemi_Bilgii_D_zenle.setText(_translate("MainWindow", "Gemi Bilgii Düzenle"))
        self.actionGemi_Sil.setText(_translate("MainWindow", "Gemi Sil"))
        self.actionB_lge_Ekle.setText(_translate("MainWindow", "Bölge Ekle"))
        self.actionYer_Ekle.setText(_translate("MainWindow", "Yer Ekle"))
        self.actionB_lge_Yer_Sil.setText(_translate("MainWindow", "Bölge  Sil"))
        self.actionPersonel_Ekle.setText(_translate("MainWindow", "Personel Ekle"))
        self.actionPersonel_Sil.setText(_translate("MainWindow", "Personel Sil"))
        self.actionAyarlar_D_zenle.setText(_translate("MainWindow", "Ayarları Düzenle"))
        self.actionYak_t_Ekle.setText(_translate("MainWindow", "Ürün Ekle"))
        self.actionYak_t_Sil.setText(_translate("MainWindow", "Ürün Sil"))
        self.actionYard_m.setText(_translate("MainWindow", "Tux Yardım"))
        self.actionHakk_nda.setText(_translate("MainWindow", "Tux Hakkında"))

    def hazirlik(self):
        """ Teslimatçıları listele  """
        self.comboBox_10.addItems(tslmt.personel_hazirla("0"))

        """ Bölgeleri veritabanından çek """
        self.comboBox_30.addItems(tslmt.bolge_hazirla())

        """ Ürünleri veritabanından çek """
        self.comboBox_4.addItems(tslmt.urun_hazirla())

        """ Gemi çalışanlarını Hazırla  """
        self.comboBox_16.addItems(tslmt.personel_hazirla("1"))

    def tgemi(self):
        self.comboBox_2.clear()
        self.comboBox_2.addItems(tslmt.gemi_listele(self.lineEdit.text()))

    def vcf_hesapla(self):
        sonuc = tslmt.v_c_f(self.lineEdit_2.text(),
                            self.lineEdit_3.text(),
                            self.lineEdit_8.text())

        self.lineEdit_5.setText(sonuc[0])
        self.lineEdit_6.setText(sonuc[1])
        self.lineEdit_7.setText(sonuc[2])

    def olustur(self):
        """ Artık Veritabanına bilgileri eklemek için değişkenleri almaya başlamamız lazım  """

        musteri_kodu = self.lineEdit.text()
        gemi = self.comboBox_2.currentText()
        yakit_turu = self.comboBox_4.currentText()
        yogunluk = self.lineEdit_2.text()
        brut_litre = self.lineEdit_3.text()
        sicaklik = self.lineEdit_8.text()
        net_litre = self.lineEdit_6.text()
        volum_correction = self.lineEdit_5.text()
        kilogram = self.lineEdit_7.text()
        teslimatci = self.comboBox_10.currentText()
        yakit_alan_kisi = self.lineEdit_16.text()
        gemici = self.comboBox_16.currentText()
        bolge = self.comboBox_30.currentText()
        baslama_saati = self.lineEdit_34.text()
        bitis_saati = self.lineEdit_33.text()
        barge_numune_muhur = self.lineEdit_35.text()
        gemi_numune_muhur = self.lineEdit_37.text()


        mesaj = gemi + " gemisine ait " + net_litre + \
                " litrelik teslimat bilgisi veritabanına eklendi. Teslimat dosyaları oluşturuluyor"
        mes.uyari(mesaj, "Bilgilendirme")

        tslmt.teslimat_hazirliği_yap(musteri_kodu, gemi, yakit_turu, yogunluk,
                                     brut_litre, sicaklik, volum_correction, net_litre, kilogram,
                                     teslimatci, yakit_alan_kisi, gemici,
                                     bolge, baslama_saati, bitis_saati, barge_numune_muhur, gemi_numune_muhur)

        self.lineEdit.clear()
        self.comboBox_2.clear()
        self.comboBox_4.setCurrentIndex(0)
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.lineEdit_33.clear()
        self.lineEdit_34.clear()
        self.lineEdit_35.clear()
        self.lineEdit_37.clear()
        self.lineEdit_16.clear()


    def help(self):
        yol = os.getcwd()
        tam_yol = yol + "\lib\help\index.html"
        chromedir = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chromedir).open(tam_yol)

    def triggerfinger(self):
        self.lineEdit.returnPressed.connect(self.tgemi)
        self.lineEdit_8.returnPressed.connect(self.vcf_hesapla)
        self.pushButton.clicked.connect(self.olustur)

import ic_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
