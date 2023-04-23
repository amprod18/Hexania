import lib_installer
lib_installer.installer()
import sys
import os
import submenus_gui
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, app, main_window):
        super().__init__(main_window)
        icon = QtGui.QIcon(cwd + "/icon.ico")
        main_window.setWindowIcon(icon)
        main_window.setWindowTitle('Hexania')
        self.main_menu = submenus_gui.Ui_main_menu(app, main_window)
        self.main_menu.show()


if __name__ == "__main__":
    cwd = os.getcwd()
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = MainWindow(app, main_window)
    main_window.show()

    sys.exit(app.exec_())
