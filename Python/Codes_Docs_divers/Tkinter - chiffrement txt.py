#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 21:47:54 2020

@author: zakari
"""


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Fenetre(QMainWindow):
    def __init__(self):
        super().__init__()                    # on reprend la structure du td3 globalement
        self.setWindowTitle("TD 4")
        self.resize(600,200)
        self.textEdit = QTextEdit()
        self.textEdit.setPlaceholderText("Entrez le texte")
        self.setCentralWidget(self.textEdit)
        self.messagebox=QMessageBox()
        self.button1=QPushButton('chiffrer')
        self.button1.clicked.connect(self.code4)
        self.button1.setToolTip('coder en ASCII')
        self.mode = QComboBox()
        self.mode.addItems(["ASCII", "Majuscule","Personnalisé"])
        self.mode.currentIndexChanged.connect(self.Choosecode)
        self.layout = QGridLayout()
        self.layout.addWidget(self.button1,1,1)
        self.layout.addWidget(self.textEdit,0,1)
        self.layout.addWidget(self.mode,2,1)


        self.menuFichier = self.menuBar().addMenu("fichier")
        self.action=QAction("Chiffrer", self)
        self.action.setShortcut(QKeySequence("Ctrl+C"))
        self.action.triggered.connect(self.code4)
        self.action.setToolTip('chiffrer le texte en ASCII')
        self.action1=QAction("Déchiffrer", self)
        self.action1.triggered.connect(self.code5)
        self.action1.setShortcut(QKeySequence("Ctrl+D"))
        self.action1.setToolTip('dechiffrer le code en ASCII')
        self.action2= QAction("Sauvegarder le texte", self)
        self.action2.triggered.connect(self.code2)
        self.action2.setShortcut(QKeySequence("Ctrl+S"))
        self.action2.setToolTip('Sauvegarder le texte sur un fichier de votre Mode utilisé')
        self.action3 = QAction("Charger un texte", self)
        self.action3.triggered.connect(self.code3)
        self.action3.setShortcut(QKeySequence("Ctrl+H"))
        self.action3.setToolTip('récupérer un texte sur un fichier de votre Mode utilisé')
        self.menuFichier.addAction(self.action)
        self.menuFichier.addAction(self.action1)
        self.menuFichier.addAction(self.action2)
        self.menuFichier.addAction(self.action3)

        self.menuAide = self.menuBar().addMenu("aide")
        self.action4=QAction("A propos de", self)
        self.action4.triggered.connect(self.apropos)
        self.action4.setToolTip('Obtenir de l\'aide')
        self.menuAide.addAction(self.action4)
        self.action5=QAction("notice", self)
        self.action5.triggered.connect(self.lanote)
        self.action5.setToolTip('Obtenir la notice de l\'application')
        self.menuAide.addAction(self.action5)

        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)
        self.toolbar.addAction(self.action1)
        self.toolbar.addAction(self.action2)
        self.toolbar.addAction(self.action3)
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.textEdit.textChanged.connect(self.composition)
        self.setStatusBar(QStatusBar())

    def code(self,message):
        nouveauMessage=""
        toto=""
        for i in message:
            if i.isdigit()==True:
                toto+=str(i)
                if len(toto)==2:
                    nouveauMessage+=str(chr(int(toto)))
                    toto=""
            else:
                nouveauMessage+=str(i)
        return nouveauMessage



    def code1(self,message):
        nouveauMessage=""
        message=message.upper()
        for cara in message:
            if ord(cara)>99:
                nouveauMessage+=str(cara)
            else:
                nouveauMessage+=str(ord(cara))
        return nouveauMessage


    def code2(self):
        message=self.textEdit.toPlainText()
        fichier = QFile('sauvegarde du texte TD')
        ok = fichier.open(QFile.WriteOnly)
        if ok:
            flux = QTextStream(fichier)
            flux << message
            fichier.close()
        else:
            print('Problème lors de l\'ouverture du fichier de sauvegarde.')

    def code3(self):
         filename=QFileDialog.getOpenFileName()
         file = open(filename[0],'r')
         for ligne in file:
             self.textEdit.setText(ligne)

    def code4(self):
        texte= ""
        if self.mode.currentIndex() == 0:
            texte = self.code1(self.textEdit.toPlainText())
        elif self.mode.currentIndex() == 1:
            texte=self.textEdit.toPlainText()
            texte=texte.upper()

        self.textEdit.setText(texte)
        fichier = QFile('texte td')
        ok = fichier.open(QFile.WriteOnly)
        if ok:
            flux = QTextStream(fichier)
            flux << texte
            fichier.close()
        else:
            print('Problème lors de l\'ouverture du fichier de sauvegarde.')

    def code5(self):
        texte= ""
        if self.mode.currentIndex() == 0:
            texte = self.code(self.textEdit.toPlainText())
        elif self.mode.currentIndex() == 1:
            texte=self.textEdit.toPlainText()
            texte=texte.lower()

        self.textEdit.setText(texte)
        fichier = QFile('texte td')
        ok = fichier.open(QFile.WriteOnly)
        if ok:
            flux = QTextStream(fichier)
            flux << texte
            fichier.close()
        else:
            print('Problème lors de l\'ouverture du fichier de sauvegarde.')

    def apropos(self):
        texteApropos=""
        file = open('A propos de.txt','r')
        for ligne in file:
            texteApropos+=ligne
        self.popup = QMessageBox(QMessageBox.Information,'A propos de',texteApropos)
        self.popup.show()

    def lanote(self):
        note=""
        file = open('Notice.txt','r')
        for ligne in file:
            note+=ligne
        self.popup = QMessageBox(QMessageBox.Information,'Notice',note)
        self.popup.show()


    def Choosecode(self):
        if self.mode.currentIndex() == 2:
            self.ali=QLabel("Choisir votre code:")
            self.layout.addWidget(self.ali,3,1)
            self.curseur = QSlider()
            self.curseur = QSlider(Qt.Horizontal)
            self.curseur.setMinimum(0)
            self.curseur.setMaximum(5)
            self.curseur.sliderMoved.connect(self.position)
            self.layout.addWidget(self.curseur,4,1)

    def position(self,s):
        self.inf=QLabel("vous avez choisi le code "+str(s))
        self.layout.addWidget(self.inf,5,1)

    def composition(self):
        k=0
        texte=self.textEdit.toPlainText()
        for cara in texte:
            if cara==" ":
                k+=0
            else:
                k+=1
        self.setStatusTip("Le texte comporte "+str(k)+" caractères")





app = QCoreApplication.instance()
if app is None:
    app = QApplication(sys.argv)
window = Fenetre()
window.show()
app.exec_()
