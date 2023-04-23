from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
import sys
import os
import submenus_gui


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.main_menu = submenus_gui.Ui_main_menu(app, main_window)
        self.main_menu.show()


if __name__ == "__main__":
    cwd = os.getcwd() + "\\Hexania_app\\"
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = MainWindow(app)
    main_window.show()

    sys.exit(app.exec_())
