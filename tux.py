# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '\lib\gui\tux.ui'
#
# Author : Mehmet Eroğlu
#

from PyQt5 import QtCore, QtGui, QtWidgets
from vtbgln import VbagKur
import mesajlar as mes
import os
import webbrowser
import tslmt
from turekle import Ui_CinsEkle


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(417, 341)
        Dialog.setMinimumSize(QtCore.QSize(417, 341))
        Dialog.setMaximumSize(QtCore.QSize(417, 341))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lib\gui\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
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
        self.plainTextEdit.setPlainText(_translate("Dialog",
                                                   "Tux özgür bir yazılımdır, Özgür Yazılım Vakfı\'nın yayınladığı GNU Genel Kamu Lisansı\'nın 3. veya daha sonraki sürümlerindeki şartlar altında dağıtılabilir ve/veya değiştirilebilir. \n"
                                                   "\n"
                                                   "Tux faydalı olacağı umut edilerek dağıtılmaktadır, fakat HİÇBİR GARANTİSİ YOKTUR; hatta ÜRÜN DEĞERİ ya da BİR AMACA UYGUNLUK gibi garantiler de vermez. Lütfen daha çok ayrıntı için GNU Genel Kamu Lisansı\'nı inceleyin. \n"
                                                   "\n"
                                                   "Tux ile beraber GNU Genel Kamu Lisansını da almış olmalısınız; eğer almadıysanız, https://www.gnu.org/licenses/ adresine bakın."

                                                   ))


