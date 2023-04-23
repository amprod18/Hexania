import lib_installer
lib_installer.installer()
import sys
import os
import submenus_gui
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        icon = QtGui.QIcon(cwd + "icon.ico")
        self.setWindowIcon(icon)
        self.setWindowTitle('Hexania')
        self.main_menu = submenus_gui.Ui_main_menu(app, main_window)
        self.main_menu.show()


if __name__ == "__main__":
    cwd = os.getcwd()
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = MainWindow(app)
    main_window.show()

    sys.exit(app.exec_())
