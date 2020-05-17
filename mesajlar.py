# -*- coding:utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

def uyari(mesaj, baslik):
    inf = QMessageBox()
    inf.setIcon(QMessageBox.Information)
    inf.setWindowTitle(baslik)
    inf.setText(mesaj)
    inf.setStandardButtons(QMessageBox.Ok)
    inf.exec_()

def soru(baslik, mesaj, ymesaj, nmesaj):
    dens_box = QMessageBox()
    dens_box.setIcon(QMessageBox.Question)
    dens_box.setWindowTitle(baslik)
    dens_box.setText(mesaj)
    dens_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    buttonY = dens_box.button(QMessageBox.Yes)
    buttonY.setText('EVET')
    buttonN = dens_box.button(QMessageBox.No)
    buttonN.setText('HAYIR')
    dens_box.exec_()
    if dens_box.clickedButton() == buttonY:
        uyari(ymesaj, "Bilgilendirme")
        return True
    else:
        uyari(nmesaj, "Bilgilendirme")
        return False

def per_sil(ad):
    dens_box = QMessageBox()
    dens_box.setIcon(QMessageBox.Question)
    dens_box.setWindowTitle('Personel Silinsin mi ?')
    yazi = ad + ' adlı personelin kaydını veritabanından silmek istediğinize emin misiniz ?'
    dens_box.setText(yazi)
    dens_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    buttonY = dens_box.button(QMessageBox.Yes)
    buttonY.setText('Sil')
    buttonN = dens_box.button(QMessageBox.No)
    buttonN.setText('İptal')
    dens_box.exec_()
    if dens_box.clickedButton() == buttonY:
        mesaj = ad + ' adlı personelin kaydı veritabanından başarıyla silinmiştir'
        uyari(mesaj, "Bilgilendirme")
        return True
    else:
        mesaj = ad + ' adlı personelin kayıt silme işlemi iptal edilmiştir'
        uyari(mesaj, "Bilgilendirme")
        return False

def yerbolsil(gemi):
    dens_box = QMessageBox()
    dens_box.setIcon(QMessageBox.Question)
    dens_box.setWindowTitle('Kayıt Silme Uyarısı !!!')
    yazi = gemi + ' bölgesini veritabanından silmek istediğinize emin misiniz ?'
    dens_box.setText(yazi)
    dens_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    buttonY = dens_box.button(QMessageBox.Yes)
    buttonY.setText('EVET')
    buttonN = dens_box.button(QMessageBox.No)
    buttonN.setText('HAYIR')
    dens_box.exec_()
    if dens_box.clickedButton() == buttonY:
        mesaj = " Kayıt Başarı ile silindi"
        uyari(mesaj, "Bilgilendirme")
        return True
    else:
        mesaj =" Kayıt silme işlemi iptal edildi"
        uyari(mesaj, "Bilgilendirme")
        return False

def urun_sil(ad):
    dens_box = QMessageBox()
    dens_box.setIcon(QMessageBox.Question)
    dens_box.setWindowTitle('Ürün Silme Uyarısı ?')
    yazi = ad + ' ürününü veritabanından silmek istediğinize emin misiniz ?'
    dens_box.setText(yazi)
    dens_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    buttonY = dens_box.button(QMessageBox.Yes)
    buttonY.setText('Sil')
    buttonN = dens_box.button(QMessageBox.No)
    buttonN.setText('İptal')
    dens_box.exec_()
    if dens_box.clickedButton() == buttonY:
        mesaj = ad + ' kaydı veritabanından başarıyla silinmiştir'
        uyari(mesaj, "Bilgilendirme")
        return True
    else:
        mesaj = ad + ' kayıt silme işlemi iptal edilmiştir'
        uyari(mesaj, "Bilgilendirme")
        return False