class Ui_Firmaolustur(VbagKur):
    def __init__(self):
        self.yaz = VbagKur()

    def setupUi(self, Firmaolustur):
        Firmaolustur.setObjectName("Firmaolustur")
        Firmaolustur.resize(400, 318)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lib\gui\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Firmaolustur.setWindowIcon(icon)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lib\gui\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Firmaguncelle.setWindowIcon(icon)
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
        elif ad == " ":
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
        sonuc = self.yaz.coklu_komut("SELECT ad FROM firmalar WHERE ad LIKE '{}'".format(self.lineEdit_6.text() + "%"))
        if len(sonuc) == 0:
            self.listWidget.addItem("Sonuç Bulunamadı")
        else:
            for i in range(len(sonuc)):
                self.listWidget.addItem(sonuc[i][0])

    def doldur(self):
        veri = self.yaz.komut("SELECT * FROM firmalar WHERE ad='{}'".format(self.listWidget.currentItem().text()))
        self.eski_kod = veri[1]
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lib\gui\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Firmasil.setWindowIcon(icon)
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
        sonuc = self.yaz.coklu_komut("SELECT ad FROM firmalar WHERE ad LIKE '{}'".format(self.lineEdit_6.text() + "%"))
        if len(sonuc) == 0:
            self.listWidget.addItem("Sonuç Bulunamadı")
        else:
            for i in range(len(sonuc)):
                self.listWidget.addItem(sonuc[i][0])

    def doldur(self):
        veri = self.yaz.komut("SELECT * FROM firmalar WHERE ad='{}'".format(self.listWidget.currentItem().text()))
        self.eski_kod = veri[1]
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
              Gemi bilgisi düzenleme kısmından yeni bir müşteri ile ilişkilendirebilirsiniz)""".format(
                self.lineEdit_2.text(),
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


class Ui_GemiEkle(object):
    def __init__(self):
        self.yaz = VbagKur()
        self.firma_ad = ""
        self.firma_kod = 0

    def gui_cins(self):
        Cins = QtWidgets.QDialog()
        cins_ui = Ui_CinsEkle()
        cins_ui.setupUi(Cins)
        Cins.show()
        Cins.exec_()
        self.gemi_tur()

    def setupUi(self, GemiEkle):
        GemiEkle.setObjectName("GemiEkle")
        GemiEkle.resize(563, 369)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lib\gui\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GemiEkle.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(GemiEkle)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(GemiEkle)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(GemiEkle)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_2.addWidget(self.lineEdit_11, 0, 1, 1, 2)
        self.listWidget = QtWidgets.QListWidget(GemiEkle)
        self.listWidget.setMaximumSize(QtCore.QSize(221, 321))
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
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 5, 1, 1, 3)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 6, 1, 1, 3)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 7, 1, 1, 3)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 8, 1, 1, 3)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 9, 1, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 10, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 10, 2, 1, 2)
        self.gridLayout_2.addWidget(self.frame, 1, 2, 1, 1)
        self.gemi_tur()

        self.retranslateUi(GemiEkle)
        QtCore.QMetaObject.connectSlotsByName(GemiEkle)
        self.lineEdit_11.textChanged['QString'].connect(self.bul)
        self.listWidget.doubleClicked['QModelIndex'].connect(self.doldur)
        self.pushButton.clicked.connect(self.ekle)
        self.pushButton_3.clicked.connect(self.gui_cins)

    def retranslateUi(self, GemiEkle):
        _translate = QtCore.QCoreApplication.translate
        GemiEkle.setWindowTitle(_translate("GemiEkle", "Gemi Ekle"))
        self.label_11.setText(_translate("GemiEkle", "Firma Bul"))
        self.label.setText(_translate("GemiEkle", "Müşteri Adı"))
        self.label_2.setText(_translate("GemiEkle", "Gemi Adı"))
        self.label_3.setText(_translate("GemiEkle", "Gemi Kodu"))
        self.label_4.setText(_translate("GemiEkle", "Gemi Cinsi"))
        self.pushButton_3.setText(_translate("GemiEkle", "Ekle"))
        self.label_5.setText(_translate("GemiEkle", "Defter No"))
        self.label_6.setText(_translate("GemiEkle", "Belge No"))
        self.label_7.setText(_translate("GemiEkle", "Sicil No"))
        self.label_8.setText(_translate("GemiEkle", "İmo / Çağrı İşareti"))
        self.label_9.setText(_translate("GemiEkle", "Acenta"))
        self.label_10.setText(_translate("GemiEkle", "Acenta Tel"))
        self.pushButton.setText(_translate("GemiEkle", "Gemi Ekle"))

    def gemi_tur(self):
        self.comboBox.clear()
        sonuc = self.yaz.kolon_oku("tur", "gemitur")
        for i in range(len(sonuc)):
            self.comboBox.addItem(sonuc[i][0])


    def bul(self):
        self.listWidget.clear()
        sonuc = self.yaz.coklu_komut(
            "SELECT ad, kod FROM firmalar WHERE ad LIKE '{}'".format(self.lineEdit_11.text() + "%"))
        if len(sonuc) == 0:
            self.listWidget.addItem("Sonuç Bulunamadı")
        else:
            for i in range(len(sonuc)):
                self.listWidget.addItem(sonuc[i][0])
                self.firma_ad = sonuc[i][0]
                self.firma_kod = sonuc[i][1]

    def doldur(self):
        self.lineEdit.setText(self.firma_ad)

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
            liste.append(self.firma_kod)
            liste.append(self.lineEdit_2.text())
            liste.append(self.lineEdit_3.text())
            liste.append(self.comboBox.currentText())
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
            self.comboBox.setCurrentIndex(0)
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
            self.lineEdit_8.clear()
            self.lineEdit_9.clear()
            self.lineEdit_10.clear()


class Ui_Fg(object):
    def __init__(self):
        self.yaz = VbagKur()
        self.yeni_firma = Ui_FirmaBul()

        self.gemi_id = 0
        self.firma_ad = ""
        self.firma_kod = 0

        self.yeni_firma_ad = ""
        self.yeni_firma_kod = 0

    def gupgui(self):
        GFirmaBul = QtWidgets.QDialog()
        ggui = Ui_FirmaBul()
        ggui.setupUi(GFirmaBul)
        GFirmaBul.show()
        GFirmaBul.exec_()
        self.yenikodlar(ggui.firma, ggui.kod)

    def gui_cins(self):
        Cins = QtWidgets.QDialog()
        cins_ui = Ui_CinsEkle()
        cins_ui.setupUi(Cins)
        Cins.show()
        Cins.exec_()
        self.gemi_tur()


    def setupUi(self, Fg):
        Fg.setObjectName("Fg")
        Fg.resize(528, 371)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lib\gui\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Fg.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(Fg)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(Fg)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
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
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(41, 23))
        self.pushButton.setMaximumSize(QtCore.QSize(41, 23))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 2, 1, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setMinimumSize(QtCore.QSize(41, 23))
        self.pushButton_3.setMaximumSize(QtCore.QSize(41, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 4, 1, 1, 3)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 5, 1, 1, 3)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 6, 1, 1, 3)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 7, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 7, 1, 1, 3)
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 8, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 8, 1, 1, 3)
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 9, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 9, 1, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(53, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 10, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 10, 2, 1, 2)
        self.gridLayout_2.addWidget(self.frame, 1, 2, 1, 1)
        self.gemi_tur()

        self.retranslateUi(Fg)
        self.lineEdit.textChanged['QString'].connect(self.bul)
        self.listWidget.doubleClicked['QModelIndex'].connect(self.doldur)
        self.pushButton_2.clicked.connect(self.guncelle)
        #

        self.pushButton.clicked.connect(self.gupgui)
        self.pushButton_3.clicked.connect(self.gui_cins)
        QtCore.QMetaObject.connectSlotsByName(Fg)

    def retranslateUi(self, Fg):
        _translate = QtCore.QCoreApplication.translate
        Fg.setWindowTitle(_translate("Fg", "Gemi Bilgisi Düzenle"))
        self.label.setText(_translate("Fg", "Gemi Adı"))
        self.label_3.setText(_translate("Fg", "Müşteri Adı"))
        self.pushButton.setText(_translate("Fg", "Bul"))
        self.label_4.setText(_translate("Fg", "Gemi Adı"))
        self.label_5.setText(_translate("Fg", "Gemi No"))
        self.label_6.setText(_translate("Fg", "Gemi Cinsi"))
        self.pushButton_3.setText(_translate("Fg", "Ekle"))
        self.label_7.setText(_translate("Fg", "Defter No"))
        self.label_8.setText(_translate("Fg", "Belge No"))
        self.label_9.setText(_translate("Fg", "Sicil No"))
        self.label_10.setText(_translate("Fg", "İmo / Çağrı"))
        self.label_12.setText(_translate("Fg", "Acenta "))
        self.label_13.setText(_translate("Fg", "Acenta Tel"))
        self.pushButton_2.setText(_translate("Fg", "Güncelle"))

    def yenikodlar(self, ad, kod):
        self.yeni_firma_ad = ad
        self.yeni_firma_kod = kod
        self.lineEdit_2.setText(self.yeni_firma_ad)

    def gemi_tur(self):
        self.comboBox.clear()
        sonuc = self.yaz.kolon_oku("tur", "gemitur")
        for i in range(len(sonuc)):
            self.comboBox.addItem(sonuc[i][0])


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
        self.firma_kod = soru[0][1]
        fad = self.yaz.komut("select ad from firmalar where kod='{}'".format(self.firma_kod))
        self.firma_ad = fad[0]

        self.lineEdit_2.setText(self.firma_ad)
        self.lineEdit_3.setText(soru[0][2])
        self.lineEdit_4.setText(soru[0][3])
        self.comboBox.setCurrentText(soru[0][4])
        self.lineEdit_6.setText(soru[0][5])
        self.lineEdit_7.setText(soru[0][6])
        self.lineEdit_8.setText(soru[0][7])
        self.lineEdit_9.setText(soru[0][8])
        self.lineEdit_10.setText(soru[0][9])
        self.lineEdit_11.setText(soru[0][10])
        self.gemi_id = soru[0][0]


    def guncelle(self):
        if self.firma_ad != self.lineEdit_2.text():
            mesaj = """Geminin bağlı olduğu Müşteriyi değiştirdiniz.
            Devam ederseniz geminin {} firması ile olan bağlantısı kesilip {} göre ilişkilendirilecektir""".format(
                self.firma_ad, self.yeni_firma_ad)
            sor = mes.soru("Müşteri Kodunu Değiştirdiniz !!", mesaj,
                           "Gemi yeni müşterinin  koduna ilişkilendiriliyor",
                           "Müşteri kod değişimi iptal edildi")
            if sor == True:
                self.yaz.gemi_guncelle(self.yeni_firma_kod,
                                       self.lineEdit_3.text(),
                                       self.lineEdit_4.text(),
                                       self.comboBox.currentText(),
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
                self.comboBox.setCurrentIndex(0)
                self.lineEdit_6.clear()
                self.lineEdit_7.clear()
                self.lineEdit_8.clear()
                self.lineEdit_9.clear()
                self.lineEdit_10.clear()
                self.lineEdit_11.clear()
                self.bul()
        else:
            self.yaz.gemi_guncelle(self.firma_kod,
                                   self.lineEdit_3.text(),
                                   self.lineEdit_4.text(),
                                   self.comboBox.currentText(),
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
            self.comboBox.setCurrentIndex(0)
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
            self.lineEdit_8.clear()
            self.lineEdit_9.clear()
            self.lineEdit_10.clear()
            self.lineEdit_11.clear()
            self.bul()


class Ui_GemiSil(VbagKur):
    def __init__(self):
        self.yaz = VbagKur()
        self.gemi_id = 0

    def setupUi(self, GemiSil):
        GemiSil.setObjectName("GemiSil")
        GemiSil.resize(456, 399)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lib\gui\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GemiSil.setWindowIcon(icon)
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
        icon.addPixmap(QtGui.QPixmap("lib\gui\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        if self.lineEdit.text() == "" or self.lineEdit_2.text() == "":
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
        icon.addPixmap(QtGui.QPixmap("lib\gui\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lib\gui\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
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
            mesaj = self.lineEdit.text() + " " + self.comboBox.currentText() + " olarak veritabanına eklendi"
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
        icon.addPixmap(QtGui.QPixmap("lib\gui\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lib\gui\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UrunEkle.setWindowIcon(icon)
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
        icon.addPixmap(QtGui.QPixmap("lib\gui\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
    def __init__(self):
        self.yaz = VbagKur()
        self.irsaliye = None
        self.ek_1 = None
        self.kontrol_cizelgesi = None
        self.defter = None
        self.subis = None
        self.numunevrak = None

    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(494, 283)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lib\gui\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Settings.setWindowIcon(icon)
        self.listWidget = QtWidgets.QListWidget(Settings)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 151, 251))
        self.listWidget.setMovement(QtWidgets.QListView.Static)
        self.listWidget.setFlow(QtWidgets.QListView.TopToBottom)
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.stackedWidget = QtWidgets.QStackedWidget(Settings)
        self.stackedWidget.setGeometry(QtCore.QRect(170, 10, 350, 269))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setGeometry(QtCore.QRect(0, 0, 332, 251))
        self.frame.setMinimumSize(QtCore.QSize(332, 251))
        self.frame.setMaximumSize(QtCore.QSize(332, 251))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_6.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_6.addWidget(self.pushButton, 0, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_5.addWidget(self.checkBox_3, 1, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_5.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_5.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_5.addWidget(self.checkBox_4, 1, 1, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_5.addWidget(self.checkBox_5, 2, 0, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_5.addWidget(self.checkBox_6, 2, 1, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox, 1, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 68, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 3, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(75, 25))
        self.pushButton_2.setMaximumSize(QtCore.QSize(75, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_6.addWidget(self.pushButton_2, 3, 2, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.frame_2 = QtWidgets.QFrame(self.page_2)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 332, 251))
        self.frame_2.setMinimumSize(QtCore.QSize(332, 251))
        self.frame_2.setMaximumSize(QtCore.QSize(332, 251))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_4.addWidget(self.lineEdit_9, 0, 1, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_4.addWidget(self.lineEdit_10, 1, 1, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_7.addWidget(self.comboBox, 0, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_7.addWidget(self.comboBox_2, 0, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_7.addWidget(self.comboBox_3, 0, 2, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout_7.addWidget(self.comboBox_4, 0, 3, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout_7.addWidget(self.comboBox_5, 0, 4, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_7.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.gridLayout_7.addWidget(self.lineEdit_19, 1, 1, 1, 1)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.gridLayout_7.addWidget(self.lineEdit_20, 1, 2, 1, 1)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.gridLayout_7.addWidget(self.lineEdit_21, 1, 3, 1, 1)
        self.lineEdit_30 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.gridLayout_7.addWidget(self.lineEdit_30, 1, 4, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.gridLayout_7.addWidget(self.comboBox_6, 2, 0, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.gridLayout_7.addWidget(self.comboBox_7, 2, 1, 1, 1)
        self.comboBox_8 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.gridLayout_7.addWidget(self.comboBox_8, 2, 2, 1, 1)
        self.comboBox_9 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.gridLayout_7.addWidget(self.comboBox_9, 2, 3, 1, 1)
        self.comboBox_10 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.gridLayout_7.addWidget(self.comboBox_10, 2, 4, 1, 1)
        self.lineEdit_31 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.gridLayout_7.addWidget(self.lineEdit_31, 3, 0, 1, 1)
        self.lineEdit_32 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.gridLayout_7.addWidget(self.lineEdit_32, 3, 1, 1, 1)
        self.lineEdit_33 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.gridLayout_7.addWidget(self.lineEdit_33, 3, 2, 1, 1)
        self.lineEdit_34 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.gridLayout_7.addWidget(self.lineEdit_34, 3, 3, 1, 1)
        self.lineEdit_35 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.gridLayout_7.addWidget(self.lineEdit_35, 3, 4, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 2, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 3, 0, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(75, 25))
        self.pushButton_3.setMaximumSize(QtCore.QSize(75, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 3, 2, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.frame_3 = QtWidgets.QFrame(self.page_3)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 332, 251))
        self.frame_3.setMinimumSize(QtCore.QSize(332, 251))
        self.frame_3.setMaximumSize(QtCore.QSize(332, 251))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 0, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_3.addWidget(self.lineEdit_4, 1, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_3.addWidget(self.lineEdit_5, 2, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_3.addWidget(self.lineEdit_6, 3, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 4, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_3.addWidget(self.lineEdit_7, 4, 1, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 69, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 5, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(201, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 6, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setMinimumSize(QtCore.QSize(75, 25))
        self.pushButton_4.setMaximumSize(QtCore.QSize(75, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 6, 2, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.frame_4 = QtWidgets.QFrame(self.page_4)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 332, 276))
        self.frame_4.setMinimumSize(QtCore.QSize(332, 251))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_2.addWidget(self.lineEdit_8, 0, 1, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.lineEdit_36 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_36.setText("")
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.gridLayout_2.addWidget(self.lineEdit_36, 1, 1, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 173, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 2, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 3, 0, 1, 2)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_5.setMinimumSize(QtCore.QSize(75, 25))
        self.pushButton_5.setMaximumSize(QtCore.QSize(75, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 3, 2, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.frame_5 = QtWidgets.QFrame(self.page_5)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 329, 253))
        self.frame_5.setMaximumSize(QtCore.QSize(435, 275))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout.setObjectName("gridLayout")
        self.label_12 = QtWidgets.QLabel(self.frame_5)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 0, 1, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.frame_5)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_12.setText("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout.addWidget(self.lineEdit_12, 1, 1, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.frame_5)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 0, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_13.setText("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout.addWidget(self.lineEdit_13, 2, 1, 1, 2)
        self.label_15 = QtWidgets.QLabel(self.frame_5)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 3, 0, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_14.setText("")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout.addWidget(self.lineEdit_14, 3, 1, 1, 2)
        self.label_16 = QtWidgets.QLabel(self.frame_5)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 4, 0, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_15.setText("")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout.addWidget(self.lineEdit_15, 4, 1, 1, 2)
        self.label_17 = QtWidgets.QLabel(self.frame_5)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 5, 0, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_16.setText("")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout.addWidget(self.lineEdit_16, 5, 1, 1, 2)
        self.label_18 = QtWidgets.QLabel(self.frame_5)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 6, 0, 1, 1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_17.setText("")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout.addWidget(self.lineEdit_17, 6, 1, 1, 2)
        self.label_19 = QtWidgets.QLabel(self.frame_5)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 7, 0, 1, 1)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_18.setText("")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout.addWidget(self.lineEdit_18, 7, 1, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 8, 0, 1, 2)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_6.setMinimumSize(QtCore.QSize(75, 25))
        self.pushButton_6.setMaximumSize(QtCore.QSize(75, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 8, 2, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        self.bul()

        self.retranslateUi(Settings)
        self.listWidget.clicked['QModelIndex'].connect(self.slide)
        self.checkBox.stateChanged.connect(self.checkbox_irsaliye)
        self.checkBox_2.stateChanged.connect(self.checkbox_ek_1)
        self.checkBox_3.stateChanged.connect(self.checkbox_kcizelgesi)
        self.checkBox_4.stateChanged.connect(self.checkbox_defter)
        self.checkBox_5.stateChanged.connect(self.checkbox_subis)
        self.checkBox_6.stateChanged.connect(self.checkbox_numune)
        self.pushButton_2.clicked.connect(self.dosya_islemleri_guncelle)
        self.pushButton_3.clicked.connect(self.sorgu_islemleri_guncelle)
        self.pushButton_4.clicked.connect(self.rate_vhc_guncelle)
        self.pushButton_5.clicked.connect(self.lisans_guncelle)
        self.pushButton_6.clicked.connect(self.ek_1_gemi_bilgisi_guncelle)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Ayarlar"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Settings", "Dosya İşlemleri"))
        item = self.listWidget.item(1)
        item.setText(_translate("Settings", "Sorgulama"))
        item = self.listWidget.item(2)
        item.setText(_translate("Settings", "EK-2 VHC & Rate Bilgileri"))
        item = self.listWidget.item(3)
        item.setText(_translate("Settings", "Dağıtıcı"))
        item = self.listWidget.item(4)
        item.setText(_translate("Settings", "EK-1 Gemi Bilgileri"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Settings", "Dosya Kayıt Yeri"))
        self.pushButton.setText(_translate("Settings", "Seç"))
        self.groupBox.setTitle(_translate("Settings", "Oluşturulacak Evraklar"))
        self.checkBox_3.setText(_translate("Settings", "Kontrol Çizelgesi"))
        self.checkBox.setText(_translate("Settings", "İrsaliye"))
        self.checkBox_2.setText(_translate("Settings", "EK-1"))
        self.checkBox_4.setText(_translate("Settings", "Defter Sorgu"))
        self.checkBox_5.setText(_translate("Settings", "SUBİS Sorgu"))
        self.checkBox_6.setText(_translate("Settings", "Numune Evrağı"))
        self.pushButton_2.setText(_translate("Settings", "Güncelle"))
        self.label_9.setText(_translate("Settings", "Defter Sorgu Sayfası"))
        self.label_11.setText(_translate("Settings", "SUBİS Sorgu Sayfası"))
        self.groupBox_2.setTitle(_translate("Settings", " Sorgu parametreleri - Türleri"))
        self.comboBox.setItemText(0, _translate("Settings", "id"))
        self.comboBox.setItemText(1, _translate("Settings", "class"))
        self.comboBox.setItemText(2, _translate("Settings", "name"))
        self.comboBox.setItemText(3, _translate("Settings", "span"))
        self.comboBox_2.setItemText(0, _translate("Settings", "id"))
        self.comboBox_2.setItemText(1, _translate("Settings", "class"))
        self.comboBox_2.setItemText(2, _translate("Settings", "name"))
        self.comboBox_2.setItemText(3, _translate("Settings", "span"))
        self.comboBox_3.setItemText(0, _translate("Settings", "id"))
        self.comboBox_3.setItemText(1, _translate("Settings", "class"))
        self.comboBox_3.setItemText(2, _translate("Settings", "name"))
        self.comboBox_3.setItemText(3, _translate("Settings", "span"))
        self.comboBox_4.setItemText(0, _translate("Settings", "id"))
        self.comboBox_4.setItemText(1, _translate("Settings", "class"))
        self.comboBox_4.setItemText(2, _translate("Settings", "name"))
        self.comboBox_4.setItemText(3, _translate("Settings", "span"))
        self.comboBox_5.setItemText(0, _translate("Settings", "id"))
        self.comboBox_5.setItemText(1, _translate("Settings", "class"))
        self.comboBox_5.setItemText(2, _translate("Settings", "name"))
        self.comboBox_5.setItemText(3, _translate("Settings", "span"))
        self.comboBox_6.setItemText(0, _translate("Settings", "id"))
        self.comboBox_6.setItemText(1, _translate("Settings", "class"))
        self.comboBox_6.setItemText(2, _translate("Settings", "name"))
        self.comboBox_6.setItemText(3, _translate("Settings", "span"))
        self.comboBox_7.setItemText(0, _translate("Settings", "id"))
        self.comboBox_7.setItemText(1, _translate("Settings", "class"))
        self.comboBox_7.setItemText(2, _translate("Settings", "name"))
        self.comboBox_7.setItemText(3, _translate("Settings", "span"))
        self.comboBox_8.setItemText(0, _translate("Settings", "id"))
        self.comboBox_8.setItemText(1, _translate("Settings", "class"))
        self.comboBox_8.setItemText(2, _translate("Settings", "name"))
        self.comboBox_8.setItemText(3, _translate("Settings", "span"))
        self.comboBox_9.setItemText(0, _translate("Settings", "id"))
        self.comboBox_9.setItemText(1, _translate("Settings", "class"))
        self.comboBox_9.setItemText(2, _translate("Settings", "name"))
        self.comboBox_9.setItemText(3, _translate("Settings", "span"))
        self.comboBox_10.setItemText(0, _translate("Settings", "id"))
        self.comboBox_10.setItemText(1, _translate("Settings", "class"))
        self.comboBox_10.setItemText(2, _translate("Settings", "name"))
        self.comboBox_10.setItemText(3, _translate("Settings", "span"))
        self.pushButton_3.setText(_translate("Settings", "Güncelle"))
        self.label_3.setText(_translate("Settings", "Başlangıç transfer miktarı  (LT/Saat)"))
        self.label_4.setText(_translate("Settings", "Maksimum transfer miktarı  (LT/Saat)"))
        self.label_5.setText(_translate("Settings", "Tank full dolumu transfer miktarı  (LT/Saat)"))
        self.label_6.setText(_translate("Settings", "İrtibat kurulacak VHC kanalı"))
        self.label_7.setText(_translate("Settings", "Terminal veya Barge içi  VHC kanalı"))
        self.pushButton_4.setText(_translate("Settings", "Güncelle"))
        self.label_8.setText(_translate("Settings", " Dağıtıcı Lisansı"))
        self.label_10.setText(_translate("Settings", " Mühür Miktar Sınırı"))
        self.pushButton_5.setText(_translate("Settings", "Güncelle"))
        self.label_12.setText(_translate("Settings", "Gemi Adı"))
        self.label_13.setText(_translate("Settings", "Gemi Cinsi"))
        self.label_14.setText(_translate("Settings", "İMO No / Çağrı  İşareti"))
        self.label_15.setText(_translate("Settings", "Donatan / İşleten"))
        self.label_16.setText(_translate("Settings", "Adres"))
        self.label_17.setText(_translate("Settings", "Tel / Faks"))
        self.label_18.setText(_translate("Settings", "Acentesi"))
        self.label_19.setText(_translate("Settings", "Acente Tel/Faks"))
        self.pushButton_6.setText(_translate("Settings", "Güncelle"))

    def slide(self):
        liste = ["Dosya İşlemleri", "Sorgulama", "EK-2 VHC & Rate Bilgileri", "Dağıtıcı", "EK-1 Gemi Bilgileri"]
        a = self.listWidget.currentItem().text()
        for i in range(len(liste)):
            if liste[i] == a:
                self.stackedWidget.setCurrentIndex(i)
            else:
                pass

    def bul(self):
        sonuc = self.yaz.kolon_oku("deger", "settings")
        # dosya sayfası
        self.lineEdit.setText(sonuc[0][0])
        if sonuc[10][0] == "0":
            self.checkBox.setChecked(False)
            self.irsaliye = "0"
        else:
            self.checkBox.setChecked(True)
            self.irsaliye = "1"
        if sonuc[11][0] == "0":
            self.checkBox_2.setChecked(False)
            self.ek_1 = "0"
        else:
            self.checkBox_2.setChecked(True)
            self.ek_1 = "1"
        if sonuc[12][0] == "0":
            self.checkBox_3.setChecked(False)
            self.kontrol_cizelgesi = "0"
        else:
            self.checkBox_3.setChecked(True)
            self.kontrol_cizelgesi = "1"
        if sonuc[13][0] == "0":
            self.checkBox_4.setChecked(False)
            self.defter = "0"
        else:
            self.checkBox_4.setChecked(True)
            self.defter = "1"
        if sonuc[14][0] == "0":
            self.checkBox_5.setChecked(False)
            self.subis = "0"
        else:
            self.checkBox_5.setChecked(True)
            self.subis = "1"
        if sonuc[15][0] == "0":
            self.checkBox_6.setChecked(False)
            self.numunevrak = "0"
        else:
            self.checkBox_6.setChecked(True)
            self.numunevrak = "1"

        # sorgu sayfası

        self.lineEdit_9.setText(sonuc[8][0])
        self.lineEdit_10.setText(sonuc[16][0])
        defterparametreleri = sonuc[25][0]
        deftersecicileri = sonuc[26][0]
        def_per = defterparametreleri.split("-")
        def_sec = deftersecicileri.split("-")

        subisparametreleri = sonuc[27][0]
        subissecicileri = sonuc[28][0]
        sub_par = subisparametreleri.split("-")
        sub_sec = subissecicileri.split("-")

        self.comboBox.setCurrentIndex(int(def_sec[0]))
        self.comboBox_2.setCurrentIndex(int(def_sec[1]))
        self.comboBox_3.setCurrentIndex(int(def_sec[2]))
        self.comboBox_4.setCurrentIndex(int(def_sec[3]))
        self.comboBox_5.setCurrentIndex(int(def_sec[4]))

        self.lineEdit_2.setText(def_per[0])
        self.lineEdit_19.setText(def_per[1])
        self.lineEdit_20.setText(def_per[2])
        self.lineEdit_21.setText(def_per[3])
        self.lineEdit_30.setText(def_per[4])

        self.comboBox_6.setCurrentIndex(int(sub_sec[0]))
        self.comboBox_7.setCurrentIndex(int(sub_sec[1]))
        self.comboBox_8.setCurrentIndex(int(sub_sec[2]))
        self.comboBox_9.setCurrentIndex(int(sub_sec[3]))
        self.comboBox_10.setCurrentIndex(int(sub_sec[4]))
        self.lineEdit_31.setText(sub_par[0])
        self.lineEdit_32.setText(sub_par[1])
        self.lineEdit_33.setText(sub_par[2])
        self.lineEdit_34.setText(sub_par[3])
        self.lineEdit_35.setText(sub_par[4])


        # rate & Vhc sayfası
        self.lineEdit_3.setText(sonuc[2][0])
        self.lineEdit_4.setText(sonuc[3][0])
        self.lineEdit_5.setText(sonuc[4][0])
        self.lineEdit_6.setText(sonuc[5][0])
        self.lineEdit_7.setText(sonuc[6][0])

        # Dağıtıcı
        self.lineEdit_8.setText(sonuc[7][0])
        self.lineEdit_36.setText(sonuc[9][0])

        # Ek-1 Gemi bilgileri
        self.lineEdit_11.setText(sonuc[17][0])
        self.lineEdit_12.setText(sonuc[18][0])
        self.lineEdit_13.setText(sonuc[19][0])
        self.lineEdit_14.setText(sonuc[20][0])
        self.lineEdit_15.setText(sonuc[21][0])
        self.lineEdit_16.setText(sonuc[22][0])
        self.lineEdit_17.setText(sonuc[23][0])
        self.lineEdit_18.setText(sonuc[24][0])

    def checkbox_irsaliye(self, state):
        if state == QtCore.Qt.Checked:
            self.irsaliye = 1
        else:
            self.irsaliye = 0

    def checkbox_ek_1(self, state):
        if state == QtCore.Qt.Checked:
            self.ek_1 = 1
        else:
            self.ek_1 = 0

    def checkbox_kcizelgesi(self, state):
        if state == QtCore.Qt.Checked:
            self.kontrol_cizelgesi = 1
        else:
            self.kontrol_cizelgesi = 0

    def checkbox_defter(self, state):
        if state == QtCore.Qt.Checked:
            self.defter = 1
        else:
            self.defter = 0

    def checkbox_subis(self, state):
        if state == QtCore.Qt.Checked:
            self.subis = 1
        else:
            self.subis = 0

    def checkbox_numune(self, state):
        if state == QtCore.Qt.Checked:
            self.numunevrak = 1
        else:
            self.numunevrak = 0

    def dosya_kayit_yeri(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory()
        if directory:
            self.lineEdit.clear()
            self.lineEdit.setText(directory)

    # Güncelleme İşlemleri
    def dosya_islemleri_guncelle(self):
        self.yaz.isle("UPDATE settings SET deger='{}' WHERE id = '{}'".format(self.lineEdit.text(), 1))
        c_listesi = []
        c_listesi.append(self.irsaliye)
        c_listesi.append(self.ek_1)
        c_listesi.append(self.kontrol_cizelgesi)
        c_listesi.append(self.defter)
        c_listesi.append(self.subis)
        c_listesi.append(self.numunevrak)
        self.yaz.set_guncelle_coklu(c_listesi, 11)
        mesaj = "Dosyalama ayarları güncellendi"
        mes.uyari(mesaj, "Veritabanı Güncelleme")

    def sorgu_islemleri_guncelle(self):
        self.yaz.isle("UPDATE settings SET deger='{}' WHERE id = '{}'".format(self.lineEdit_9.text(), 9))
        self.yaz.isle("UPDATE settings SET deger='{}' WHERE id = '{}'".format(self.lineEdit_10.text(), 17))
        def_secici = "{}-{}-{}-{}-{}".format(self.comboBox.currentIndex(),
                                             self.comboBox_2.currentIndex(),
                                             self.comboBox_3.currentIndex(),
                                             self.comboBox_4.currentIndex(),
                                             self.comboBox_5.currentIndex())
        def_par = "{}-{}-{}-{}-{}".format(self.lineEdit_2.text(), self.lineEdit_19.text(),
                                          self.lineEdit_20.text(), self.lineEdit_21.text(),
                                          self.lineEdit_30.text())

        subi_secici = "{}-{}-{}-{}-{}".format(self.comboBox_6.currentIndex(),
                                             self.comboBox_7.currentIndex(),
                                             self.comboBox_8.currentIndex(),
                                             self.comboBox_9.currentIndex(),
                                             self.comboBox_10.currentIndex())

        subi_par = "{}-{}-{}-{}-{}".format(self.lineEdit_31.text(), self.lineEdit_32.text(),
                                          self.lineEdit_33.text(), self.lineEdit_34.text(),
                                          self.lineEdit_35.text())

        self.yaz.isle("UPDATE settings SET deger='{}' WHERE id = '{}'".format(def_secici, 27))
        self.yaz.isle("UPDATE settings SET deger='{}' WHERE id = '{}'".format(def_par, 26))
        self.yaz.isle("UPDATE settings SET deger='{}' WHERE id = '{}'".format(subi_secici, 29))
        self.yaz.isle("UPDATE settings SET deger='{}' WHERE id = '{}'".format(subi_par, 28))


        mesaj = "Sorgulama bilgileri güncellendi"
        mes.uyari(mesaj, "Veritabanı Güncelleme")

    def rate_vhc_guncelle(self):
        liste = []
        liste.append(self.lineEdit_3.text())
        liste.append(self.lineEdit_4.text())
        liste.append(self.lineEdit_5.text())
        liste.append(self.lineEdit_6.text())
        liste.append(self.lineEdit_7.text())
        self.yaz.set_guncelle_coklu(liste, 3)
        mesaj = "Rate & VHC bilgileri güncellendi"
        mes.uyari(mesaj, "Veritabanı Güncelleme")

    def lisans_guncelle(self):
        self.yaz.isle("UPDATE settings SET deger='{}' WHERE id = '{}'".format(self.lineEdit_8.text(), 8))
        self.yaz.isle("UPDATE settings SET deger='{}' WHERE id = '{}'".format(self.lineEdit_36.text(), 10))

        mesaj = "Dağıtıcı ayarları güncellendi"
        mes.uyari(mesaj, "Veritabanı Güncelleme")

    def ek_1_gemi_bilgisi_guncelle(self):
        liste = []
        liste.append(self.lineEdit_11.text())
        liste.append(self.lineEdit_12.text())
        liste.append(self.lineEdit_13.text())
        liste.append(self.lineEdit_14.text())
        liste.append(self.lineEdit_15.text())
        liste.append(self.lineEdit_16.text())
        liste.append(self.lineEdit_17.text())
        liste.append(self.lineEdit_18.text())
        self.yaz.set_guncelle_coklu(liste, 18)
        mesaj = "İkmal gemisi bilgileri güncellendi"
        mes.uyari(mesaj, "Veritabanı Güncelleme")


class Ui_FirmaBul(object):
    def __init__(self):
        self.yaz = VbagKur()
        self.firma = ""
        self.kod = 0

    def setupUi(self, FirmaBul):
        FirmaBul.setObjectName("FirmaBul")
        FirmaBul.resize(572, 220)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lib\gui\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FirmaBul.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(FirmaBul)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(FirmaBul)
        self.frame.setMinimumSize(QtCore.QSize(554, 201))
        self.frame.setMaximumSize(QtCore.QSize(554, 201))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(53, 20))
        self.label.setMaximumSize(QtCore.QSize(53, 20))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(428, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(FirmaBul)
        self.lineEdit.textChanged['QString'].connect(self.bul)
        self.listWidget.clicked['QModelIndex'].connect(self.gonder)
        self.pushButton.clicked.connect(FirmaBul.close)
        QtCore.QMetaObject.connectSlotsByName(FirmaBul)

    def retranslateUi(self, FirmaBul):
        _translate = QtCore.QCoreApplication.translate
        FirmaBul.setWindowTitle(_translate("FirmaBul", "Müşteri Bul"))
        self.label.setText(_translate("FirmaBul", "Müşteri Adı"))
        self.pushButton.setText(_translate("FirmaBul", "Seç"))

    def bul(self):
        self.listWidget.clear()
        sonuc = self.yaz.coklu_komut("SELECT ad FROM firmalar WHERE ad LIKE '{}'".format(self.lineEdit.text() + "%"))
        if len(sonuc) == 0:
            self.listWidget.addItem("Sonuç Bulunamadı")
        else:
            for i in range(len(sonuc)):
                self.listWidget.addItem(sonuc[i][0])

    def gonder(self):
        self.firma = self.listWidget.currentItem().text()
        sonuc = self.yaz.komut("SELECT kod FROM firmalar WHERE ad='{}'".format(self.firma))
        self.kod = sonuc[0]
        self.pushButton.setChecked(True)


class Ui_GemiTurleri(object):
    def __init__(self):
        self.yaz = VbagKur()

    def setupUi(self, GemiTurleri):
        GemiTurleri.setObjectName("GemiTurleri")
        GemiTurleri.resize(394, 262)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lib\gui\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GemiTurleri.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(GemiTurleri)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(GemiTurleri)
        self.frame.setMinimumSize(QtCore.QSize(381, 43))
        self.frame.setMaximumSize(QtCore.QSize(381, 43))
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
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(GemiTurleri)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 361, 151))
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 351, 20))
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 1)
        self.bul()

        self.retranslateUi(GemiTurleri)
        self.pushButton.clicked.connect(self.cins_yaz)
        self.listWidget.doubleClicked['QModelIndex'].connect(self.sil)
        QtCore.QMetaObject.connectSlotsByName(GemiTurleri)

    def retranslateUi(self, GemiTurleri):
        _translate = QtCore.QCoreApplication.translate
        GemiTurleri.setWindowTitle(_translate("GemiTurleri", "Gemi Cins Ekle & Sil"))
        self.label.setText(_translate("GemiTurleri", "Gemi Türü"))
        self.pushButton.setText(_translate("GemiTurleri", "Ekle"))
        self.label_2.setText(_translate("GemiTurleri", "Veritabanında Kayıtlı Gemi Türleri(silmek için çift tıklayın)"))

    def bul(self):
        self.listWidget.clear()
        self.yaz = VbagKur()
        sonuc = self.yaz.kolon_oku("tur", "gemitur")
        for i in range(len(sonuc)):
            self.listWidget.addItem(sonuc[i][0])

    def cins_yaz(self):
        ad = self.lineEdit.text()
        if ad =="":
            mesaj = "Lütfen bir gemi türü giriniz !!"
            mes.uyari(mesaj, "Bilgi Giriş Hatası")
        else:
            self.yaz.isle("INSERT INTO gemitur VALUES(NULL, '{}')".format(ad))
            mesaj = ad + " türü veritabanına eklendi"
            mes.uyari(mesaj, "Kayıt Eklendi")
            self.lineEdit.clear()
            self.bul()

    def sil(self):
        if mes.tur_sil(self.listWidget.currentItem().text()) == True:
            conn = self.yaz.komut("SELECT Count(*) FROM gemitur where tur='{}'".format(self.listWidget.currentItem().text()))
            if conn[0] != 0:
                mesaj = """ İlişkilendirilmiş bir gemi türünü silmeye çalışıyorsunuz.Veritabanında bu gemi türü ile ilişkilendirilmiş {} adet kayıt bulundu.Eğer bu kaydı silerseniz, bu kayıt ile bağlantılı gemiler veritabanındaki ilk Gemi Cins kaydına aktarılacak  """.format(conn[0])
                sor = mes.soru("İlişkilendirilmiş Gemi Türü !!", mesaj,
                               "Gemi Türü siliniyor",
                               "Silme İşlemi İptal EDildi")
                if sor == True:
                    self.yaz.kayit_sil("gemitur", "tur", self.listWidget.currentItem().text())
                    self.listWidget.clear()
                    self.bul()
                else:
                    pass
            else:
                self.yaz.kayit_sil("gemitur", "tur", self.listWidget.currentItem().text())
                self.listWidget.clear()
                self.bul()
        else:
            pass


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

    def gui_firma_ara(self):
        Firmaara = QtWidgets.QDialog()
        ui = Ui_FirmaBul()
        ui.setupUi(Firmaara)
        Firmaara.show()
        Firmaara.exec_()
        self.firma_ara_yaz(ui.firma, ui.kod)

    def gui_gemi_tur_olustur(self):
        Turekle = QtWidgets.QDialog()
        ui = Ui_GemiTurleri()
        ui.setupUi(Turekle)
        Turekle.show()
        Turekle.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 586)
        MainWindow.setMinimumSize(QtCore.QSize(458, 586))
        MainWindow.setMaximumSize(QtCore.QSize(458, 586))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lib\gui\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setMaximumSize(QtCore.QSize(440, 527))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_4)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 39, 491, 478))
        self.stackedWidget.setMinimumSize(QtCore.QSize(11, 0))
        self.stackedWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.stackedWidget.setToolTipDuration(-1)
        self.stackedWidget.setLineWidth(1)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setGeometry(QtCore.QRect(0, 0, 441, 497))
        self.frame.setMinimumSize(QtCore.QSize(441, 497))
        self.frame.setMaximumSize(QtCore.QSize(441, 485))
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
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 3)
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 2, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.frame)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout.addWidget(self.comboBox_4, 2, 1, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 1, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 4, 1, 1, 3)
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 5, 1, 1, 3)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 6, 1, 1, 3)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 7, 1, 1, 3)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 8, 1, 1, 3)
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 9, 0, 1, 1)
        self.comboBox_10 = QtWidgets.QComboBox(self.frame)
        self.comboBox_10.setObjectName("comboBox_10")
        self.gridLayout.addWidget(self.comboBox_10, 9, 1, 1, 3)
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 10, 0, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout.addWidget(self.lineEdit_16, 10, 1, 1, 3)
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 11, 0, 1, 1)
        self.comboBox_16 = QtWidgets.QComboBox(self.frame)
        self.comboBox_16.setObjectName("comboBox_16")
        self.gridLayout.addWidget(self.comboBox_16, 11, 1, 1, 3)
        self.label_67 = QtWidgets.QLabel(self.frame)
        self.label_67.setObjectName("label_67")
        self.gridLayout.addWidget(self.label_67, 12, 0, 1, 1)
        self.comboBox_30 = QtWidgets.QComboBox(self.frame)
        self.comboBox_30.setObjectName("comboBox_30")
        self.gridLayout.addWidget(self.comboBox_30, 12, 1, 1, 3)
        self.label_65 = QtWidgets.QLabel(self.frame)
        self.label_65.setObjectName("label_65")
        self.gridLayout.addWidget(self.label_65, 13, 0, 1, 1)
        self.lineEdit_34 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.gridLayout.addWidget(self.lineEdit_34, 13, 1, 1, 3)
        self.label_61 = QtWidgets.QLabel(self.frame)
        self.label_61.setObjectName("label_61")
        self.gridLayout.addWidget(self.label_61, 14, 0, 1, 1)
        self.lineEdit_33 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.gridLayout.addWidget(self.lineEdit_33, 14, 1, 1, 3)
        self.label_62 = QtWidgets.QLabel(self.frame)
        self.label_62.setObjectName("label_62")
        self.gridLayout.addWidget(self.label_62, 15, 0, 1, 1)
        self.lineEdit_35 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.gridLayout.addWidget(self.lineEdit_35, 15, 1, 1, 3)
        self.label_63 = QtWidgets.QLabel(self.frame)
        self.label_63.setObjectName("label_63")
        self.gridLayout.addWidget(self.label_63, 16, 0, 1, 1)
        self.lineEdit_37 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.gridLayout.addWidget(self.lineEdit_37, 16, 1, 1, 3)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 17, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(276, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 17, 0, 1, 3)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.frame_3 = QtWidgets.QFrame(self.page_2)
        self.frame_3.setGeometry(QtCore.QRect(-1, -1, 441, 481))
        self.frame_3.setMinimumSize(QtCore.QSize(441, 481))
        self.frame_3.setMaximumSize(QtCore.QSize(441, 481))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_3.addWidget(self.lineEdit_4, 0, 1, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 0, 3, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_3.addWidget(self.comboBox_3, 1, 1, 1, 4)
        self.label_22 = QtWidgets.QLabel(self.frame_3)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 2, 0, 1, 1)
        self.comboBox_11 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_11.setObjectName("comboBox_11")
        self.gridLayout_3.addWidget(self.comboBox_11, 2, 1, 1, 4)
        self.label_23 = QtWidgets.QLabel(self.frame_3)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 3, 0, 1, 1)
        self.lineEdit_36 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.gridLayout_3.addWidget(self.lineEdit_36, 3, 1, 1, 4)
        self.label_24 = QtWidgets.QLabel(self.frame_3)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 4, 0, 1, 1)
        self.comboBox_13 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_13.setObjectName("comboBox_13")
        self.gridLayout_3.addWidget(self.comboBox_13, 4, 1, 1, 4)
        self.label_69 = QtWidgets.QLabel(self.frame_3)
        self.label_69.setObjectName("label_69")
        self.gridLayout_3.addWidget(self.label_69, 5, 0, 1, 1)
        self.lineEdit_38 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.gridLayout_3.addWidget(self.lineEdit_38, 5, 1, 1, 4)
        self.label_66 = QtWidgets.QLabel(self.frame_3)
        self.label_66.setObjectName("label_66")
        self.gridLayout_3.addWidget(self.label_66, 6, 0, 1, 1)
        self.lineEdit_39 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.gridLayout_3.addWidget(self.lineEdit_39, 6, 1, 1, 4)
        self.label_64 = QtWidgets.QLabel(self.frame_3)
        self.label_64.setObjectName("label_64")
        self.gridLayout_3.addWidget(self.label_64, 7, 0, 1, 1)
        self.lineEdit_40 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.gridLayout_3.addWidget(self.lineEdit_40, 7, 1, 1, 4)
        self.label_68 = QtWidgets.QLabel(self.frame_3)
        self.label_68.setObjectName("label_68")
        self.gridLayout_3.addWidget(self.label_68, 8, 0, 1, 1)
        self.lineEdit_41 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.gridLayout_3.addWidget(self.lineEdit_41, 8, 1, 1, 4)
        self.label_70 = QtWidgets.QLabel(self.frame_3)
        self.label_70.setObjectName("label_70")
        self.gridLayout_3.addWidget(self.label_70, 9, 0, 1, 1)
        self.lineEdit_42 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.gridLayout_3.addWidget(self.lineEdit_42, 9, 1, 1, 4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 270, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 10, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(337, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 11, 0, 1, 2)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 11, 2, 1, 2)
        self.stackedWidget.addWidget(self.page_2)
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        self.frame_2.setGeometry(QtCore.QRect(-40, 0, 551, 33))
        self.frame_2.setMinimumSize(QtCore.QSize(0, 33))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 33))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background-color: rgb(254, 197, 3);\n"
"color: rgb(21, 20, 23);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.radioButton = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton.setGeometry(QtCore.QRect(70, 10, 151, 16))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton.setFont(font)
        self.radioButton.setToolTip("")
        self.radioButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_2.setGeometry(QtCore.QRect(230, 10, 111, 16))
        self.radioButton_2.setMaximumSize(QtCore.QSize(249, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_2.addWidget(self.frame_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 458, 21))
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

        self.actionGemi_Cins_Ekle = QtWidgets.QAction(MainWindow)
        self.actionGemi_Cins_Ekle.setObjectName("actionGemi_Cins_Ekle")


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
        self.menuGemiler.addSeparator()
        self.menuGemiler.addAction(self.actionGemi_Cins_Ekle)
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

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionYeni_M_teri_Ekle.triggered.connect(self.Folustur)
        self.actionM_teri_D_zenle.triggered.connect(self.Fguncelle)
        self.actionM_teri_Sil.triggered.connect(self.Fsil)
        self.actionGemi_Ekle.triggered.connect(self.Gekle)
        self.actionGemi_Bilgii_D_zenle.triggered.connect(self.Gduz)
        self.actionGemi_Sil.triggered.connect(self.Gsil)
        self.actionGemi_Cins_Ekle.triggered.connect(self.gui_gemi_tur_olustur)
        self.actionB_lge_Ekle.triggered.connect(self.gui_bolge_ekle)
        self.actionB_lge_Yer_Sil.triggered.connect(self.gui_bolge_sil)
        self.actionPersonel_Ekle.triggered.connect(self.gui_personel_ekle)
        self.actionPersonel_Sil.triggered.connect(self.gui_personel_sil)
        self.actionYak_t_Ekle.triggered.connect(self.gui_urunekle)
        self.actionYak_t_Sil.triggered.connect(self.gui_urunsil)
        self.actionAyarlar_D_zenle.triggered.connect(self.gui_settings)
        self.actionYard_m.triggered.connect(self.help)
        self.actionHakk_nda.triggered.connect(self.lisans_gui)
        self.radioButton.clicked.connect(self.radio_secim)
        self.radioButton_2.clicked.connect(self.radio_secim_2)
        self.pushButton_2.clicked.connect(self.gui_firma_ara)
        self.pushButton_3.clicked.connect(self.gui_firma_ara)
        self.pushButton_4.clicked.connect(self.tanker_olustur)

        # tetikleme
        self.hazirlik()
        self.triggerfinger()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tux"))
        self.label.setText(_translate("MainWindow", "Müşteri Ünvanı"))
        self.pushButton_2.setText(_translate("MainWindow", "BUL"))
        self.label_3.setText(_translate("MainWindow", "Gemi Adı"))
        self.label_27.setText(_translate("MainWindow", "Yakıt Türü"))
        self.label_4.setText(_translate("MainWindow", "Yoğunluk"))
        self.label_5.setText(_translate("MainWindow", "Sipariş Miktarı"))
        self.label_11.setText(_translate("MainWindow", "Sıcaklık"))
        self.label_8.setText(_translate("MainWindow", "V.C.F  (T54)"))
        self.label_9.setText(_translate("MainWindow", "Litre"))
        self.label_10.setText(_translate("MainWindow", "Kilogram"))
        self.label_21.setText(_translate("MainWindow", "Teslimatçı"))
        self.label_30.setText(_translate("MainWindow", "Yakıt Alan Gemi C/E"))
        self.label_12.setText(_translate("MainWindow", "Barge/Terminal Yetkilisi"))
        self.label_67.setText(_translate("MainWindow", "Bölge"))
        self.label_65.setText(_translate("MainWindow", "Başlama Saati"))
        self.label_61.setText(_translate("MainWindow", "Bitiş Saati"))
        self.label_62.setText(_translate("MainWindow", "Opet Numune Mühür"))
        self.label_63.setText(_translate("MainWindow", "Müşteri Numune Mühür"))
        self.pushButton.setText(_translate("MainWindow", "Oluştur"))
        self.label_2.setText(_translate("MainWindow", "Müşteri Ünvanı"))
        self.pushButton_3.setText(_translate("MainWindow", "BUL"))
        self.label_6.setText(_translate("MainWindow", "Gemi Adı"))
        self.label_22.setText(_translate("MainWindow", "Teslimatçı"))
        self.label_23.setText(_translate("MainWindow", "Teslimat Yapılan Yer"))
        self.label_24.setText(_translate("MainWindow", "Yakıt Türü"))
        self.label_69.setText(_translate("MainWindow", "Yakıt alan Kişi -  C/E"))
        self.label_66.setText(_translate("MainWindow", "Opet Numune Mühür"))
        self.label_64.setText(_translate("MainWindow", "Müşteri Numune Mühür"))
        self.label_68.setText(_translate("MainWindow", "İntertek Num. Mühür"))
        self.label_70.setText(_translate("MainWindow", "Tanker Plaka"))
        self.pushButton_4.setText(_translate("MainWindow", "Oluştur"))
        self.radioButton.setText(_translate("MainWindow", "Barge / Terminal"))
        self.radioButton_2.setText(_translate("MainWindow", "Kara Tankeri"))
        self.menuM_teriler.setTitle(_translate("MainWindow", "Müşteriler"))
        self.menuGemiler.setTitle(_translate("MainWindow", "Gemiler"))
        self.menuB_lgeler.setTitle(_translate("MainWindow", "Bölgeler"))
        self.menuPersonel_Bilgisi.setTitle(_translate("MainWindow", "Personel Bilgisi"))
        self.menuAyarlar.setTitle(_translate("MainWindow", "Ayarlar"))
        self.menuYak_tlar.setTitle(_translate("MainWindow", "Yakıtlar"))
        self.menuTeslimat.setTitle(_translate("MainWindow", "Yardım"))
        self.actionYeni_M_teri_Ekle.setText(_translate("MainWindow", "Yeni Müşteri Ekle"))
        self.actionM_teri_D_zenle.setText(_translate("MainWindow", "Müşteri Düzenle"))
        self.actionM_teri_Sil.setText(_translate("MainWindow", "Müşteri Sil"))
        self.actionGemi_Ekle.setText(_translate("MainWindow", "Gemi Ekle"))
        self.actionGemi_Bilgii_D_zenle.setText(_translate("MainWindow", "Gemi Bilgisi Düzenle"))
        self.actionGemi_Sil.setText(_translate("MainWindow", "Gemi Sil"))
        self.actionGemi_Cins_Ekle.setText(_translate("MainWindow", "Gemi Türleri"))

        self.actionB_lge_Ekle.setText(_translate("MainWindow", "Bölge Ekle"))
        self.actionYer_Ekle.setText(_translate("MainWindow", "Yer Ekle"))
        self.actionB_lge_Yer_Sil.setText(_translate("MainWindow", "Bölge  Sil"))
        self.actionPersonel_Ekle.setText(_translate("MainWindow", "Personel Ekle"))
        self.actionPersonel_Sil.setText(_translate("MainWindow", "Personel Sil"))
        self.actionAyarlar_D_zenle.setText(_translate("MainWindow", "Ayarları Düzenle"))
        self.actionYak_t_Ekle.setText(_translate("MainWindow", "Yakıt Ekle"))
        self.actionYak_t_Sil.setText(_translate("MainWindow", "Yakıt Sil"))
        self.actionYard_m.setText(_translate("MainWindow", "Tux Yardım"))
        self.actionHakk_nda.setText(_translate("MainWindow", "Tux Hakkında"))

    def radio_secim(self):
        if self.radioButton.isChecked():
            self.stackedWidget.setCurrentIndex(0)
        else:
            pass

    def radio_secim_2(self):
        if self.radioButton_2.isChecked():
            self.stackedWidget.setCurrentIndex(1)
        else:
            pass

    def firma_ara_yaz(self, ad, kod):
        if self.radioButton.isChecked():
            self.lineEdit.setText(ad)
            self.tgemi(kod)
        elif self.radioButton_2.isChecked():
            self.lineEdit_4.setText(ad)
            self.tanker_gemi(kod)
        else:
            pass

    def hazirlik(self):
        """ Teslimatçıları listele  """
        self.comboBox_10.addItems(tslmt.personel_hazirla("0"))
        self.comboBox_11.addItems(tslmt.personel_hazirla("0"))

        """ Bölgeleri veritabanından çek """
        self.comboBox_30.addItems(tslmt.bolge_hazirla())

        """ Ürünleri veritabanından çek """
        self.comboBox_4.addItems(tslmt.urun_hazirla())
        self.comboBox_13.addItems(tslmt.urun_hazirla())

        """ Gemi çalışanlarını Hazırla  """
        self.comboBox_16.addItems(tslmt.personel_hazirla("1"))

    def tgemi(self, kod):
        self.comboBox_2.clear()
        self.comboBox_2.addItems(tslmt.gemi_listele(kod))

    def tanker_gemi(self, kod):
        self.comboBox_3.clear()
        self.comboBox_3.addItems(tslmt.gemi_listele(kod))

    def vcf_hesapla(self):
        """
                    Density
                    brüt
                    sıcaklık
                    :return:
                    """
        dnsty = self.lineEdit_2.text().replace(",", ".", 1)
        brut = self.lineEdit_3.text().replace(",", ".", 1)
        try:
            sonuc = tslmt.v_c_f(dnsty, brut, self.lineEdit_8.text())
            self.lineEdit_5.setText(sonuc[0])
            self.lineEdit_6.setText(sonuc[1])
            self.lineEdit_7.setText(sonuc[2])
        except (ValueError):
            self.lineEdit_8.clear()

    def olustur(self):
        """ Artık Veritabanına bilgileri eklemek için değişkenleri almaya başlamamız lazım  """

        musteri_adi = self.lineEdit.text()
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
        if musteri_adi == "":
            mes.giris_kontrol("Müşteri ")
        elif gemi == "":
            mes.giris_kontrol("Gemi")
        elif yogunluk == "":
            mes.giris_kontrol("Yakıt türü")
        elif brut_litre == "":
            mes.giris_kontrol("Brüt Litre")
        elif sicaklik == "":
            mes.giris_kontrol("Sıcaklık")
        elif yakit_alan_kisi == "":
            mes.giris_kontrol("Yakıt Alacak Kişi (C/E)")
        elif baslama_saati == "":
            mes.giris_kontrol("Operasyon başlama saati")
        elif bitis_saati == "":
            mes.giris_kontrol("Operasyon bitiş saati")
        else:
            mesaj = gemi + " gemisine ait " + net_litre + \
                    "  yakıt için teslimat dosyaları oluşturuluyor"
            mes.uyari(mesaj, "Bilgilendirme")

            tslmt.teslimat_hazirliği_yap(musteri_adi, gemi, yakit_turu, yogunluk,
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

    def tanker_olustur(self):
        #Kara tankeri ile yapılan teslimat işlemleri için

        musteri_adi = self.lineEdit_4.text()
        gemi_adi = self.comboBox_3.currentText()
        teslimatci = self.comboBox_11.currentText()
        muhurler = []
        #Mühür Sıralaması
        #OPET
        #Müşteri
        #İntertek

        muhurler.append(self.lineEdit_39.text())
        muhurler.append(self.lineEdit_40.text())
        muhurler.append(self.lineEdit_41.text())
        op_yeri = self.lineEdit_36.text()
        yakit = self.comboBox_13.currentText()
        ce = self.lineEdit_38.text()
        plaka = self.lineEdit_42.text()

        if musteri_adi == "":
            mes.giris_kontrol("Müşteri Adı")
        elif gemi_adi == "":
            mes.giris_kontrol("Gemi Adı")
        else:
            mesaj = gemi_adi + " gemisine ait yakıt için teslimat dosyaları oluşturuluyor"
            mes.uyari(mesaj, "Bilgilendirme")
            tslmt.tanker_teslimat_hazirliği_yap(musteri_adi, gemi_adi, teslimatci, muhurler, yakit, op_yeri, plaka, ce)

        self.lineEdit_39.clear()
        self.lineEdit_40.clear()
        self.lineEdit_41.clear()

    def help(self):
        dizin = os.getcwd()
        os.startfile(dizin + "\lib\help\index.html")

    def triggerfinger(self):
        self.lineEdit_8.textChanged['QString'].connect(self.vcf_hesapla)
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
