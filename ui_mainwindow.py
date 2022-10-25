# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(580, 433)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.Red_spinBox = QSpinBox(self.groupBox)
        self.Red_spinBox.setObjectName(u"Red_spinBox")

        self.gridLayout.addWidget(self.Red_spinBox, 6, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)

        self.DestinoY_spinBox = QSpinBox(self.groupBox)
        self.DestinoY_spinBox.setObjectName(u"DestinoY_spinBox")
        self.DestinoY_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.DestinoY_spinBox, 5, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.label0 = QLabel(self.groupBox)
        self.label0.setObjectName(u"label0")

        self.gridLayout.addWidget(self.label0, 1, 0, 1, 1)

        self.OrigenY_spinBox = QSpinBox(self.groupBox)
        self.OrigenY_spinBox.setObjectName(u"OrigenY_spinBox")
        self.OrigenY_spinBox.setMaximum(999)

        self.gridLayout.addWidget(self.OrigenY_spinBox, 3, 1, 1, 1)

        self.Agregar_final = QPushButton(self.groupBox)
        self.Agregar_final.setObjectName(u"Agregar_final")

        self.gridLayout.addWidget(self.Agregar_final, 10, 0, 1, 2)

        self.DestinoX_spinBox = QSpinBox(self.groupBox)
        self.DestinoX_spinBox.setObjectName(u"DestinoX_spinBox")
        self.DestinoX_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.DestinoX_spinBox, 4, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)

        self.ID_spinBox = QSpinBox(self.groupBox)
        self.ID_spinBox.setObjectName(u"ID_spinBox")
        self.ID_spinBox.setMaximum(999)

        self.gridLayout.addWidget(self.ID_spinBox, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.OrigenX_spinBox = QSpinBox(self.groupBox)
        self.OrigenX_spinBox.setObjectName(u"OrigenX_spinBox")
        self.OrigenX_spinBox.setMaximum(999)

        self.gridLayout.addWidget(self.OrigenX_spinBox, 1, 1, 1, 1)

        self.Mostrar = QPushButton(self.groupBox)
        self.Mostrar.setObjectName(u"Mostrar")

        self.gridLayout.addWidget(self.Mostrar, 11, 0, 1, 2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.Green_spinBox = QSpinBox(self.groupBox)
        self.Green_spinBox.setObjectName(u"Green_spinBox")

        self.gridLayout.addWidget(self.Green_spinBox, 7, 1, 1, 1)

        self.Agregar_Inicio = QPushButton(self.groupBox)
        self.Agregar_Inicio.setObjectName(u"Agregar_Inicio")

        self.gridLayout.addWidget(self.Agregar_Inicio, 9, 0, 1, 2)

        self.Blue_spinBox = QSpinBox(self.groupBox)
        self.Blue_spinBox.setObjectName(u"Blue_spinBox")

        self.gridLayout.addWidget(self.Blue_spinBox, 8, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 1, 1, 1)

        self.Print = QPlainTextEdit(self.centralwidget)
        self.Print.setObjectName(u"Print")

        self.gridLayout_2.addWidget(self.Print, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 580, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino Y", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino X", None))
        self.label0.setText(QCoreApplication.translate("MainWindow", u"Origen X", None))
        self.Agregar_final.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.Mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen Y", None))
        self.Agregar_Inicio.setText(QCoreApplication.translate("MainWindow", u"Agregar al inicio", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

