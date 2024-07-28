# Créé par Thomas, le 30/05/2024 en Python 3.7

"""
Author    :  Younes Derfoufi
Web site  :  www.tresfacile.net
YouTube   :  https://www.youtube.com/user/InformatiquesFacile
Contact   :  https://www.tresfacile.net/me-contacter/
"""
# You must install the library : PyQtWebEngine
# pip install PyQtWebEngine
import time
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Créer la vue WebEngineView et la définir comme widget central
        self.view = QWebEngineView(self)
        self.setCentralWidget(self.view)

        # Définir la barre de menus
        menu_bar = QMenuBar()

        file_menu = menu_bar.addMenu("Fichier")
        exit_action = QAction("Quitter", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        nav_menu = menu_bar.addMenu("Navigation")
        back_action = QAction("Retour", self)
        back_action.triggered.connect(self.view.back)
        nav_menu.addAction(back_action)

        forward_action = QAction("Avancer", self)
        forward_action.triggered.connect(self.view.forward)
        nav_menu.addAction(forward_action)

        refresh_action = QAction("Actualiser", self)
        refresh_action.triggered.connect(self.view.reload)
        nav_menu.addAction(refresh_action)

        # Définir la barre d'outils
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        back_button = QAction(QIcon.fromTheme("go-previous"), "<- Pécédent", self)
        back_button.triggered.connect(self.view.back)
        toolbar.addAction(back_button)
        forward_button = QAction(QIcon.fromTheme("go-next"), "Suivant ->", self)
        forward_button.triggered.connect(self.view.forward)
        toolbar.addAction(forward_button)

        refresh_button = QAction(QIcon.fromTheme("view-refresh"), "Actualiser F5", self)
        refresh_button.triggered.connect(self.view.reload)
        toolbar.addAction(refresh_button)

        # Définir la barre d'adresse
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate)
        toolbar.addWidget(self.urlbar)

        # Bouton de connexion
        self.btn = QPushButton('OK')
        toolbar.addWidget(self.btn)
        self.btn.clicked.connect(self.navigate)

        # Configurer la fenêtre
        self.setWindowTitle("Mon Navigateur Web")
        self.setWindowIcon(QIcon.fromTheme("web-browser"))
        self.showMaximized()

    def navigate(self):
        url = self.urlbar.text()

        if not url.startswith("http"):
            url = "http://" + url

        self.view.setUrl(QUrl(url))

app = QApplication(sys.argv)
window = MainWindow()
app.exec_()
