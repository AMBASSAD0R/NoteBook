# Notebook

# Terms of reference: the User must be able to enter the contact's name and number.
# After adding the data, it should be displayed in the List Widget.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 30, 121, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.phone_number = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.phone_number.setObjectName("phone_number")
        self.verticalLayout.addWidget(self.phone_number)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(170, 30, 211, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.input_name = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.input_name.setObjectName("input_name")
        self.verticalLayout_2.addWidget(self.input_name)
        self.input_number = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.input_number.setObjectName("input_number")
        self.verticalLayout_2.addWidget(self.input_number)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(380, 30, 141, 131))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.contacts_list = QtWidgets.QListWidget(self.centralwidget)
        self.contacts_list.setGeometry(QtCore.QRect(50, 160, 471, 181))
        self.contacts_list.setObjectName("contacts_list")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Записная книжка"))
        self.name.setText(_translate("MainWindow", "Имя"))
        self.phone_number.setText(_translate("MainWindow", "Телефон"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))


class Notebook(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_item)

    def add_item(self):
        self.contacts_list.addItem(f'{self.input_name.text()} {self.input_number.text()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Notebook()
    ex.show()
    sys.exit(app.exec())
