from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from io import BytesIO
import os
import shapez2


class Ui_main_menu(QtWidgets.QWidget):
    def __init__(self, app, main_window=None):
        global cwd
        super().__init__(main_window)
        cwd = os.getcwd() + "\\Hexania_app\\"
        avaliable = QtWidgets.QDesktopWidget().availableGeometry()
        self.width_, self.height_ = avaliable.right() - avaliable.left(), avaliable.bottom() - avaliable.top()
        self.color = "(100, 100, 100)"
        self.button_color = "(200, 200, 200)"
        self.app = app
        self.setup_main_menu_Ui(main_window)

    def setup_main_menu_Ui(self, main_window):
        main_window.setObjectName("main_window") # type: ignore
        main_window.resize(self.width_, self.height_)
        self.centralwidget = QtWidgets.QWidget(main_window) # type: ignore
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb" + self.color + ";")

        # Set help and exit buttons
        self.help_button = QtWidgets.QPushButton(self.centralwidget)
        self.help_button.setGeometry(QtCore.QRect(60, 900, 130, 50))
        self.help_button.setStyleSheet("background-color: rgb" + self.button_color + "; border-radius: 10px")
        self.help_button.setAutoFillBackground(False)
        self.help_button.setCheckable(False)
        self.help_button.setObjectName("help_button")
        self.help_button.clicked.connect(self.goto_general_help_menu)

        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(60, 960, 130, 50))
        self.exit_button.setStyleSheet("background-color: rgb" + self.button_color + "; border-radius: 10px")
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(self.exit_app) # type: ignore

        # Set circle menu button
        self.circle_button = QtWidgets.QPushButton(self.centralwidget)
        self.circle_button.setGeometry(QtCore.QRect(410, 200, 150, 150))
        self.circle_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(cwd + "images/circle_button1_bad.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) # type: ignore
        self.circle_button.setIcon(icon)
        self.circle_button.setIconSize(QtCore.QSize(150, 150))
        self.circle_button.setObjectName("circle_button")
        self.circle_button.clicked.connect(lambda main_window: self.goto_crl_menu(main_window))

        # Set diamond menu button
        self.diamond_button = QtWidgets.QPushButton(self.centralwidget)
        self.diamond_button.setGeometry(QtCore.QRect(470, 430, 150, 150))
        self.diamond_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(cwd + "images/diamond_button1_bad.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) # type: ignore
        self.diamond_button.setIcon(icon1)
        self.diamond_button.setIconSize(QtCore.QSize(150, 150))
        self.diamond_button.setObjectName("diamond_button")
        self.diamond_button.clicked.connect(self.goto_dmd_menu)

        # Set square menu button
        self.square_button = QtWidgets.QPushButton(self.centralwidget)
        self.square_button.setGeometry(QtCore.QRect(1310, 430, 150, 150))
        self.square_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(cwd + "images/square_button1_bad.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) # type: ignore
        self.square_button.setIcon(icon2)
        self.square_button.setIconSize(QtCore.QSize(150, 150))
        self.square_button.setObjectName("square_button")
        self.square_button.clicked.connect(self.goto_sq_menu)

        # Set rhomboid menu button
        self.rhomboid_button = QtWidgets.QPushButton(self.centralwidget)
        self.rhomboid_button.setGeometry(QtCore.QRect(1140, 610, 150, 150))
        self.rhomboid_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(cwd + "images/rhomboid_button1_bad.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) # type: ignore
        self.rhomboid_button.setIcon(icon3)
        self.rhomboid_button.setIconSize(QtCore.QSize(150, 150))
        self.rhomboid_button.setObjectName("rhomboid_button")
        self.rhomboid_button.clicked.connect(self.goto_rhm_menu)

        # Set regular polygon menu button
        self.regular_polygon_button = QtWidgets.QPushButton(self.centralwidget)
        self.regular_polygon_button.setGeometry(QtCore.QRect(890, 680, 150, 150))
        self.regular_polygon_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(cwd + "images/regular_polygon_button1_bad.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) # type: ignore
        self.regular_polygon_button.setIcon(icon4)
        self.regular_polygon_button.setIconSize(QtCore.QSize(150, 150))
        self.regular_polygon_button.setObjectName("regular_polygon_button")
        self.regular_polygon_button.clicked.connect(self.goto_rp_menu)

        # Set rectangle menu button
        self.rectangle_button = QtWidgets.QPushButton(self.centralwidget)
        self.rectangle_button.setGeometry(QtCore.QRect(640, 610, 150, 150))
        self.rectangle_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(cwd + "images/rectangle_button1_bad.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) # type: ignore
        self.rectangle_button.setIcon(icon5)
        self.rectangle_button.setIconSize(QtCore.QSize(150, 150))
        self.rectangle_button.setObjectName("rectangle_button")
        self.rectangle_button.clicked.connect(self.goto_rct_menu)

        # Set triangle menu button
        self.triangle_button = QtWidgets.QPushButton(self.centralwidget)
        self.triangle_button.setGeometry(QtCore.QRect(1370, 200, 150, 150))
        self.triangle_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(cwd + "images/triangle_button1_bad.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) # type: ignore
        self.triangle_button.setIcon(icon6)
        self.triangle_button.setIconSize(QtCore.QSize(150, 150))
        self.triangle_button.setObjectName("triangle_button")
        self.triangle_button.clicked.connect(self.goto_tgl_menu)

        self.main_menu_button_list = [self.circle_button, self.diamond_button, self.square_button, self.rhomboid_button, self.regular_polygon_button, self.rectangle_button, self.triangle_button]
        
        # Set up the menu buttons
        for i in self.main_menu_button_list:
            i.raise_()
            i.setStyleSheet("border-radius: 10px;")
        self.exit_button.raise_()
        self.help_button.raise_()
        
        # Set up other menu stuff
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.menubar.setStyleSheet("background-color: rgb" + self.color + ";")
        self.statusbar.setStyleSheet("background-color: rgb" + self.color + ";")
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslate_main_menu_Ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_main_menu_Ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "MainWindow"))
        self.help_button.setText(_translate("main_window", "Help"))
        self.exit_button.setText(_translate("main_window", "Exit"))

    def goto_crl_menu(self, main_window):
        self.centralwidget.hide()
        self.crl_ui = Ui_crl_menu(self)
        self.crl_ui.show()
    
    def goto_dmd_menu(self):
        self.centralwidget.hide()
        self.dmd_ui = Ui_dmd_menu(self)
        self.dmd_ui.show()
    
    def goto_rct_menu(self):
        self.centralwidget.hide()
        self.rct_ui = Ui_rct_menu(self)
        self.rct_ui.show()

    def goto_rp_menu(self):
        self.centralwidget.hide()
        self.rp_ui = Ui_rp_menu(self)
        self.rp_ui.show()

    def goto_rhm_menu(self):
        self.centralwidget.hide()
        self.rhm_ui = Ui_rhm_menu(self)
        self.rhm_ui.show()

    def goto_sq_menu(self):
        self.centralwidget.hide()
        self.sq_ui = Ui_sq_menu(self)
        self.sq_ui.show()

    def goto_tgl_menu(self):
        self.centralwidget.hide()
        self.tgl_ui = Ui_tgl_menu(self)
        self.tgl_ui.show()

    def goto_general_help_menu(self):
        self.centralwidget.hide()
        self.ghelp_ui = Ui_ghelp_menu(self)
        self.ghelp_ui.show()
    
    def get_pixmap_from_latex(self, latex):
        fig, ax = plt.subplots(figsize=(1, 1))
        ax.axis('off')
        ax.text(0.5, 0.5, f"${latex}$", fontsize=10, ha='center', va='center')
        buf = BytesIO()
        fig.savefig(buf, format='png', dpi=200, transparent=True)
        buf.seek(0)
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(buf.getvalue())
        return pixmap
    
    def exit_app(self):
        self.app.quit()

class Ui_crl_menu(QtWidgets.QWidget):
    def __init__(self, main_window=None):
        super().__init__(main_window)
        self.main_window = main_window
        self.setup_crl_menu_Ui(main_window)
    
    def setup_crl_menu_Ui(self, crl_menu):
        crl_menu.setObjectName("crl_menu")
        crl_menu.resize(self.parent().width_, self.parent().height_) # type: ignore
        self.centralwidget = QtWidgets.QWidget(crl_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb" + self.parent().color + ";") # type: ignore

        # Set up output grid
        self.crl_output_grid_obj = QtWidgets.QWidget(self.centralwidget)
        self.crl_output_grid_obj.setGeometry(QtCore.QRect(610, 220, 332, 311))
        self.crl_output_grid_obj.setObjectName("crl_output_grid_obj")
        self.crl_output_grid = QtWidgets.QGridLayout(self.crl_output_grid_obj)
        self.crl_output_grid.setContentsMargins(0, 0, 0, 0)
        self.crl_output_grid.setObjectName("crl_output_grid")
        # Radius row
        self.crl_valuetag_radius = QtWidgets.QLabel(self.crl_output_grid_obj)
        self.crl_valuetag_radius.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.crl_valuetag_radius.setObjectName("crl_valuetag_radius")
        self.crl_output_grid.addWidget(self.crl_valuetag_radius, 0, 0, 1, 1)
        self.crl_radius_value = QtWidgets.QLabel(self.crl_output_grid_obj)
        self.crl_radius_value.setObjectName("crl_radius_value")
        self.crl_output_grid.addWidget(self.crl_radius_value, 0, 1, 1, 1)
        self.crl_latextag_radius = QtWidgets.QLabel(self.crl_output_grid_obj)
        self.crl_latextag_radius.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.crl_latextag_radius.setObjectName("crl_latextag_radius")
        self.crl_output_grid.addWidget(self.crl_latextag_radius, 0, 2, 1, 1)
        self.crl_radius_latex = QtWidgets.QLabel(self.crl_output_grid_obj)
        self.crl_radius_latex.setObjectName("crl_radius_latex")
        self.crl_output_grid.addWidget(self.crl_radius_latex, 0, 3, 1, 1)
        # Diameter row
        self.crl_valuetag_diameter = QtWidgets.QLabel(self.crl_output_grid_obj)
        self.crl_valuetag_diameter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.crl_valuetag_diameter.setObjectName("crl_valuetag_diameter")
        self.crl_output_grid.addWidget(self.crl_valuetag_diameter, 1, 0, 1, 1)
        self.crl_diameter_value = QtWidgets.QLabel(self.crl_output_grid_obj)
        self.crl_diameter_value.setObjectName("crl_diameter_value")
        self.crl_output_grid.addWidget(self.crl_diameter_value, 1, 1, 1, 1)
        self.crl_latextag_diameter = QtWidgets.QLabel(self.crl_output_grid_obj)
        self.crl_latextag_diameter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.crl_latextag_diameter.setObjectName("crl_latextag_diameter")
        self.crl_output_grid.addWidget(self.crl_latextag_diameter, 1, 2, 1, 1)
        self.crl_diameter_latex = QtWidgets.QLabel(self.crl_output_grid_obj)
        self.crl_diameter_latex.setObjectName("crl_diameter_latex")
        self.crl_output_grid.addWidget(self.crl_diameter_latex, 1, 3, 1, 1)
        # Perimeter row
        self.crl_valuetag_perimeter = QtWidgets.QLabel(self.crl_output_grid_obj)
        self.crl_valuetag_perimeter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.crl_valuetag_perimeter.setObjectName("crl_valuetag_perimeter")
        self.crl_output_grid.addWidget(self.crl_valuetag_perimeter, 2, 0, 1, 1)
        self.crl_perimeter_value = QtWidgets.QLabel(self.crl_output_grid_obj)
        self.crl_perimeter_value.setObjectName("crl_perimeter_value")
        self.crl_output_grid.addWidget(self.crl_perimeter_value, 2, 1, 1, 1)
        self.crl_latextag_perimeter = QtWidgets.QLabel(self.crl_output_grid_obj)
        self.crl_latextag_perimeter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.crl_latextag_perimeter.setObjectName("crl_latextag_perimeter")
        self.crl_output_grid.addWidget(self.crl_latextag_perimeter, 2, 2, 1, 1)
        self.crl_perimeter_latex = QtWidgets.QLabel(self.crl_output_grid_obj)
        self.crl_perimeter_latex.setObjectName("crl_perimeter_latex")
        self.crl_output_grid.addWidget(self.crl_perimeter_latex, 2, 3, 1, 1)
        # Surface row
        self.crl_valuetag_surface = QtWidgets.QLabel(self.crl_output_grid_obj)
        self.crl_valuetag_surface.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.crl_valuetag_surface.setObjectName("crl_valuetag_surface")
        self.crl_output_grid.addWidget(self.crl_valuetag_surface, 3, 0, 1, 1)
        self.crl_surface_value = QtWidgets.QLabel(self.crl_output_grid_obj)
        self.crl_surface_value.setObjectName("crl_surface_value")
        self.crl_output_grid.addWidget(self.crl_surface_value, 3, 1, 1, 1)
        self.crl_latextag_surface = QtWidgets.QLabel(self.crl_output_grid_obj)
        self.crl_latextag_surface.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.crl_latextag_surface.setObjectName("crl_latextag_surface")
        self.crl_output_grid.addWidget(self.crl_latextag_surface, 3, 2, 1, 1)
        self.crl_surface_latex = QtWidgets.QLabel(self.crl_output_grid_obj)
        self.crl_surface_latex.setObjectName("crl_surface_latex")
        self.crl_output_grid.addWidget(self.crl_surface_latex, 3, 3, 1, 1)

        # Set up entry grid
        self.crl_entry_grid_obj = QtWidgets.QWidget(self.centralwidget)
        self.crl_entry_grid_obj.setGeometry(QtCore.QRect(210, 230, 351, 301))
        self.crl_entry_grid_obj.setObjectName("crl_entry_grid_obj")
        self.crl_entry_grid = QtWidgets.QGridLayout(self.crl_entry_grid_obj)
        self.crl_entry_grid.setContentsMargins(0, 0, 0, 0)
        self.crl_entry_grid.setObjectName("crl_entry_grid")
        # Radius row
        self.crl_radius_label = QtWidgets.QLabel(self.crl_entry_grid_obj)
        self.crl_radius_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.crl_radius_label.setObjectName("crl_radius_label")
        self.crl_entry_grid.addWidget(self.crl_radius_label, 0, 0, 1, 1)
        self.crl_radius_entry = QtWidgets.QLineEdit(self.crl_entry_grid_obj)
        self.crl_radius_entry.setObjectName("crl_radius_entry")
        self.crl_entry_grid.addWidget(self.crl_radius_entry, 0, 1, 1, 1)
        # Diameter row
        self.crl_diameter_label = QtWidgets.QLabel(self.crl_entry_grid_obj)
        self.crl_diameter_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.crl_diameter_label.setObjectName("crl_diameter_label")
        self.crl_entry_grid.addWidget(self.crl_diameter_label, 1, 0, 1, 1)
        self.crl_diameter_entry = QtWidgets.QLineEdit(self.crl_entry_grid_obj)
        self.crl_diameter_entry.setObjectName("crl_diameter_entry")
        self.crl_entry_grid.addWidget(self.crl_diameter_entry, 1, 1, 1, 1)
        # Perimeter row
        self.crl_perimeter_label = QtWidgets.QLabel(self.crl_entry_grid_obj)
        self.crl_perimeter_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.crl_perimeter_label.setObjectName("crl_perimeter_label")
        self.crl_entry_grid.addWidget(self.crl_perimeter_label, 2, 0, 1, 1)
        self.crl_perimeter_entry = QtWidgets.QLineEdit(self.crl_entry_grid_obj)
        self.crl_perimeter_entry.setObjectName("crl_perimeter_entry")
        self.crl_entry_grid.addWidget(self.crl_perimeter_entry, 2, 1, 1, 1)
        # Surface row
        self.crl_surface_label = QtWidgets.QLabel(self.crl_entry_grid_obj)
        self.crl_surface_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.crl_surface_label.setObjectName("crl_surface_label")
        self.crl_entry_grid.addWidget(self.crl_surface_label, 3, 0, 1, 1)
        self.crl_surface_entry = QtWidgets.QLineEdit(self.crl_entry_grid_obj)
        self.crl_surface_entry.setObjectName("crl_surface_entry")
        self.crl_entry_grid.addWidget(self.crl_surface_entry, 3, 1, 1, 1)
        # Decimal row
        self.crl_decimal_label = QtWidgets.QLabel(self.crl_entry_grid_obj)
        self.crl_decimal_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.crl_decimal_label.setObjectName("crl_decimal_label")
        self.crl_entry_grid.addWidget(self.crl_decimal_label, 4, 0, 1, 1)
        self.crl_decimal_entry = QtWidgets.QLineEdit(self.crl_entry_grid_obj)
        self.crl_decimal_entry.setObjectName("crl_decimal_entry")
        self.crl_entry_grid.addWidget(self.crl_decimal_entry, 4, 1, 1, 1)

        # Set up the canvas
        self.canvas_circle = QtWidgets.QGraphicsView(self.centralwidget)
        self.canvas_circle.setGeometry(QtCore.QRect(1150, 150, 500, 500))
        self.canvas_circle.setObjectName("canvas_circle")

        # Set up utility buttons
        self.clean_crl_screen_button = QtWidgets.QPushButton(self.centralwidget)
        self.clean_crl_screen_button.setGeometry(QtCore.QRect(230, 550, 130, 50))
        self.clean_crl_screen_button.setObjectName("clean_crl_screen_button")
        self.clean_crl_screen_button.clicked.connect(self.clean_crl_menu)

        self.draw_circle_button = QtWidgets.QPushButton(self.centralwidget)
        self.draw_circle_button.setGeometry(QtCore.QRect(410, 550, 130, 50))
        self.draw_circle_button.setObjectName("draw_circle_button")
        self.draw_circle_button.clicked.connect(self.draw_circle)

        self.goback_button = QtWidgets.QPushButton(self.centralwidget)
        self.goback_button.setGeometry(QtCore.QRect(410, 630, 130, 50))
        self.goback_button.setObjectName("goback_button")
        self.goback_button.clicked.connect(lambda x: self.goto_main_menu(self.main_window.parent())) # type: ignore

        self.circle_help_button = QtWidgets.QPushButton(self.centralwidget)
        self.circle_help_button.setGeometry(QtCore.QRect(230, 630, 130, 50))
        self.circle_help_button.setObjectName("circle_help_button")
        self.circle_help_button.clicked.connect(self.goto_crl_help_menu)

        self.crl_value_entries = [self.crl_radius_entry, self.crl_diameter_entry, self.crl_perimeter_entry, self.crl_surface_entry, self.crl_decimal_entry]
        self.crl_value_outputs = [self.crl_radius_value, self.crl_diameter_value, self.crl_perimeter_value, self.crl_surface_value]
        self.crl_latex_outputs = [self.crl_radius_latex, self.crl_diameter_latex, self.crl_perimeter_latex, self.crl_surface_latex]
        self.crl_buttons = [self.clean_crl_screen_button, self.draw_circle_button, self.goback_button, self.circle_help_button, self.crl_output_grid_obj, self.crl_entry_grid_obj]

        for i in self.crl_buttons:
            i.setStyleSheet("background-color: rgb" + self.parent().button_color + "; border-radius: 10px;") # type: ignore
        
        for i in self.crl_value_entries:
            i.setStyleSheet("background-color: white;")

        # Set up other menu stuff
        crl_menu.parent().setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(crl_menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        crl_menu.parent().setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(crl_menu)
        self.menubar.setStyleSheet("background-color: rgb" + self.parent().color + ";") # type: ignore
        self.statusbar.setStyleSheet("background-color: rgb" + self.parent().color + ";") # type: ignore
        self.statusbar.setObjectName("statusbar")
        crl_menu.parent().setStatusBar(self.statusbar)

        self.retranslate_crl_menu_Ui(crl_menu)
        QtCore.QMetaObject.connectSlotsByName(crl_menu)

    def retranslate_crl_menu_Ui(self, crl_menu):
        _translate = QtCore.QCoreApplication.translate
        crl_menu.setWindowTitle(_translate("crl_menu", "CircleWindow"))
        self.crl_latextag_perimeter.setText(_translate("crl_menu", "Acquisiton:"))
        self.crl_perimeter_latex.setText(_translate("crl_menu", ""))
        self.crl_valuetag_radius.setText(_translate("crl_menu", "Radius Value:"))
        self.crl_latextag_diameter.setText(_translate("crl_menu", "Acquisiton:"))
        self.crl_surface_value.setText(_translate("crl_menu", ""))
        self.crl_diameter_latex.setText(_translate("crl_menu", ""))
        self.crl_latextag_surface.setText(_translate("crl_menu", "Acquisiton:"))
        self.crl_radius_latex.setText(_translate("crl_menu", ""))
        self.crl_diameter_value.setText(_translate("crl_menu", ""))
        self.crl_latextag_radius.setText(_translate("crl_menu", "Acquisiton:"))
        self.crl_perimeter_value.setText(_translate("crl_menu", ""))
        self.crl_radius_value.setText(_translate("crl_menu", ""))
        self.crl_valuetag_perimeter.setText(_translate("crl_menu", "Perimeter Value:"))
        self.crl_valuetag_surface.setText(_translate("crl_menu", "Surface Value:"))
        self.crl_valuetag_diameter.setText(_translate("crl_menu", "Diameter Value:"))
        self.crl_surface_latex.setText(_translate("crl_menu", ""))
        self.crl_decimal_label.setText(_translate("crl_menu", "Decimal Precision:"))
        self.crl_diameter_label.setText(_translate("crl_menu", "Diameter:"))
        self.crl_perimeter_label.setText(_translate("crl_menu", "Perimeter:"))
        self.crl_surface_label.setText(_translate("crl_menu", "Surface:"))
        self.crl_radius_label.setText(_translate("crl_menu", "Radius:"))
        self.clean_crl_screen_button.setText(_translate("crl_menu", "Clean Screen"))
        self.draw_circle_button.setText(_translate("crl_menu", "Draw Circle"))
        self.goback_button.setText(_translate("crl_menu", "Back to Menu"))
        self.circle_help_button.setText(_translate("crl_menu", "Help"))

    def goto_crl_help_menu(self):
        self.centralwidget.hide()
        # ui.setup_crl_help_menu_Ui(main_menu)
        self.centralwidget.show()
    
    def draw_circle(self):
        radius, diameter, perimeter, surface, decimal = self.get_crl_info() 
        circle = shapez2.Circle(radius=radius, surface=surface, perimeter=perimeter, diameter=diameter, n=int(decimal))
        crl_info, crl_latex = circle.get_parameters()
        self.update_crl_info(crl_info, crl_latex)
        return
    
    def get_crl_info(self):
        crl_info = [i.text() for i in self.crl_value_entries]
        try:
            if crl_info[-1] == "":
                crl_info[-1] = 2 # type: ignore

            for i, v in enumerate(crl_info):
                if v == "":
                    crl_info[i] = None # type: ignore
                else:
                    crl_info[i] = float(v) # type: ignore
            return crl_info
        except TypeError:
            return ("Enter valid number")
    
    def update_crl_info(self, crl_info, crl_latex):
        radius_v, diameter_v, perimeter_v, surface_v, angle_v, length_v, sector_v = crl_info
        crl_info = [radius_v, diameter_v, perimeter_v, surface_v]
        radius_l, diameter_l, perimeter_l, surface_l, angle_l, length_l, sector_l = crl_latex
        crl_latex = [radius_l, diameter_l, perimeter_l, surface_l]

        for i, v in enumerate(self.crl_value_outputs):
            v.setText(str(crl_info[i]))
        for i, v in enumerate(self.crl_latex_outputs):
            v.setPixmap(self.parent().get_pixmap_from_latex(str(crl_latex[i]))) # type: ignore
            v.setScaledContents(True)
    
    def clean_crl_menu(self):
        for i in self.crl_value_outputs:
            i.setText("")
        for i in self.crl_latex_outputs:
            i.setPixmap(QtGui.QPixmap())

    def goto_main_menu(self, main_window):
        self.centralwidget.hide()
        self.parent().setup_main_menu_Ui(main_window) # type: ignore
        self.parent().centralwidget.show() # type: ignore

class Ui_dmd_menu(QtWidgets.QWidget):
    def __init__(self, main_window=None):
        super().__init__(main_window)
        self.main_window = main_window
        self.setup_dmd_menu_Ui(main_window)

    def setup_dmd_menu_Ui(self, dmd_menu):
        dmd_menu.setObjectName("dmd_menu")
        dmd_menu.resize(self.parent().width_, self.parent().height_) # type: ignore
        self.centralwidget = QtWidgets.QWidget(dmd_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb" + self.parent().color + ";") # type: ignore

        # Set up output grid
        self.dmd_output_grid_obj = QtWidgets.QWidget(self.centralwidget)
        self.dmd_output_grid_obj.setGeometry(QtCore.QRect(610, 220, 332, 311))
        self.dmd_output_grid_obj.setObjectName("dmd_output_grid_obj")
        self.dmd_output_grid = QtWidgets.QGridLayout(self.dmd_output_grid_obj)
        self.dmd_output_grid.setContentsMargins(0, 0, 0, 0)
        self.dmd_output_grid.setObjectName("output_grid")
        # side row
        self.dmd_valuetag_side = QtWidgets.QLabel(self.dmd_output_grid_obj)
        self.dmd_valuetag_side.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.dmd_valuetag_side.setObjectName("dmd_valuetag_side")
        self.dmd_output_grid.addWidget(self.dmd_valuetag_side, 0, 0, 1, 1)
        self.dmd_side_value = QtWidgets.QLabel(self.dmd_output_grid_obj)
        self.dmd_side_value.setObjectName("dmd_side_value")
        self.dmd_output_grid.addWidget(self.dmd_side_value, 0, 1, 1, 1)
        self.dmd_latextag_side = QtWidgets.QLabel(self.dmd_output_grid_obj)
        self.dmd_latextag_side.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.dmd_latextag_side.setObjectName("dmd_latextag_side")
        self.dmd_output_grid.addWidget(self.dmd_latextag_side, 0, 2, 1, 1)
        self.dmd_side_latex = QtWidgets.QLabel(self.dmd_output_grid_obj)
        self.dmd_side_latex.setObjectName("dmd_side_latex")
        self.dmd_output_grid.addWidget(self.dmd_side_latex, 0, 3, 1, 1)
        # Diagonal1 row
        self.dmd_valuetag_diagonal1 = QtWidgets.QLabel(self.dmd_output_grid_obj)
        self.dmd_valuetag_diagonal1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.dmd_valuetag_diagonal1.setObjectName("dmd_valuetag_diagonal1")
        self.dmd_output_grid.addWidget(self.dmd_valuetag_diagonal1, 1, 0, 1, 1)
        self.dmd_diagonal1_value = QtWidgets.QLabel(self.dmd_output_grid_obj)
        self.dmd_diagonal1_value.setObjectName("dmd_diagonal1_value")
        self.dmd_output_grid.addWidget(self.dmd_diagonal1_value, 1, 1, 1, 1)
        self.dmd_latextag_diagonal1 = QtWidgets.QLabel(self.dmd_output_grid_obj)
        self.dmd_latextag_diagonal1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.dmd_latextag_diagonal1.setObjectName("dmd_latextag_diagonal1")
        self.dmd_output_grid.addWidget(self.dmd_latextag_diagonal1, 1, 2, 1, 1)
        self.dmd_diagonal1_latex = QtWidgets.QLabel(self.dmd_output_grid_obj)
        self.dmd_diagonal1_latex.setObjectName("dmd_diagonal1_latex")
        self.dmd_output_grid.addWidget(self.dmd_diagonal1_latex, 1, 3, 1, 1)
        # Diagonal2 row
        self.dmd_valuetag_diagonal2 = QtWidgets.QLabel(self.dmd_output_grid_obj)
        self.dmd_valuetag_diagonal2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.dmd_valuetag_diagonal2.setObjectName("dmd_valuetag_diagonal2")
        self.dmd_output_grid.addWidget(self.dmd_valuetag_diagonal2, 2, 0, 1, 1)
        self.dmd_diagonal2_value = QtWidgets.QLabel(self.dmd_output_grid_obj)
        self.dmd_diagonal2_value.setObjectName("dmd_diagonal2_value")
        self.dmd_output_grid.addWidget(self.dmd_diagonal2_value, 2, 1, 1, 1)
        self.dmd_latextag_diagonal2 = QtWidgets.QLabel(self.dmd_output_grid_obj)
        self.dmd_latextag_diagonal2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.dmd_latextag_diagonal2.setObjectName("dmd_latextag_diagonal2")
        self.dmd_output_grid.addWidget(self.dmd_latextag_diagonal2, 2, 2, 1, 1)
        self.dmd_diagonal2_latex = QtWidgets.QLabel(self.dmd_output_grid_obj)
        self.dmd_diagonal2_latex.setObjectName("dmd_diagonal2_latex")
        self.dmd_output_grid.addWidget(self.dmd_diagonal2_latex, 2, 3, 1, 1)
        # Perimeter row
        self.dmd_valuetag_perimeter = QtWidgets.QLabel(self.dmd_output_grid_obj)
        self.dmd_valuetag_perimeter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.dmd_valuetag_perimeter.setObjectName("dmd_valuetag_perimeter")
        self.dmd_output_grid.addWidget(self.dmd_valuetag_perimeter, 3, 0, 1, 1)
        self.dmd_perimeter_value = QtWidgets.QLabel(self.dmd_output_grid_obj)
        self.dmd_perimeter_value.setObjectName("dmd_perimeter_value")
        self.dmd_output_grid.addWidget(self.dmd_perimeter_value, 3, 1, 1, 1)
        self.dmd_latextag_perimeter = QtWidgets.QLabel(self.dmd_output_grid_obj)
        self.dmd_latextag_perimeter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.dmd_latextag_perimeter.setObjectName("dmd_latextag_perimeter")
        self.dmd_output_grid.addWidget(self.dmd_latextag_perimeter, 3, 2, 1, 1)
        self.dmd_perimeter_latex = QtWidgets.QLabel(self.dmd_output_grid_obj)
        self.dmd_perimeter_latex.setObjectName("dmd_perimeter_latex")
        self.dmd_output_grid.addWidget(self.dmd_perimeter_latex, 3, 3, 1, 1)
        # Surface row
        self.dmd_valuetag_surface = QtWidgets.QLabel(self.dmd_output_grid_obj)
        self.dmd_valuetag_surface.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.dmd_valuetag_surface.setObjectName("dmd_valuetag_surface")
        self.dmd_output_grid.addWidget(self.dmd_valuetag_surface, 4, 0, 1, 1)
        self.dmd_surface_value = QtWidgets.QLabel(self.dmd_output_grid_obj)
        self.dmd_surface_value.setObjectName("dmd_surface_value")
        self.dmd_output_grid.addWidget(self.dmd_surface_value, 4, 1, 1, 1)
        self.dmd_latextag_surface = QtWidgets.QLabel(self.dmd_output_grid_obj)
        self.dmd_latextag_surface.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.dmd_latextag_surface.setObjectName("dmd_latextag_surface")
        self.dmd_output_grid.addWidget(self.dmd_latextag_surface, 4, 2, 1, 1)
        self.dmd_surface_latex = QtWidgets.QLabel(self.dmd_output_grid_obj)
        self.dmd_surface_latex.setObjectName("dmd_surface_latex")
        self.dmd_output_grid.addWidget(self.dmd_surface_latex, 4, 3, 1, 1)

        # Set up entry grid
        self.dmd_entry_grid_obj = QtWidgets.QWidget(self.centralwidget)
        self.dmd_entry_grid_obj.setGeometry(QtCore.QRect(210, 230, 351, 301))
        self.dmd_entry_grid_obj.setObjectName("dmd_entry_grid_obj")
        self.dmd_entry_grid = QtWidgets.QGridLayout(self.dmd_entry_grid_obj)
        self.dmd_entry_grid.setContentsMargins(0, 0, 0, 0)
        self.dmd_entry_grid.setObjectName("entry_grid")
        # Side row
        self.dmd_side_label = QtWidgets.QLabel(self.dmd_entry_grid_obj)
        self.dmd_side_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.dmd_side_label.setObjectName("dmd_side_label")
        self.dmd_entry_grid.addWidget(self.dmd_side_label, 0, 0, 1, 1)
        self.dmd_side_entry = QtWidgets.QLineEdit(self.dmd_entry_grid_obj)
        self.dmd_side_entry.setObjectName("dmd_side_entry")
        self.dmd_entry_grid.addWidget(self.dmd_side_entry, 0, 1, 1, 1)
        # Diagonal1 row
        self.dmd_diagonal1_label = QtWidgets.QLabel(self.dmd_entry_grid_obj)
        self.dmd_diagonal1_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.dmd_diagonal1_label.setObjectName("dmd_diagonal1_label")
        self.dmd_entry_grid.addWidget(self.dmd_diagonal1_label, 1, 0, 1, 1)
        self.dmd_diagonal1_entry = QtWidgets.QLineEdit(self.dmd_entry_grid_obj)
        self.dmd_diagonal1_entry.setObjectName("dmd_diagonal1_entry")
        self.dmd_entry_grid.addWidget(self.dmd_diagonal1_entry, 1, 1, 1, 1)
        # Diagonal2 row
        self.dmd_diagonal2_label = QtWidgets.QLabel(self.dmd_entry_grid_obj)
        self.dmd_diagonal2_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.dmd_diagonal2_label.setObjectName("dmd_diagonal2_label")
        self.dmd_entry_grid.addWidget(self.dmd_diagonal2_label, 2, 0, 1, 1)
        self.dmd_diagonal2_entry = QtWidgets.QLineEdit(self.dmd_entry_grid_obj)
        self.dmd_diagonal2_entry.setObjectName("dmd_diagonal2_entry")
        self.dmd_entry_grid.addWidget(self.dmd_diagonal2_entry, 2, 1, 1, 1)
        # Perimeter row
        self.dmd_perimeter_label = QtWidgets.QLabel(self.dmd_entry_grid_obj)
        self.dmd_perimeter_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.dmd_perimeter_label.setObjectName("dmd_perimeter_label")
        self.dmd_entry_grid.addWidget(self.dmd_perimeter_label, 3, 0, 1, 1)
        self.dmd_perimeter_entry = QtWidgets.QLineEdit(self.dmd_entry_grid_obj)
        self.dmd_perimeter_entry.setObjectName("dmd_perimeter_entry")
        self.dmd_entry_grid.addWidget(self.dmd_perimeter_entry, 3, 1, 1, 1)
        # Surface row
        self.dmd_surface_label = QtWidgets.QLabel(self.dmd_entry_grid_obj)
        self.dmd_surface_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.dmd_surface_label.setObjectName("dmd_surface_label")
        self.dmd_entry_grid.addWidget(self.dmd_surface_label, 4, 0, 1, 1)
        self.dmd_surface_entry = QtWidgets.QLineEdit(self.dmd_entry_grid_obj)
        self.dmd_surface_entry.setObjectName("dmd_surface_entry")
        self.dmd_entry_grid.addWidget(self.dmd_surface_entry, 4, 1, 1, 1)
        # Decimal row
        self.dmd_decimal_label = QtWidgets.QLabel(self.dmd_entry_grid_obj)
        self.dmd_decimal_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.dmd_decimal_label.setObjectName("dmd_decimal_label")
        self.dmd_entry_grid.addWidget(self.dmd_decimal_label, 5, 0, 1, 1)
        self.dmd_decimal_entry = QtWidgets.QLineEdit(self.dmd_entry_grid_obj)
        self.dmd_decimal_entry.setObjectName("dmd_decimal_entry")
        self.dmd_entry_grid.addWidget(self.dmd_decimal_entry, 5, 1, 1, 1)

        # Set up the canvas
        self.canvas_diamond = QtWidgets.QGraphicsView(self.centralwidget)
        self.canvas_diamond.setGeometry(QtCore.QRect(1150, 150, 500, 500))
        self.canvas_diamond.setObjectName("canvas_diamond")

        # Set up utility buttons
        self.clean_dmd_screen_button = QtWidgets.QPushButton(self.centralwidget)
        self.clean_dmd_screen_button.setGeometry(QtCore.QRect(230, 550, 130, 50))
        self.clean_dmd_screen_button.setObjectName("clean_dmd_screen_button")
        self.clean_dmd_screen_button.clicked.connect(self.clean_dmd_menu)

        self.draw_diamond_button = QtWidgets.QPushButton(self.centralwidget)
        self.draw_diamond_button.setGeometry(QtCore.QRect(410, 550, 130, 50))
        self.draw_diamond_button.setObjectName("draw_diamond_button")
        self.draw_diamond_button.clicked.connect(self.draw_diamond)

        self.goback_button = QtWidgets.QPushButton(self.centralwidget)
        self.goback_button.setGeometry(QtCore.QRect(410, 630, 130, 50))
        self.goback_button.setObjectName("goback_button")
        self.goback_button.clicked.connect(lambda x: self.goto_main_menu(self.main_window.parent())) # type: ignore

        self.diamond_help_button = QtWidgets.QPushButton(self.centralwidget)
        self.diamond_help_button.setGeometry(QtCore.QRect(230, 630, 130, 50))
        self.diamond_help_button.setObjectName("diamond_help_button")
        self.diamond_help_button.clicked.connect(self.goto_dmd_help_menu)

        self.dmd_value_entries = [self.dmd_side_entry, self.dmd_diagonal1_entry, self.dmd_diagonal2_entry, self.dmd_perimeter_entry, self.dmd_surface_entry, self.dmd_decimal_entry]
        self.dmd_value_outputs = [self.dmd_side_value, self.dmd_diagonal1_value, self.dmd_diagonal2_value, self.dmd_perimeter_value, self.dmd_surface_value]
        self.dmd_latex_outputs = [self.dmd_side_latex, self.dmd_diagonal1_latex, self.dmd_diagonal2_latex, self.dmd_perimeter_latex, self.dmd_surface_latex]
        self.dmd_buttons = [self.clean_dmd_screen_button, self.draw_diamond_button, self.goback_button, self.diamond_help_button, self.dmd_output_grid_obj, self.dmd_entry_grid_obj]

        for i in self.dmd_buttons:
            i.setStyleSheet("background-color: rgb" + self.parent().button_color + "; border-radius: 10px;") # type: ignore
        
        for i in self.dmd_value_entries:
            i.setStyleSheet("background-color: white;")

        # Sey up other menu stuff
        dmd_menu.parent().setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(dmd_menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        dmd_menu.parent().setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(dmd_menu)
        self.menubar.setStyleSheet("background-color: rgb" + self.parent().color + ";") # type: ignore
        self.statusbar.setStyleSheet("background-color: rgb" + self.parent().color + ";") # type: ignore
        self.statusbar.setObjectName("statusbar")
        dmd_menu.parent().setStatusBar(self.statusbar)

        self.retranslate_dmd_menu_Ui(dmd_menu)
        QtCore.QMetaObject.connectSlotsByName(dmd_menu)

    def retranslate_dmd_menu_Ui(self, dmd_menu):
        _translate = QtCore.QCoreApplication.translate
        dmd_menu.setWindowTitle(_translate("dmd_menu", "MainWindow"))
        self.dmd_diagonal2_latex.setText(_translate("dmd_menu", "Latex"))
        self.dmd_valuetag_perimeter.setText(_translate("dmd_menu", "Perimeter Value:"))
        self.dmd_diagonal2_value.setText(_translate("dmd_menu", "TextLabel"))
        self.dmd_latextag_perimeter.setText(_translate("dmd_menu", "Acquisiton:"))
        self.dmd_side_latex.setText(_translate("dmd_menu", "Latex"))
        self.dmd_surface_value.setText(_translate("dmd_menu", "TextLabel"))
        self.dmd_perimeter_value.setText(_translate("dmd_menu", "TextLabel"))
        self.dmd_latextag_side.setText(_translate("dmd_menu", "Acquisiton:"))
        self.dmd_perimeter_latex.setText(_translate("dmd_menu", "Latex"))
        self.dmd_valuetag_side.setText(_translate("dmd_menu", "Side Value:"))
        self.dmd_side_value.setText(_translate("dmd_menu", "TextLabel"))
        self.dmd_valuetag_surface.setText(_translate("dmd_menu", "Surface Value:"))
        self.dmd_valuetag_diagonal2.setText(_translate("dmd_menu", "Diagonal 2 Value:"))
        self.dmd_latextag_diagonal2.setText(_translate("dmd_menu", "Acquisiton:"))
        self.dmd_latextag_surface.setText(_translate("dmd_menu", "Acquisiton:"))
        self.dmd_surface_latex.setText(_translate("dmd_menu", "Latex"))
        self.dmd_valuetag_diagonal1.setText(_translate("dmd_menu", "Diagonal 1 Value:"))
        self.dmd_diagonal1_value.setText(_translate("dmd_menu", "TextLabel"))
        self.dmd_latextag_diagonal1.setText(_translate("dmd_menu", "Acquisiton:"))
        self.dmd_diagonal1_latex.setText(_translate("dmd_menu", "Latex"))
        self.dmd_perimeter_label.setText(_translate("dmd_menu", "Perimeter:"))
        self.dmd_surface_label.setText(_translate("dmd_menu", "Surface:"))
        self.dmd_decimal_label.setText(_translate("dmd_menu", "Decimal Precision:"))
        self.dmd_diagonal2_label.setText(_translate("dmd_menu", "Diagonal 2:"))
        self.dmd_side_label.setText(_translate("dmd_menu", "Side:"))
        self.dmd_diagonal1_label.setText(_translate("dmd_menu", "Diagonal 1:"))
        self.clean_dmd_screen_button.setText(_translate("dmd_menu", "Clean Screen"))
        self.draw_diamond_button.setText(_translate("dmd_menu", "Draw Diamond"))
        self.goback_button.setText(_translate("dmd_menu", "Back to Menu"))
        self.diamond_help_button.setText(_translate("dmd_menu", "Help"))

    def goto_dmd_help_menu(self):
        self.centralwidget.hide()
        # ui.setup_dmd_help_menu_Ui(main_menu)
        self.centralwidget.show()
    
    def draw_diamond(self):
        side, diagonal1, diagonal2, perimeter, surface, decimal = self.get_dmd_info() 
        diamond = shapez2.Diamond(side=side, surface=surface, perimeter=perimeter, diagonal1=diagonal1, diagonal2=diagonal2, n=int(decimal))
        dmd_info, dmd_latex = diamond.get_parameters()
        self.update_dmd_info(dmd_info, dmd_latex)
        return
    
    def get_dmd_info(self):
        dmd_info = [i.text() for i in self.dmd_value_entries]
        try:
            if dmd_info[-1] == "":
                dmd_info[-1] = 2 # type: ignore

            for i, v in enumerate(dmd_info):
                if v == "":
                    dmd_info[i] = None # type: ignore
                else:
                    dmd_info[i] = float(v) # type: ignore
            return dmd_info
        except TypeError:
            return ("Enter valid number")
    
    def update_dmd_info(self, dmd_info, dmd_latex):
        for i, v in enumerate(self.dmd_value_outputs):
            v.setText(str(dmd_info[i]))
        for i, v in enumerate(self.dmd_latex_outputs):
            v.setPixmap(self.parent().get_pixmap_from_latex(str(dmd_latex[i]))) # type: ignore
            v.setScaledContents(True)
    
    def clean_dmd_menu(self):
        for i in self.dmd_value_outputs:
            i.setText("")
        for i in self.dmd_latex_outputs:
            i.setPixmap(QtGui.QPixmap())

    def goto_main_menu(self, main_window):
        self.centralwidget.hide()
        self.parent().setup_main_menu_Ui(main_window) # type: ignore
        self.parent().centralwidget.show() # type: ignore

class Ui_rct_menu(QtWidgets.QWidget):
    def __init__(self, main_window=None):
        super().__init__(main_window)
        self.main_window = main_window
        self.setup_rct_menu_Ui(main_window)

    def setup_rct_menu_Ui(self, rct_menu):
        rct_menu.setObjectName("rct_menu")
        rct_menu.resize(self.parent().width_, self.parent().height_) # type: ignore
        self.centralwidget = QtWidgets.QWidget(rct_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb" + self.parent().color + ";") # type: ignore

        # Set up output grid
        self.rct_output_grid_obj = QtWidgets.QWidget(self.centralwidget)
        self.rct_output_grid_obj.setGeometry(QtCore.QRect(610, 220, 332, 311))
        self.rct_output_grid_obj.setObjectName("gridLayoutWidget_2")
        self.rct_output_grid = QtWidgets.QGridLayout(self.rct_output_grid_obj)
        self.rct_output_grid.setContentsMargins(0, 0, 0, 0)
        self.rct_output_grid.setObjectName("output_grid")
        # Length row
        self.rct_valuetag_length = QtWidgets.QLabel(self.rct_output_grid_obj)
        self.rct_valuetag_length.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rct_valuetag_length.setObjectName("rct_valuetag_length")
        self.rct_output_grid.addWidget(self.rct_valuetag_length, 0, 0, 1, 1)
        self.rct_length_value = QtWidgets.QLabel(self.rct_output_grid_obj)
        self.rct_length_value.setObjectName("rct_length_value")
        self.rct_output_grid.addWidget(self.rct_length_value, 0, 1, 1, 1)
        self.rct_latextag_length = QtWidgets.QLabel(self.rct_output_grid_obj)
        self.rct_latextag_length.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rct_latextag_length.setObjectName("rct_latextag_length")
        self.rct_output_grid.addWidget(self.rct_latextag_length, 0, 2, 1, 1)
        self.rct_length_latex = QtWidgets.QLabel(self.rct_output_grid_obj)
        self.rct_length_latex.setObjectName("rct_length_latex")
        self.rct_output_grid.addWidget(self.rct_length_latex, 0, 3, 1, 1)
        # Height row
        self.rct_valuetag_height = QtWidgets.QLabel(self.rct_output_grid_obj)
        self.rct_valuetag_height.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rct_valuetag_height.setObjectName("rct_valuetag_height")
        self.rct_output_grid.addWidget(self.rct_valuetag_height, 1, 0, 1, 1)
        self.rct_height_value = QtWidgets.QLabel(self.rct_output_grid_obj)
        self.rct_height_value.setObjectName("rct_height_value")
        self.rct_output_grid.addWidget(self.rct_height_value, 1, 1, 1, 1)
        self.rct_latextag_height = QtWidgets.QLabel(self.rct_output_grid_obj)
        self.rct_latextag_height.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rct_latextag_height.setObjectName("rct_latextag_height")
        self.rct_output_grid.addWidget(self.rct_latextag_height, 1, 2, 1, 1)
        self.rct_height_latex = QtWidgets.QLabel(self.rct_output_grid_obj)
        self.rct_height_latex.setObjectName("rct_height_latex")
        self.rct_output_grid.addWidget(self.rct_height_latex, 1, 3, 1, 1)
        # Diagonal row
        self.rct_valuetag_diagonal = QtWidgets.QLabel(self.rct_output_grid_obj)
        self.rct_valuetag_diagonal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rct_valuetag_diagonal.setObjectName("rct_valuetag_diagonal")
        self.rct_output_grid.addWidget(self.rct_valuetag_diagonal, 2, 0, 1, 1)
        self.rct_diagonal_value = QtWidgets.QLabel(self.rct_output_grid_obj)
        self.rct_diagonal_value.setObjectName("rct_diagonal_value")
        self.rct_output_grid.addWidget(self.rct_diagonal_value, 2, 1, 1, 1)
        self.rct_latextag_diagonal = QtWidgets.QLabel(self.rct_output_grid_obj)
        self.rct_latextag_diagonal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rct_latextag_diagonal.setObjectName("rct_latextag_diagonal")
        self.rct_output_grid.addWidget(self.rct_latextag_diagonal, 2, 2, 1, 1)
        self.rct_diagonal_latex = QtWidgets.QLabel(self.rct_output_grid_obj)
        self.rct_diagonal_latex.setObjectName("rct_diagonal_latex")
        self.rct_output_grid.addWidget(self.rct_diagonal_latex, 2, 3, 1, 1)
        # Perimeter row
        self.rct_valuetag_perimeter = QtWidgets.QLabel(self.rct_output_grid_obj)
        self.rct_valuetag_perimeter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rct_valuetag_perimeter.setObjectName("rct_valuetag_perimeter")
        self.rct_output_grid.addWidget(self.rct_valuetag_perimeter, 3, 0, 1, 1)
        self.rct_perimeter_value = QtWidgets.QLabel(self.rct_output_grid_obj)
        self.rct_perimeter_value.setObjectName("rct_perimeter_value")
        self.rct_output_grid.addWidget(self.rct_perimeter_value, 3, 1, 1, 1)
        self.rct_latextag_perimeter = QtWidgets.QLabel(self.rct_output_grid_obj)
        self.rct_latextag_perimeter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rct_latextag_perimeter.setObjectName("rct_latextag_perimeter")
        self.rct_output_grid.addWidget(self.rct_latextag_perimeter, 3, 2, 1, 1)
        self.rct_perimeter_latex = QtWidgets.QLabel(self.rct_output_grid_obj)
        self.rct_perimeter_latex.setObjectName("rct_perimeter_latex")
        self.rct_output_grid.addWidget(self.rct_perimeter_latex, 3, 3, 1, 1)
        # Surface row
        self.rct_valuetag_surface = QtWidgets.QLabel(self.rct_output_grid_obj)
        self.rct_valuetag_surface.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rct_valuetag_surface.setObjectName("rct_valuetag_surface")
        self.rct_output_grid.addWidget(self.rct_valuetag_surface, 4, 0, 1, 1)
        self.rct_surface_value = QtWidgets.QLabel(self.rct_output_grid_obj)
        self.rct_surface_value.setObjectName("rct_surface_value")
        self.rct_output_grid.addWidget(self.rct_surface_value, 4, 1, 1, 1)
        self.rct_latextag_surface = QtWidgets.QLabel(self.rct_output_grid_obj)
        self.rct_latextag_surface.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rct_latextag_surface.setObjectName("rct_latextag_surface")
        self.rct_output_grid.addWidget(self.rct_latextag_surface, 4, 2, 1, 1)
        self.rct_surface_latex = QtWidgets.QLabel(self.rct_output_grid_obj)
        self.rct_surface_latex.setObjectName("rct_surface_latex")
        self.rct_output_grid.addWidget(self.rct_surface_latex, 4, 3, 1, 1)

        # Set up entry grid
        self.rct_entry_grid_obj = QtWidgets.QWidget(self.centralwidget)
        self.rct_entry_grid_obj.setGeometry(QtCore.QRect(210, 230, 351, 301))
        self.rct_entry_grid_obj.setObjectName("gridLayoutWidget_3")
        self.rct_entry_grid = QtWidgets.QGridLayout(self.rct_entry_grid_obj)
        self.rct_entry_grid.setContentsMargins(0, 0, 0, 0)
        self.rct_entry_grid.setObjectName("entry_grid")
        # Length row
        self.rct_length_label = QtWidgets.QLabel(self.rct_entry_grid_obj)
        self.rct_length_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rct_length_label.setObjectName("rct_length_label")
        self.rct_entry_grid.addWidget(self.rct_length_label, 0, 0, 1, 1)
        self.rct_length_entry = QtWidgets.QLineEdit(self.rct_entry_grid_obj)
        self.rct_length_entry.setObjectName("rct_length_entry")
        self.rct_entry_grid.addWidget(self.rct_length_entry, 0, 1, 1, 1)
        # Height row
        self.rct_height_label = QtWidgets.QLabel(self.rct_entry_grid_obj)
        self.rct_height_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rct_height_label.setObjectName("rct_height_label")
        self.rct_entry_grid.addWidget(self.rct_height_label, 1, 0, 1, 1)
        self.rct_height_entry = QtWidgets.QLineEdit(self.rct_entry_grid_obj)
        self.rct_height_entry.setObjectName("rct_height_entry")
        self.rct_entry_grid.addWidget(self.rct_height_entry, 1, 1, 1, 1)
        # Diagonal row
        self.rct_diagonal_label = QtWidgets.QLabel(self.rct_entry_grid_obj)
        self.rct_diagonal_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rct_diagonal_label.setObjectName("rct_diagonal_label")
        self.rct_entry_grid.addWidget(self.rct_diagonal_label, 2, 0, 1, 1)
        self.rct_diagonal_entry = QtWidgets.QLineEdit(self.rct_entry_grid_obj)
        self.rct_diagonal_entry.setObjectName("rct_diagonal_entry")
        self.rct_entry_grid.addWidget(self.rct_diagonal_entry, 2, 1, 1, 1)
        # Perimeter row
        self.rct_perimeter_label = QtWidgets.QLabel(self.rct_entry_grid_obj)
        self.rct_perimeter_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rct_perimeter_label.setObjectName("rct_perimeter_label")
        self.rct_entry_grid.addWidget(self.rct_perimeter_label, 3, 0, 1, 1)
        self.rct_perimeter_entry = QtWidgets.QLineEdit(self.rct_entry_grid_obj)
        self.rct_perimeter_entry.setObjectName("rct_perimeter_entry")
        self.rct_entry_grid.addWidget(self.rct_perimeter_entry, 3, 1, 1, 1)
        # Surface row
        self.rct_surface_label = QtWidgets.QLabel(self.rct_entry_grid_obj)
        self.rct_surface_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rct_surface_label.setObjectName("rct_surface_label")
        self.rct_entry_grid.addWidget(self.rct_surface_label, 4, 0, 1, 1)
        self.rct_surface_entry = QtWidgets.QLineEdit(self.rct_entry_grid_obj)
        self.rct_surface_entry.setObjectName("rct_surface_entry")
        self.rct_entry_grid.addWidget(self.rct_surface_entry, 4, 1, 1, 1)
        # Decimal row
        self.rct_decimal_label = QtWidgets.QLabel(self.rct_entry_grid_obj)
        self.rct_decimal_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rct_decimal_label.setObjectName("rct_decimal_label")
        self.rct_entry_grid.addWidget(self.rct_decimal_label, 5, 0, 1, 1)
        self.rct_decimal_entry = QtWidgets.QLineEdit(self.rct_entry_grid_obj)
        self.rct_decimal_entry.setObjectName("rct_decimal_entry")
        self.rct_entry_grid.addWidget(self.rct_decimal_entry, 5, 1, 1, 1)
        
        # Set up the canvas
        self.canvas_rectangle = QtWidgets.QGraphicsView(self.centralwidget)
        self.canvas_rectangle.setGeometry(QtCore.QRect(1150, 150, 500, 500))
        self.canvas_rectangle.setObjectName("canvas_rectangle")

        # Set up utility buttons
        self.clean_rct_screen_button = QtWidgets.QPushButton(self.centralwidget)
        self.clean_rct_screen_button.setGeometry(QtCore.QRect(230, 550, 130, 50))
        self.clean_rct_screen_button.setObjectName("clean_rct_screen_button")
        self.clean_rct_screen_button.clicked.connect(self.clean_rct_menu)

        self.draw_rectangle_button = QtWidgets.QPushButton(self.centralwidget)
        self.draw_rectangle_button.setGeometry(QtCore.QRect(410, 550, 130, 50))
        self.draw_rectangle_button.setObjectName("draw_rectangle_button")
        self.draw_rectangle_button.clicked.connect(self.draw_rectangle)

        self.goback_button = QtWidgets.QPushButton(self.centralwidget)
        self.goback_button.setGeometry(QtCore.QRect(410, 630, 130, 50))
        self.goback_button.setObjectName("goback_button")
        self.goback_button.clicked.connect(lambda x: self.goto_main_menu(self.main_window.parent())) # type: ignore

        self.rectangle_help_button = QtWidgets.QPushButton(self.centralwidget)
        self.rectangle_help_button.setGeometry(QtCore.QRect(230, 630, 130, 50))
        self.rectangle_help_button.setObjectName("rectangle_help_button")
        self.rectangle_help_button.clicked.connect(lambda x: self.goto_rct_help_menu(self.main_window.parent())) # type: ignore

        self.rct_value_entries = [self.rct_length_entry, self.rct_height_entry, self.rct_diagonal_entry, self.rct_perimeter_entry, self.rct_surface_entry, self.rct_decimal_entry]
        self.rct_value_outputs = [self.rct_length_value, self.rct_height_value, self.rct_diagonal_value, self.rct_perimeter_value, self.rct_surface_value]
        self.rct_latex_outputs = [self.rct_length_latex, self.rct_height_latex, self.rct_diagonal_latex, self.rct_perimeter_latex, self.rct_surface_latex]
        self.rct_buttons = [self.clean_rct_screen_button, self.draw_rectangle_button, self.goback_button, self.rectangle_help_button, self.rct_output_grid_obj, self.rct_entry_grid_obj]

        for i in self.rct_buttons:
            i.setStyleSheet("background-color: rgb" + self.parent().button_color + "; border-radius: 10px;") # type: ignore
        
        for i in self.rct_value_entries:
            i.setStyleSheet("background-color: white;")

        # Set up other menu stuff
        rct_menu.parent().setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(rct_menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        rct_menu.parent().setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(rct_menu)
        self.menubar.setStyleSheet("background-color: rgb" + self.parent().color + ";") # type: ignore
        self.statusbar.setStyleSheet("background-color: rgb" + self.parent().color + ";") # type: ignore
        self.statusbar.setObjectName("statusbar")
        rct_menu.parent().setStatusBar(self.statusbar)

        self.retranslate_rct_menu_Ui(rct_menu)
        QtCore.QMetaObject.connectSlotsByName(rct_menu)

    def retranslate_rct_menu_Ui(self, rct_menu):
        _translate = QtCore.QCoreApplication.translate
        rct_menu.setWindowTitle(_translate("sq_menu", "MainWindow"))
        self.rct_diagonal_latex.setText(_translate("sq_menu", "Latex"))
        self.rct_valuetag_perimeter.setText(_translate("sq_menu", "Perimeter Value:"))
        self.rct_diagonal_value.setText(_translate("sq_menu", "TextLabel"))
        self.rct_latextag_perimeter.setText(_translate("sq_menu", "Acquisiton:"))
        self.rct_length_latex.setText(_translate("sq_menu", "Latex"))
        self.rct_surface_value.setText(_translate("sq_menu", "TextLabel"))
        self.rct_perimeter_value.setText(_translate("sq_menu", "TextLabel"))
        self.rct_latextag_length.setText(_translate("sq_menu", "Acquisiton:"))
        self.rct_perimeter_latex.setText(_translate("sq_menu", "Latex"))
        self.rct_valuetag_length.setText(_translate("sq_menu", "Length Value:"))
        self.rct_length_value.setText(_translate("sq_menu", "TextLabel"))
        self.rct_valuetag_surface.setText(_translate("sq_menu", "Surface Value:"))
        self.rct_valuetag_diagonal.setText(_translate("sq_menu", "Diagonal Value:"))
        self.rct_latextag_diagonal.setText(_translate("sq_menu", "Acquisiton:"))
        self.rct_latextag_surface.setText(_translate("sq_menu", "Acquisiton:"))
        self.rct_surface_latex.setText(_translate("sq_menu", "Latex"))
        self.rct_valuetag_height.setText(_translate("sq_menu", "Height Value:"))
        self.rct_height_value.setText(_translate("sq_menu", "TextLabel"))
        self.rct_latextag_height.setText(_translate("sq_menu", "Acquisiton:"))
        self.rct_height_latex.setText(_translate("sq_menu", "Latex"))
        self.rct_perimeter_label.setText(_translate("sq_menu", "Perimeter:"))
        self.rct_surface_label.setText(_translate("sq_menu", "Surface:"))
        self.rct_decimal_label.setText(_translate("sq_menu", "Decimal Precision:"))
        self.rct_diagonal_label.setText(_translate("sq_menu", "Diagonal:"))
        self.rct_length_label.setText(_translate("sq_menu", "Length:"))
        self.rct_height_label.setText(_translate("sq_menu", "Height:"))
        self.clean_rct_screen_button.setText(_translate("sq_menu", "Clean Screen"))
        self.draw_rectangle_button.setText(_translate("sq_menu", "Draw Rectangle"))
        self.goback_button.setText(_translate("sq_menu", "Back to Menu"))
        self.rectangle_help_button.setText(_translate("sq_menu", "Help"))
    
    def goto_rct_help_menu(self):
        self.centralwidget.hide()
        # ui.setup_rct_help_menu_Ui(main_menu)
        self.centralwidget.show()
    
    def draw_rectangle(self):
        length, height, diagonal, perimeter, surface, decimal = self.get_rct_info() 
        rectangle = shapez2.Rectangle(length=length, surface=surface, perimeter=perimeter, diagonal=diagonal, height=height, n=int(decimal))
        rct_info, rct_latex = rectangle.get_parameters()
        self.update_rct_info(rct_info, rct_latex)
        return
    
    def get_rct_info(self):
        rct_info = [i.text() for i in self.rct_value_entries]
        try:
            if rct_info[-1] == "":
                rct_info[-1] = 2 # type: ignore

            for i, v in enumerate(rct_info):
                if v == "":
                    rct_info[i] = None # type: ignore
                else:
                    rct_info[i] = float(v) # type: ignore
            return rct_info
        except TypeError:
            return ("Enter valid number")
    
    def update_rct_info(self, rct_info, rct_latex):
        for i, v in enumerate(self.rct_value_outputs):
            v.setText(str(rct_info[i]))
        for i, v in enumerate(self.rct_latex_outputs):
            v.setPixmap(self.parent().get_pixmap_from_latex(str(rct_latex[i]))) # type: ignore
            v.setScaledContents(True)
    
    def clean_rct_menu(self):
        for i in self.rct_value_outputs:
            i.setText("")
        for i in self.rct_latex_outputs:
            i.setPixmap(QtGui.QPixmap())

    def goto_main_menu(self, main_window):
        self.centralwidget.hide()
        self.parent().setup_main_menu_Ui(main_window) # type: ignore
        self.parent().centralwidget.show() # type: ignore

class Ui_rp_menu(QtWidgets.QWidget):
    def __init__(self, main_window=None):
        super().__init__(main_window)
        self.main_window = main_window
        self.setup_rp_menu_Ui(main_window)

    def setup_rp_menu_Ui(self, rp_menu):
        rp_menu.setObjectName("rp_menu")
        rp_menu.resize(self.parent().width_, self.parent().height_) # type: ignore
        self.centralwidget = QtWidgets.QWidget(rp_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb" + self.parent().color + ";") # type: ignore

        # Set up output grid
        self.rp_output_grid_obj = QtWidgets.QWidget(self.centralwidget)
        self.rp_output_grid_obj.setGeometry(QtCore.QRect(610, 220, 332, 311))
        self.rp_output_grid_obj.setObjectName("rp_output_grid_obj")
        self.rp_output_grid = QtWidgets.QGridLayout(self.rp_output_grid_obj)
        self.rp_output_grid.setContentsMargins(0, 0, 0, 0)
        self.rp_output_grid.setObjectName("rp_output_grid")
        # Pifactor row
        self.rp_valuetag_pifactor = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_valuetag_pifactor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rp_valuetag_pifactor.setObjectName("rp_valuetag_pifactor")
        self.rp_output_grid.addWidget(self.rp_valuetag_pifactor, 0, 0, 1, 1)
        self.rp_pifactor_value = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_pifactor_value.setObjectName("rp_pifactor_value")
        self.rp_output_grid.addWidget(self.rp_pifactor_value, 0, 1, 1, 1)
        self.rp_latextag_pifactor = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_latextag_pifactor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rp_latextag_pifactor.setObjectName("rp_latextag_pifactor")
        self.rp_output_grid.addWidget(self.rp_latextag_pifactor, 0, 2, 1, 1)
        self.rp_pifactor_latex = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_pifactor_latex.setObjectName("rp_pifactor_latex")
        self.rp_output_grid.addWidget(self.rp_pifactor_latex, 0, 3, 1, 1)
        # Side row
        self.rp_valuetag_side = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_valuetag_side.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rp_valuetag_side.setObjectName("rp_valuetag_side")
        self.rp_output_grid.addWidget(self.rp_valuetag_side, 1, 0, 1, 1)
        self.rp_side_value = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_side_value.setObjectName("rp_side_value")
        self.rp_output_grid.addWidget(self.rp_side_value, 1, 1, 1, 1)
        self.rp_latextag_side = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_latextag_side.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rp_latextag_side.setObjectName("rp_latextag_side")
        self.rp_output_grid.addWidget(self.rp_latextag_side, 1, 2, 1, 1)
        self.rp_side_latex = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_side_latex.setObjectName("rp_side_latex")
        self.rp_output_grid.addWidget(self.rp_side_latex, 1, 3, 1, 1)
        # Radius row
        self.rp_valuetag_radius = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_valuetag_radius.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rp_valuetag_radius.setObjectName("rp_valuetag_radius")
        self.rp_output_grid.addWidget(self.rp_valuetag_radius, 2, 0, 1, 1)
        self.rp_radius_value = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_radius_value.setObjectName("rp_radius_value")
        self.rp_output_grid.addWidget(self.rp_radius_value, 2, 1, 1, 1)
        self.rp_latextag_radius = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_latextag_radius.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rp_latextag_radius.setObjectName("rp_latextag_radius")
        self.rp_output_grid.addWidget(self.rp_latextag_radius, 2, 2, 1, 1)
        self.rp_radius_latex = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_radius_latex.setObjectName("rp_radius_latex")
        self.rp_output_grid.addWidget(self.rp_radius_latex, 2, 3, 1, 1)
        # Apothem row
        self.rp_valuetag_apothem = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_valuetag_apothem.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rp_valuetag_apothem.setObjectName("rp_valuetag_apothem")
        self.rp_output_grid.addWidget(self.rp_valuetag_apothem, 3, 0, 1, 1)
        self.rp_apothem_value = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_apothem_value.setObjectName("rp_apothem_value")
        self.rp_output_grid.addWidget(self.rp_apothem_value, 3, 1, 1, 1)
        self.rp_latextag_apothem = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_latextag_apothem.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rp_latextag_apothem.setObjectName("rp_latextag_apothem")
        self.rp_output_grid.addWidget(self.rp_latextag_apothem, 3, 2, 1, 1)
        self.rp_apothem_latex = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_apothem_latex.setObjectName("rp_apothem_latex")
        self.rp_output_grid.addWidget(self.rp_apothem_latex, 3, 3, 1, 1)
        # Perimeter row
        self.rp_valuetag_perimeter = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_valuetag_perimeter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rp_valuetag_perimeter.setObjectName("rp_valuetag_perimeter")
        self.rp_output_grid.addWidget(self.rp_valuetag_perimeter, 4, 0, 1, 1)
        self.rp_perimeter_value = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_perimeter_value.setObjectName("rp_perimeter_value")
        self.rp_output_grid.addWidget(self.rp_perimeter_value, 4, 1, 1, 1)
        self.rp_latextag_perimeter = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_latextag_perimeter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rp_latextag_perimeter.setObjectName("rp_latextag_perimeter")
        self.rp_output_grid.addWidget(self.rp_latextag_perimeter, 4, 2, 1, 1)
        self.rp_perimeter_latex = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_perimeter_latex.setObjectName("rp_perimeter_latex")
        self.rp_output_grid.addWidget(self.rp_perimeter_latex, 4, 3, 1, 1)
        # Surface row
        self.rp_valuetag_surface = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_valuetag_surface.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rp_valuetag_surface.setObjectName("rp_valuetag_surface")
        self.rp_output_grid.addWidget(self.rp_valuetag_surface, 5, 0, 1, 1)
        self.rp_surface_value = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_surface_value.setObjectName("rp_surface_value")
        self.rp_output_grid.addWidget(self.rp_surface_value, 5, 1, 1, 1)
        self.rp_latextag_surface = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_latextag_surface.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rp_latextag_surface.setObjectName("rp_latextag_surface")
        self.rp_output_grid.addWidget(self.rp_latextag_surface, 5, 2, 1, 1)
        self.rp_surface_latex = QtWidgets.QLabel(self.rp_output_grid_obj)
        self.rp_surface_latex.setObjectName("rp_surface_latex")
        self.rp_output_grid.addWidget(self.rp_surface_latex, 5, 3, 1, 1)

        # Set up entry grid
        self.rp_entry_grid_obj = QtWidgets.QWidget(self.centralwidget)
        self.rp_entry_grid_obj.setGeometry(QtCore.QRect(210, 230, 351, 301))
        self.rp_entry_grid_obj.setObjectName("rp_entry_grid_obj")
        self.rp_entry_grid = QtWidgets.QGridLayout(self.rp_entry_grid_obj)
        self.rp_entry_grid.setContentsMargins(0, 0, 0, 0)
        self.rp_entry_grid.setObjectName("rp_entry_grid")
        # Number of sides row
        self.rp_nsides_label = QtWidgets.QLabel(self.rp_entry_grid_obj)
        self.rp_nsides_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rp_nsides_label.setObjectName("rp_nsides_label")
        self.rp_entry_grid.addWidget(self.rp_nsides_label, 0, 0, 1, 1)
        self.rp_nsides_entry = QtWidgets.QLineEdit(self.rp_entry_grid_obj)
        self.rp_nsides_entry.setObjectName("rp_nsides_entry")
        self.rp_entry_grid.addWidget(self.rp_nsides_entry, 0, 1, 1, 1)
        # Side row
        self.rp_side_label = QtWidgets.QLabel(self.rp_entry_grid_obj)
        self.rp_side_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rp_side_label.setObjectName("rp_side_label")
        self.rp_entry_grid.addWidget(self.rp_side_label, 1, 0, 1, 1)
        self.rp_side_entry = QtWidgets.QLineEdit(self.rp_entry_grid_obj)
        self.rp_side_entry.setObjectName("rp_side_entry")
        self.rp_entry_grid.addWidget(self.rp_side_entry, 1, 1, 1, 1)
        # Radius row
        self.rp_radius_label = QtWidgets.QLabel(self.rp_entry_grid_obj)
        self.rp_radius_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rp_radius_label.setObjectName("rp_radius_label")
        self.rp_entry_grid.addWidget(self.rp_radius_label, 2, 0, 1, 1)
        self.rp_radius_entry = QtWidgets.QLineEdit(self.rp_entry_grid_obj)
        self.rp_radius_entry.setObjectName("rp_radius_entry")
        self.rp_entry_grid.addWidget(self.rp_radius_entry, 2, 1, 1, 1)
        # Apothem row
        self.rp_apothem_label = QtWidgets.QLabel(self.rp_entry_grid_obj)
        self.rp_apothem_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rp_apothem_label.setObjectName("rp_apothem_label")
        self.rp_entry_grid.addWidget(self.rp_apothem_label, 3, 0, 1, 1)
        self.rp_apothem_entry = QtWidgets.QLineEdit(self.rp_entry_grid_obj)
        self.rp_apothem_entry.setObjectName("rp_apothem_entry")
        self.rp_entry_grid.addWidget(self.rp_apothem_entry, 3, 1, 1, 1)
        # Perimeter row
        self.rp_perimeter_label = QtWidgets.QLabel(self.rp_entry_grid_obj)
        self.rp_perimeter_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rp_perimeter_label.setObjectName("rp_perimeter_label")
        self.rp_entry_grid.addWidget(self.rp_perimeter_label, 4, 0, 1, 1)
        self.rp_perimeter_entry = QtWidgets.QLineEdit(self.rp_entry_grid_obj)
        self.rp_perimeter_entry.setObjectName("rp_perimeter_entry")
        self.rp_entry_grid.addWidget(self.rp_perimeter_entry, 4, 1, 1, 1)
        # Surface row
        self.rp_surface_label = QtWidgets.QLabel(self.rp_entry_grid_obj)
        self.rp_surface_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rp_surface_label.setObjectName("rp_surface_label")
        self.rp_entry_grid.addWidget(self.rp_surface_label, 5, 0, 1, 1)
        self.rp_surface_entry = QtWidgets.QLineEdit(self.rp_entry_grid_obj)
        self.rp_surface_entry.setObjectName("rp_surface_entry")
        self.rp_entry_grid.addWidget(self.rp_surface_entry, 5, 1, 1, 1)
        # Decimal row
        self.rp_decimal_label = QtWidgets.QLabel(self.rp_entry_grid_obj)
        self.rp_decimal_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rp_decimal_label.setObjectName("rp_decimal_label")
        self.rp_entry_grid.addWidget(self.rp_decimal_label, 6, 0, 1, 1)
        self.rp_decimal_entry = QtWidgets.QLineEdit(self.rp_entry_grid_obj)
        self.rp_decimal_entry.setObjectName("rp_decimal_entry")
        self.rp_entry_grid.addWidget(self.rp_decimal_entry, 6, 1, 1, 1)

        # Set up the canvas
        self.canvas_regular_polygon = QtWidgets.QGraphicsView(self.centralwidget)
        self.canvas_regular_polygon.setGeometry(QtCore.QRect(1150, 150, 500, 500))
        self.canvas_regular_polygon.setObjectName("canvas_regular_polygon")

        # Set up utility buttons
        self.clean_rp_screen_button = QtWidgets.QPushButton(self.centralwidget)
        self.clean_rp_screen_button.setGeometry(QtCore.QRect(230, 550, 130, 50))
        self.clean_rp_screen_button.setObjectName("clean_rp_screen_button")
        self.clean_rp_screen_button.clicked.connect(self.clean_rp_menu)

        self.draw_regular_polygon_button = QtWidgets.QPushButton(self.centralwidget)
        self.draw_regular_polygon_button.setGeometry(QtCore.QRect(410, 550, 130, 50))
        self.draw_regular_polygon_button.setObjectName("draw_regular_polygon_button")
        self.draw_regular_polygon_button.clicked.connect(self.draw_regular_polygon)

        self.goback_button = QtWidgets.QPushButton(self.centralwidget)
        self.goback_button.setGeometry(QtCore.QRect(410, 630, 130, 50))
        self.goback_button.setObjectName("goback_button")
        self.goback_button.clicked.connect(lambda x: self.goto_main_menu(self.main_window.parent())) # type: ignore

        self.regular_polygon_help_button = QtWidgets.QPushButton(self.centralwidget)
        self.regular_polygon_help_button.setGeometry(QtCore.QRect(230, 630, 130, 50))
        self.regular_polygon_help_button.setObjectName("regular_polygon_help_button")
        self.regular_polygon_help_button.clicked.connect(self.goto_rp_help_menu)

        self.rp_value_entries = [self.rp_side_entry, self.rp_radius_entry, self.rp_apothem_entry, self.rp_perimeter_entry, self.rp_surface_entry, self.rp_nsides_entry, self.rp_decimal_entry]
        self.rp_value_outputs = [self.rp_pifactor_value, self.rp_side_value, self.rp_radius_value, self.rp_apothem_value, self.rp_perimeter_value, self.rp_surface_value]
        self.rp_latex_outputs = [self.rp_pifactor_latex, self.rp_side_latex, self.rp_radius_latex, self.rp_apothem_latex, self.rp_perimeter_latex, self.rp_surface_latex]
        self.rp_buttons = [self.clean_rp_screen_button, self.draw_regular_polygon_button, self.goback_button, self.regular_polygon_help_button, self.rp_output_grid_obj, self.rp_entry_grid_obj]

        for i in self.rp_buttons:
            i.setStyleSheet("background-color: rgb" + self.parent().button_color + "; border-radius: 10px;") # type: ignore

        for i in self.rp_value_entries:
            i.setStyleSheet("background-color: white;")

        # Set up other menu stuff
        rp_menu.parent().setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(rp_menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        rp_menu.parent().setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(rp_menu)
        self.menubar.setStyleSheet("background-color: rgb" + self.parent().color + ";") # type: ignore
        self.statusbar.setStyleSheet("background-color: rgb" + self.parent().color + ";") # type: ignore
        self.statusbar.setObjectName("statusbar")
        rp_menu.parent().setStatusBar(self.statusbar)

        self.retranslate_rp_menu_Ui(rp_menu)
        QtCore.QMetaObject.connectSlotsByName(rp_menu)

    def retranslate_rp_menu_Ui(self, rp_menu):
        _translate = QtCore.QCoreApplication.translate
        rp_menu.setWindowTitle(_translate("rp_menu", "MainWindow"))
        self.rp_latextag_radius.setText(_translate("rp_menu", "Acquisiton:"))
        self.rp_radius_value.setText(_translate("rp_menu", "TextLabel"))
        self.rp_latextag_perimeter.setText(_translate("rp_menu", "Acquisiton:"))
        self.rp_perimeter_latex.setText(_translate("rp_menu", "Latex"))
        self.rp_surface_latex.setText(_translate("rp_menu", "Latex"))
        self.rp_side_value.setText(_translate("rp_menu", "TextLabel"))
        self.rp_apothem_latex.setText(_translate("rp_menu", "Latex"))
        self.rp_side_latex.setText(_translate("rp_menu", "Latex"))
        self.rp_latextag_side.setText(_translate("rp_menu", "Acquisiton:"))
        self.rp_latextag_surface.setText(_translate("rp_menu", "Acquisiton:"))
        self.rp_latextag_apothem.setText(_translate("rp_menu", "Acquisiton:"))
        self.rp_valuetag_side.setText(_translate("rp_menu", "Side Value:"))
        self.rp_apothem_value.setText(_translate("rp_menu", "TextLabel"))
        self.rp_valuetag_radius.setText(_translate("rp_menu", "Radius Value:"))
        self.rp_valuetag_apothem.setText(_translate("rp_menu", "Apothem Value:"))
        self.rp_surface_value.setText(_translate("rp_menu", "TextLabel"))
        self.rp_radius_latex.setText(_translate("rp_menu", "Latex"))
        self.rp_valuetag_perimeter.setText(_translate("rp_menu", "Perimeter Value:"))
        self.rp_perimeter_value.setText(_translate("rp_menu", "TextLabel"))
        self.rp_valuetag_surface.setText(_translate("rp_menu", "Surface Value:"))
        self.rp_valuetag_pifactor.setText(_translate("rp_menu", "Correction Factor:"))
        self.rp_pifactor_value.setText(_translate("rp_menu", "TextLabel"))
        self.rp_latextag_pifactor.setText(_translate("rp_menu", "Acquisiton:"))
        self.rp_pifactor_latex.setText(_translate("rp_menu", "Latex"))
        self.rp_radius_label.setText(_translate("rp_menu", "Radius:"))
        self.rp_side_label.setText(_translate("rp_menu", "Side:"))
        self.rp_surface_label.setText(_translate("rp_menu", "Surface:"))
        self.rp_apothem_label.setText(_translate("rp_menu", "Apothem:"))
        self.rp_decimal_label.setText(_translate("rp_menu", "Decimal Precision:"))
        self.rp_perimeter_label.setText(_translate("rp_menu", "Perimeter:"))
        self.rp_nsides_label.setText(_translate("rp_menu", "Number of Sides:"))
        self.clean_rp_screen_button.setText(_translate("rp_menu", "Clean Screen"))
        self.draw_regular_polygon_button.setText(_translate("rp_menu", "Draw Regular Polygon"))
        self.goback_button.setText(_translate("rp_menu", "Back to Menu"))
        self.regular_polygon_help_button.setText(_translate("rp_menu", "Help"))

    def goto_rp_help_menu(self):
        self.centralwidget.hide()
        # ui.setup_rp_help_menu_Ui(main_menu)
        self.centralwidget.show()
    
    def draw_regular_polygon(self):
        side, radius, apothem, perimeter, surface, n_sides, decimal = self.get_rp_info() 
        regular_polygon = shapez2.RegularPolygon(side=side, radius=radius, apothem=apothem, surface=surface, perimeter=perimeter, n_sides=int(n_sides), n=int(decimal)) # type: ignore
        rp_info, rp_latex = regular_polygon.get_parameters()
        self.update_rp_info(rp_info, rp_latex)
        return
    
    def get_rp_info(self):
        rp_info = [i.text() for i in self.rp_value_entries]
        try:
            if rp_info[-1] == "":
                rp_info[-1] = 2 # type: ignore
            if rp_info[-2] == "":
                rp_info[-2] = 5 # type: ignore

            for i, v in enumerate(rp_info):
                if v == "":
                    rp_info[i] = None # type: ignore
                else:
                    rp_info[i] = float(v) # type: ignore
            return rp_info
        except TypeError:
            return ("Enter valid number")
    
    def update_rp_info(self, rp_info, rp_latex):
        for i, v in enumerate(self.rp_value_outputs):
            v.setText(str(rp_info[i]))
        for i, v in enumerate(self.rp_latex_outputs):
            v.setPixmap(self.parent().get_pixmap_from_latex(str(rp_latex[i]))) # type: ignore
            v.setScaledContents(True)
    
    def clean_rp_menu(self):
        for i in self.rp_value_outputs:
            i.setText("")
        for i in self.rp_latex_outputs:
            i.setPixmap(QtGui.QPixmap())
    
    def goto_main_menu(self, main_window):
        self.centralwidget.hide()
        self.parent().setup_main_menu_Ui(main_window) # type: ignore
        self.parent().centralwidget.show() # type: ignore

class Ui_rhm_menu(QtWidgets.QWidget):
    def __init__(self, main_window=None):
        super().__init__(main_window)
        self.main_window = main_window
        self.setup_rhm_menu_Ui(main_window)

    def setup_rhm_menu_Ui(self, rhm_menu):
        rhm_menu.setObjectName("rhm_menu")
        rhm_menu.resize(self.parent().width_, self.parent().height_) # type: ignore
        self.centralwidget = QtWidgets.QWidget(rhm_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb" + self.parent().color + ";") # type: ignore

        # Set up output grid
        self.rhm_output_grid_obj = QtWidgets.QWidget(self.centralwidget)
        self.rhm_output_grid_obj.setGeometry(QtCore.QRect(610, 220, 332, 311))
        self.rhm_output_grid_obj.setObjectName("rhm_output_grid_obj")
        self.rhm_output_grid = QtWidgets.QGridLayout(self.rhm_output_grid_obj)
        self.rhm_output_grid.setContentsMargins(0, 0, 0, 0)
        self.rhm_output_grid.setObjectName("rhm_output_grid")
        # Length row
        self.rhm_valuetag_length = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_valuetag_length.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rhm_valuetag_length.setObjectName("rhm_valuetag_length")
        self.rhm_output_grid.addWidget(self.rhm_valuetag_length, 0, 0, 1, 1)
        self.rhm_length_value = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_length_value.setObjectName("rhm_length_value")
        self.rhm_output_grid.addWidget(self.rhm_length_value, 0, 1, 1, 1)
        self.rhm_latextag_length = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_latextag_length.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rhm_latextag_length.setObjectName("rhm_latextag_length")
        self.rhm_output_grid.addWidget(self.rhm_latextag_length, 0, 2, 1, 1)
        self.rhm_length_latex = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_length_latex.setObjectName("rhm_length_latex")
        self.rhm_output_grid.addWidget(self.rhm_length_latex, 0, 3, 1, 1)
        # Height row
        self.rhm_valuetag_height = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_valuetag_height.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rhm_valuetag_height.setObjectName("rhm_valuetag_height")
        self.rhm_output_grid.addWidget(self.rhm_valuetag_height, 1, 0, 1, 1)
        self.rhm_height_value = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_height_value.setObjectName("rhm_height_value")
        self.rhm_output_grid.addWidget(self.rhm_height_value, 1, 1, 1, 1)
        self.rhm_latextag_height = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_latextag_height.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rhm_latextag_height.setObjectName("rhm_latextag_height")
        self.rhm_output_grid.addWidget(self.rhm_latextag_height, 1, 2, 1, 1)
        self.rhm_height_latex = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_height_latex.setObjectName("rhm_height_latex")
        self.rhm_output_grid.addWidget(self.rhm_height_latex, 1, 3, 1, 1)
        # Side row
        self.rhm_valuetag_side = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_valuetag_side.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rhm_valuetag_side.setObjectName("rhm_valuetag_side")
        self.rhm_output_grid.addWidget(self.rhm_valuetag_side, 2, 0, 1, 1)
        self.rhm_side_value = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_side_value.setObjectName("rhm_side_value")
        self.rhm_output_grid.addWidget(self.rhm_side_value, 2, 1, 1, 1)
        self.rhm_latextag_side = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_latextag_side.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rhm_latextag_side.setObjectName("rhm_latextag_side")
        self.rhm_output_grid.addWidget(self.rhm_latextag_side, 2, 2, 1, 1)
        self.rhm_side_latex = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_side_latex.setObjectName("rhm_side_latex")
        self.rhm_output_grid.addWidget(self.rhm_side_latex, 2, 3, 1, 1)
        # Skew row
        self.rhm_valuetag_skew = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_valuetag_skew.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rhm_valuetag_skew.setObjectName("rhm_valuetag_skew")
        self.rhm_output_grid.addWidget(self.rhm_valuetag_skew, 3, 0, 1, 1)
        self.rhm_skew_value = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_skew_value.setObjectName("rhm_skew_value")
        self.rhm_output_grid.addWidget(self.rhm_skew_value, 3, 1, 1, 1)
        self.rhm_latextag_skew = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_latextag_skew.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rhm_latextag_skew.setObjectName("rhm_latextag_skew")
        self.rhm_output_grid.addWidget(self.rhm_latextag_skew, 3, 2, 1, 1)
        self.rhm_skew_latex = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_skew_latex.setObjectName("rhm_skew_latex")
        self.rhm_output_grid.addWidget(self.rhm_skew_latex, 3, 3, 1, 1)
        # Perimeter row
        self.rhm_valuetag_perimeter = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_valuetag_perimeter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rhm_valuetag_perimeter.setObjectName("rhm_valuetag_perimeter")
        self.rhm_output_grid.addWidget(self.rhm_valuetag_perimeter, 4, 0, 1, 1)
        self.rhm_perimeter_value = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_perimeter_value.setObjectName("rhm_perimeter_value")
        self.rhm_output_grid.addWidget(self.rhm_perimeter_value, 4, 1, 1, 1)
        self.rhm_latextag_perimeter = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_latextag_perimeter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rhm_latextag_perimeter.setObjectName("rhm_latextag_perimeter")
        self.rhm_output_grid.addWidget(self.rhm_latextag_perimeter, 4, 2, 1, 1)
        self.rhm_perimeter_latex = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_perimeter_latex.setObjectName("rhm_perimeter_latex")
        self.rhm_output_grid.addWidget(self.rhm_perimeter_latex, 4, 3, 1, 1)
        # Surface row
        self.rhm_valuetag_surface = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_valuetag_surface.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rhm_valuetag_surface.setObjectName("rhm_valuetag_surface")
        self.rhm_output_grid.addWidget(self.rhm_valuetag_surface, 5, 0, 1, 1)
        self.rhm_surface_value = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_surface_value.setObjectName("rhm_surface_value")
        self.rhm_output_grid.addWidget(self.rhm_surface_value, 5, 1, 1, 1)
        self.rhm_latextag_surface = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_latextag_surface.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rhm_latextag_surface.setObjectName("rhm_latextag_surface")
        self.rhm_output_grid.addWidget(self.rhm_latextag_surface, 5, 2, 1, 1)
        self.rhm_surface_latex = QtWidgets.QLabel(self.rhm_output_grid_obj)
        self.rhm_surface_latex.setObjectName("rhm_surface_latex")
        self.rhm_output_grid.addWidget(self.rhm_surface_latex, 5, 3, 1, 1)

        # Set up entry grid
        self.rhm_entry_grid_obj = QtWidgets.QWidget(self.centralwidget)
        self.rhm_entry_grid_obj.setGeometry(QtCore.QRect(210, 230, 351, 301))
        self.rhm_entry_grid_obj.setObjectName("rhm_entry_grid_obj")
        self.rhm_entry_grid = QtWidgets.QGridLayout(self.rhm_entry_grid_obj)
        self.rhm_entry_grid.setContentsMargins(0, 0, 0, 0)
        self.rhm_entry_grid.setObjectName("rhm_entry_grid")
        # Length row
        self.rhm_length_label = QtWidgets.QLabel(self.rhm_entry_grid_obj)
        self.rhm_length_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rhm_length_label.setObjectName("rhm_length_label")
        self.rhm_entry_grid.addWidget(self.rhm_length_label, 0, 0, 1, 1)
        self.rhm_length_entry = QtWidgets.QLineEdit(self.rhm_entry_grid_obj)
        self.rhm_length_entry.setObjectName("rhm_length_entry")
        self.rhm_entry_grid.addWidget(self.rhm_length_entry, 0, 1, 1, 1)
        # Height row
        self.rhm_height_label = QtWidgets.QLabel(self.rhm_entry_grid_obj)
        self.rhm_height_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rhm_height_label.setObjectName("rhm_height_label")
        self.rhm_entry_grid.addWidget(self.rhm_height_label, 1, 0, 1, 1)
        self.rhm_height_entry = QtWidgets.QLineEdit(self.rhm_entry_grid_obj)
        self.rhm_height_entry.setObjectName("rhm_height_entry")
        self.rhm_entry_grid.addWidget(self.rhm_height_entry, 1, 1, 1, 1)
        # Side row
        self.rhm_side_label = QtWidgets.QLabel(self.rhm_entry_grid_obj)
        self.rhm_side_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rhm_side_label.setObjectName("rhm_side_label")
        self.rhm_entry_grid.addWidget(self.rhm_side_label, 2, 0, 1, 1)
        self.rhm_side_entry = QtWidgets.QLineEdit(self.rhm_entry_grid_obj)
        self.rhm_side_entry.setObjectName("rhm_side_entry")
        self.rhm_entry_grid.addWidget(self.rhm_side_entry, 2, 1, 1, 1)
        # Skew row
        self.rhm_skew_label = QtWidgets.QLabel(self.rhm_entry_grid_obj)
        self.rhm_skew_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rhm_skew_label.setObjectName("rhm_skew_label")
        self.rhm_entry_grid.addWidget(self.rhm_skew_label, 3, 0, 1, 1)
        self.rhm_skew_entry = QtWidgets.QLineEdit(self.rhm_entry_grid_obj)
        self.rhm_skew_entry.setObjectName("rhm_skew_entry")
        self.rhm_entry_grid.addWidget(self.rhm_skew_entry, 3, 1, 1, 1)
        # Perimeter row
        self.rhm_perimeter_label = QtWidgets.QLabel(self.rhm_entry_grid_obj)
        self.rhm_perimeter_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rhm_perimeter_label.setObjectName("rhm_perimeter_label")
        self.rhm_entry_grid.addWidget(self.rhm_perimeter_label, 4, 0, 1, 1)
        self.rhm_perimeter_entry = QtWidgets.QLineEdit(self.rhm_entry_grid_obj)
        self.rhm_perimeter_entry.setObjectName("rhm_perimeter_entry")
        self.rhm_entry_grid.addWidget(self.rhm_perimeter_entry, 4, 1, 1, 1)
        # Surface row
        self.rhm_surface_label = QtWidgets.QLabel(self.rhm_entry_grid_obj)
        self.rhm_surface_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rhm_surface_label.setObjectName("rhm_surface_label")
        self.rhm_entry_grid.addWidget(self.rhm_surface_label, 5, 0, 1, 1)
        self.rhm_surface_entry = QtWidgets.QLineEdit(self.rhm_entry_grid_obj)
        self.rhm_surface_entry.setObjectName("rhm_surface_entry")
        self.rhm_entry_grid.addWidget(self.rhm_surface_entry, 5, 1, 1, 1)
        # Decimal row
        self.rhm_decimal_label = QtWidgets.QLabel(self.rhm_entry_grid_obj)
        self.rhm_decimal_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.rhm_decimal_label.setObjectName("rhm_decimal_label")
        self.rhm_entry_grid.addWidget(self.rhm_decimal_label, 6, 0, 1, 1)
        self.rhm_decimal_entry = QtWidgets.QLineEdit(self.rhm_entry_grid_obj)
        self.rhm_decimal_entry.setObjectName("rhm_decimal_entry")
        self.rhm_entry_grid.addWidget(self.rhm_decimal_entry, 6, 1, 1, 1)

        # Set up the canvas
        self.canvas_rhomboid = QtWidgets.QGraphicsView(self.centralwidget)
        self.canvas_rhomboid.setGeometry(QtCore.QRect(1150, 150, 500, 500))
        self.canvas_rhomboid.setObjectName("canvas_rhomboid")

        # Set up utility buttons
        self.clean_rhm_screen_button = QtWidgets.QPushButton(self.centralwidget)
        self.clean_rhm_screen_button.setGeometry(QtCore.QRect(230, 550, 130, 50))
        self.clean_rhm_screen_button.setObjectName("clean_rhm_screen_button")
        self.clean_rhm_screen_button.clicked.connect(self.clean_rhm_menu)

        self.draw_rhomboid_button = QtWidgets.QPushButton(self.centralwidget)
        self.draw_rhomboid_button.setGeometry(QtCore.QRect(410, 550, 130, 50))
        self.draw_rhomboid_button.setObjectName("draw_rhomboid_button")
        self.draw_rhomboid_button.clicked.connect(self.draw_rhomboid)

        self.goback_button = QtWidgets.QPushButton(self.centralwidget)
        self.goback_button.setGeometry(QtCore.QRect(410, 630, 130, 50))
        self.goback_button.setObjectName("goback_button")
        self.goback_button.clicked.connect(lambda x: self.goto_main_menu(self.main_window.parent())) # type: ignore

        self.rhomboid_help_button = QtWidgets.QPushButton(self.centralwidget)
        self.rhomboid_help_button.setGeometry(QtCore.QRect(230, 630, 130, 50))
        self.rhomboid_help_button.setObjectName("rhomboid_help_button")
        self.rhomboid_help_button.clicked.connect(self.goto_rhm_help_menu)

        self.rhm_value_entries = [self.rhm_length_entry, self.rhm_height_entry, self.rhm_side_entry, self.rhm_skew_entry, self.rhm_perimeter_entry, self.rhm_surface_entry, self.rhm_decimal_entry]
        self.rhm_value_outputs = [self.rhm_length_value, self.rhm_height_value, self.rhm_side_value, self.rhm_skew_value, self.rhm_perimeter_value, self.rhm_surface_value]
        self.rhm_latex_outputs = [self.rhm_length_latex, self.rhm_height_latex, self.rhm_side_latex, self.rhm_skew_latex, self.rhm_perimeter_latex, self.rhm_surface_latex]
        self.rhm_buttons = [self.clean_rhm_screen_button, self.draw_rhomboid_button, self.goback_button, self.rhomboid_help_button, self.rhm_output_grid_obj, self.rhm_entry_grid_obj]

        for i in self.rhm_buttons:
            i.setStyleSheet("background-color: rgb" + self.parent().button_color + "; border-radius: 10px;") # type: ignore

        for i in self.rhm_value_entries:
            i.setStyleSheet("background-color: white;")

        # Set up other menu stuff
        rhm_menu.parent().setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(rhm_menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        rhm_menu.parent().setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(rhm_menu)
        self.menubar.setStyleSheet("background-color: rgb" + self.parent().color + ";") # type: ignore
        self.statusbar.setStyleSheet("background-color: rgb" + self.parent().color + ";") # type: ignore
        self.statusbar.setObjectName("statusbar") 
        rhm_menu.parent().setStatusBar(self.statusbar)

        self.retranslate_rhm_menu_Ui(rhm_menu)
        QtCore.QMetaObject.connectSlotsByName(rhm_menu)

    def retranslate_rhm_menu_Ui(self, rhm_menu):
        _translate = QtCore.QCoreApplication.translate
        rhm_menu.setWindowTitle(_translate("rhm_menu", "MainWindow"))
        self.rhm_latextag_perimeter.setText(_translate("rhm_menu", "Acquisiton:"))
        self.rhm_length_latex.setText(_translate("rhm_menu", "Latex"))
        self.rhm_valuetag_surface.setText(_translate("rhm_menu", "Surface Value:"))
        self.rhm_valuetag_side.setText(_translate("rhm_menu", "Oblique Side Value:"))
        self.rhm_latextag_side.setText(_translate("rhm_menu", "Acquisiton:"))
        self.rhm_valuetag_height.setText(_translate("rhm_menu", "Height Value:"))
        self.rhm_height_latex.setText(_translate("rhm_menu", "Latex"))
        self.rhm_perimeter_value.setText(_translate("rhm_menu", "TextLabel"))
        self.rhm_surface_value.setText(_translate("rhm_menu", "TextLabel"))
        self.rhm_valuetag_perimeter.setText(_translate("rhm_menu", "Perimeter Value:"))
        self.rhm_valuetag_length.setText(_translate("rhm_menu", "Length Value:"))
        self.rhm_perimeter_latex.setText(_translate("rhm_menu", "Latex"))
        self.rhm_latextag_height.setText(_translate("rhm_menu", "Acquisiton:"))
        self.rhm_side_latex.setText(_translate("rhm_menu", "Latex"))
        self.rhm_length_value.setText(_translate("rhm_menu", "TextLabel"))
        self.rhm_surface_latex.setText(_translate("rhm_menu", "Latex"))
        self.rhm_side_value.setText(_translate("rhm_menu", "TextLabel"))
        self.rhm_height_value.setText(_translate("rhm_menu", "TextLabel"))
        self.rhm_latextag_length.setText(_translate("rhm_menu", "Acquisiton:"))
        self.rhm_latextag_surface.setText(_translate("rhm_menu", "Acquisiton:"))
        self.rhm_valuetag_skew.setText(_translate("rhm_menu", "Skew Value:"))
        self.rhm_skew_value.setText(_translate("rhm_menu", "TextLabel"))
        self.rhm_latextag_skew.setText(_translate("rhm_menu", "Acquisiton:"))
        self.rhm_skew_latex.setText(_translate("rhm_menu", "Latex"))
        self.rhm_length_label.setText(_translate("rhm_menu", "Length:"))
        self.rhm_surface_label.setText(_translate("rhm_menu", "Surface:"))
        self.rhm_height_label.setText(_translate("rhm_menu", "Height:"))
        self.rhm_perimeter_label.setText(_translate("rhm_menu", "Perimeter:"))
        self.rhm_decimal_label.setText(_translate("rhm_menu", "Decimal Precision:"))
        self.rhm_side_label.setText(_translate("rhm_menu", "Oblique Side:"))
        self.rhm_skew_label.setText(_translate("rhm_menu", "Skew:"))
        self.clean_rhm_screen_button.setText(_translate("rhm_menu", "Clean Screen"))
        self.draw_rhomboid_button.setText(_translate("rhm_menu", "Draw Rectangle"))
        self.goback_button.setText(_translate("rhm_menu", "Back to Menu"))
        self.rhomboid_help_button.setText(_translate("rhm_menu", "Help"))

    def goto_rhm_help_menu(self):
        self.centralwidget.hide()
        # ui.setup_rhm_help_menu_Ui(main_menu)
        self.centralwidget.show()
    
    def draw_rhomboid(self):
        length, height, side, skew, perimeter, surface, decimal = self.get_rhm_info() 
        rhomboid = shapez2.Rhomboid(side=side, length=length, height=height, surface=surface, perimeter=perimeter, skew=skew, n=int(decimal)) # type: ignore
        rhm_info, rhm_latex = rhomboid.get_parameters()
        self.update_rhm_info(rhm_info, rhm_latex)
        return
    
    def get_rhm_info(self):
        rhm_info = [i.text() for i in self.rhm_value_entries]
        try:
            if rhm_info[-1] == "":
                rhm_info[-1] = 2 # type: ignore

            for i, v in enumerate(rhm_info):
                if v == "":
                    rhm_info[i] = None # type: ignore
                else:
                    rhm_info[i] = float(v) # type: ignore
            return rhm_info
        except TypeError:
            return ("Enter valid number")
    
    def update_rhm_info(self, rhm_info, rhm_latex):
        length_v, height_v, side_v, skew_v, perimeter_v, surface_v, diagonal_v = rhm_info
        rhm_info = [length_v, height_v, side_v, skew_v, perimeter_v, surface_v]
        length_l, height_l, side_l, skew_l, perimeter_l, surface_l, diagonal_l = rhm_latex
        rhm_latex = [length_l, height_l, side_l, skew_l, perimeter_l, surface_l]
        for i, v in enumerate(self.rhm_value_outputs):
            v.setText(str(rhm_info[i]))
        for i, v in enumerate(self.rhm_latex_outputs):
            v.setPixmap(self.parent().get_pixmap_from_latex(str(rhm_latex[i]))) # type: ignore
            v.setScaledContents(True)
    
    def clean_rhm_menu(self):
        for i in self.rhm_value_outputs:
            i.setText("")
        for i in self.rhm_latex_outputs:
            i.setPixmap(QtGui.QPixmap())

    def goto_main_menu(self, main_window):
        self.centralwidget.hide()
        self.parent().setup_main_menu_Ui(main_window) # type: ignore
        self.parent().centralwidget.show() # type: ignore

class Ui_sq_menu(QtWidgets.QWidget):
    def __init__(self, main_window=None):
        super().__init__(main_window)
        self.main_window = main_window
        self.setup_sq_menu_Ui(main_window)

    def setup_sq_menu_Ui(self, sq_menu):
        sq_menu.setObjectName("sq_menu")
        sq_menu.resize(self.parent().width_, self.parent().height_) # type: ignore
        self.centralwidget = QtWidgets.QWidget(sq_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb" + self.parent().color + ";") # type: ignore

        # Set up output grid
        self.sq_output_grid = QtWidgets.QWidget(self.centralwidget)
        self.sq_output_grid.setGeometry(QtCore.QRect(610, 220, 332, 311))
        self.sq_output_grid.setObjectName("sq_output_grid")
        self.sq_output_grid_obj = QtWidgets.QGridLayout(self.sq_output_grid)
        self.sq_output_grid_obj.setContentsMargins(0, 0, 0, 0)
        self.sq_output_grid_obj.setObjectName("output_grid")
        # Side row
        self.sq_valuetag_side = QtWidgets.QLabel(self.sq_output_grid)
        self.sq_valuetag_side.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.sq_valuetag_side.setObjectName("sq_valuetag_side")
        self.sq_output_grid_obj.addWidget(self.sq_valuetag_side, 0, 0, 1, 1)
        self.sq_side_value = QtWidgets.QLabel(self.sq_output_grid)
        self.sq_side_value.setObjectName("sq_side_value")
        self.sq_output_grid_obj.addWidget(self.sq_side_value, 0, 1, 1, 1)
        self.sq_latextag_side = QtWidgets.QLabel(self.sq_output_grid)
        self.sq_latextag_side.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.sq_latextag_side.setObjectName("sq_latextag_side")
        self.sq_output_grid_obj.addWidget(self.sq_latextag_side, 0, 2, 1, 1)
        self.sq_side_latex = QtWidgets.QLabel(self.sq_output_grid)
        self.sq_side_latex.setObjectName("sq_side_latex")
        self.sq_output_grid_obj.addWidget(self.sq_side_latex, 0, 3, 1, 1)
        # Diagonal row
        self.sq_valuetag_diagonal = QtWidgets.QLabel(self.sq_output_grid)
        self.sq_valuetag_diagonal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.sq_valuetag_diagonal.setObjectName("sq_valuetag_diagonal")
        self.sq_output_grid_obj.addWidget(self.sq_valuetag_diagonal, 1, 0, 1, 1)
        self.sq_diagonal_value = QtWidgets.QLabel(self.sq_output_grid)
        self.sq_diagonal_value.setObjectName("sq_diagonal_value")
        self.sq_output_grid_obj.addWidget(self.sq_diagonal_value, 1, 1, 1, 1)
        self.sq_latextag_diagonal = QtWidgets.QLabel(self.sq_output_grid)
        self.sq_latextag_diagonal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.sq_latextag_diagonal.setObjectName("sq_latextag_diagonal")
        self.sq_output_grid_obj.addWidget(self.sq_latextag_diagonal, 1, 2, 1, 1)
        self.sq_diagonal_latex = QtWidgets.QLabel(self.sq_output_grid)
        self.sq_diagonal_latex.setObjectName("sq_diagonal_latex")
        self.sq_output_grid_obj.addWidget(self.sq_diagonal_latex, 1, 3, 1, 1)
        # Perimeter row
        self.sq_valuetag_perimeter = QtWidgets.QLabel(self.sq_output_grid)
        self.sq_valuetag_perimeter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.sq_valuetag_perimeter.setObjectName("sq_valuetag_perimeter")
        self.sq_output_grid_obj.addWidget(self.sq_valuetag_perimeter, 2, 0, 1, 1)
        self.sq_perimeter_value = QtWidgets.QLabel(self.sq_output_grid)
        self.sq_perimeter_value.setObjectName("sq_perimeter_value")
        self.sq_output_grid_obj.addWidget(self.sq_perimeter_value, 2, 1, 1, 1)
        self.sq_latextag_perimeter = QtWidgets.QLabel(self.sq_output_grid)
        self.sq_latextag_perimeter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.sq_latextag_perimeter.setObjectName("sq_latextag_perimeter")
        self.sq_output_grid_obj.addWidget(self.sq_latextag_perimeter, 2, 2, 1, 1)
        self.sq_perimeter_latex = QtWidgets.QLabel(self.sq_output_grid)
        self.sq_perimeter_latex.setObjectName("sq_perimeter_latex")
        self.sq_output_grid_obj.addWidget(self.sq_perimeter_latex, 2, 3, 1, 1)
        # Surface row
        self.sq_valuetag_surface = QtWidgets.QLabel(self.sq_output_grid)
        self.sq_valuetag_surface.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.sq_valuetag_surface.setObjectName("sq_valuetag_surface")
        self.sq_output_grid_obj.addWidget(self.sq_valuetag_surface, 3, 0, 1, 1)
        self.sq_surface_value = QtWidgets.QLabel(self.sq_output_grid)
        self.sq_surface_value.setObjectName("sq_surface_value")
        self.sq_output_grid_obj.addWidget(self.sq_surface_value, 3, 1, 1, 1)
        self.sq_latextag_surface = QtWidgets.QLabel(self.sq_output_grid)
        self.sq_latextag_surface.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.sq_latextag_surface.setObjectName("sq_latextag_surface")
        self.sq_output_grid_obj.addWidget(self.sq_latextag_surface, 3, 2, 1, 1)
        self.sq_surface_latex = QtWidgets.QLabel(self.sq_output_grid)
        self.sq_surface_latex.setObjectName("sq_surface_latex")
        self.sq_output_grid_obj.addWidget(self.sq_surface_latex, 3, 3, 1, 1)

        # Set up entry grid
        self.sq_entry_grid = QtWidgets.QWidget(self.centralwidget)
        self.sq_entry_grid.setGeometry(QtCore.QRect(210, 230, 351, 301))
        self.sq_entry_grid.setObjectName("sq_entry_grid")
        self.sq_entry_grid_obj = QtWidgets.QGridLayout(self.sq_entry_grid)
        self.sq_entry_grid_obj.setContentsMargins(0, 0, 0, 0)
        self.sq_entry_grid_obj.setObjectName("entry_grid")
        # Side row
        self.sq_side_label = QtWidgets.QLabel(self.sq_entry_grid)
        self.sq_side_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.sq_side_label.setObjectName("sq_side_label")
        self.sq_entry_grid_obj.addWidget(self.sq_side_label, 0, 0, 1, 1)
        self.sq_side_entry = QtWidgets.QLineEdit(self.sq_entry_grid)
        self.sq_side_entry.setObjectName("sq_side_entry")
        self.sq_entry_grid_obj.addWidget(self.sq_side_entry, 0, 1, 1, 1)
        # Diagonal row
        self.sq_diagonal_label = QtWidgets.QLabel(self.sq_entry_grid)
        self.sq_diagonal_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.sq_diagonal_label.setObjectName("sq_diagonal_label")
        self.sq_entry_grid_obj.addWidget(self.sq_diagonal_label, 1, 0, 1, 1)
        self.sq_diagonal_entry = QtWidgets.QLineEdit(self.sq_entry_grid)
        self.sq_diagonal_entry.setObjectName("sq_diagonal_entry")
        self.sq_entry_grid_obj.addWidget(self.sq_diagonal_entry, 1, 1, 1, 1)
        # Perimeter row
        self.sq_perimeter_label = QtWidgets.QLabel(self.sq_entry_grid)
        self.sq_perimeter_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.sq_perimeter_label.setObjectName("sq_perimeter_label")
        self.sq_entry_grid_obj.addWidget(self.sq_perimeter_label, 2, 0, 1, 1)
        self.sq_perimeter_entry = QtWidgets.QLineEdit(self.sq_entry_grid)
        self.sq_perimeter_entry.setObjectName("sq_perimeter_entry")
        self.sq_entry_grid_obj.addWidget(self.sq_perimeter_entry, 2, 1, 1, 1)
        # Surface row
        self.sq_surface_label = QtWidgets.QLabel(self.sq_entry_grid)
        self.sq_surface_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.sq_surface_label.setObjectName("sq_surface_label")
        self.sq_entry_grid_obj.addWidget(self.sq_surface_label, 3, 0, 1, 1)
        self.sq_surface_entry = QtWidgets.QLineEdit(self.sq_entry_grid)
        self.sq_surface_entry.setObjectName("sq_surface_entry")
        self.sq_entry_grid_obj.addWidget(self.sq_surface_entry, 3, 1, 1, 1)
        # Decimal row
        self.sq_decimal_label = QtWidgets.QLabel(self.sq_entry_grid)
        self.sq_decimal_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.sq_decimal_label.setObjectName("sq_decimal_label")
        self.sq_entry_grid_obj.addWidget(self.sq_decimal_label, 4, 0, 1, 1)
        self.sq_decimal_entry = QtWidgets.QLineEdit(self.sq_entry_grid)
        self.sq_decimal_entry.setObjectName("sq_decimal_entry")
        self.sq_entry_grid_obj.addWidget(self.sq_decimal_entry, 4, 1, 1, 1)

        # Set up the canvas
        self.canvas_square = QtWidgets.QGraphicsView(self.centralwidget)
        self.canvas_square.setGeometry(QtCore.QRect(1150, 150, 500, 500))
        self.canvas_square.setObjectName("canvas_square")

        # Set up utility buttons
        self.clean_sq_screen_button = QtWidgets.QPushButton(self.centralwidget)
        self.clean_sq_screen_button.setGeometry(QtCore.QRect(230, 550, 130, 50))
        self.clean_sq_screen_button.setObjectName("clean_screen_button")
        self.clean_sq_screen_button.clicked.connect(self.clean_sq_menu)

        self.draw_square_button = QtWidgets.QPushButton(self.centralwidget)
        self.draw_square_button.setGeometry(QtCore.QRect(410, 550, 130, 50))
        self.draw_square_button.setObjectName("draw_square_button")
        self.draw_square_button.clicked.connect(self.draw_square)

        self.goback_button = QtWidgets.QPushButton(self.centralwidget)
        self.goback_button.setGeometry(QtCore.QRect(410, 630, 130, 50))
        self.goback_button.setObjectName("goback_button")
        self.goback_button.clicked.connect(lambda x: self.goto_main_menu(self.main_window.parent())) # type: ignore

        self.square_help_button = QtWidgets.QPushButton(self.centralwidget)
        self.square_help_button.setGeometry(QtCore.QRect(230, 630, 130, 50))
        self.square_help_button.setObjectName("square_help_button")
        self.square_help_button.clicked.connect(self.goto_sq_help_menu)

        self.sq_value_entries = [self.sq_side_entry, self.sq_diagonal_entry, self.sq_perimeter_entry, self.sq_surface_entry, self.sq_decimal_entry]
        self.sq_value_outputs = [self.sq_side_value, self.sq_diagonal_value, self.sq_perimeter_value, self.sq_surface_value]
        self.sq_latex_outputs = [self.sq_side_latex, self.sq_diagonal_latex, self.sq_perimeter_latex, self.sq_surface_latex]
        self.sq_buttons = [self.clean_sq_screen_button, self.draw_square_button, self.goback_button, self.square_help_button, self.sq_output_grid, self.sq_entry_grid]

        for i in self.sq_buttons:
            i.setStyleSheet("background-color: rgb" + self.parent().button_color + "; border-radius: 10px;") # type: ignore

        for i in self.sq_value_entries:
            i.setStyleSheet("background-color: white;")

        # Set up other menu stuff
        sq_menu.parent().setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(sq_menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        sq_menu.parent().setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(sq_menu)
        self.menubar.setStyleSheet("background-color: rgb" + self.parent().color + ";") # type: ignore
        self.statusbar.setStyleSheet("background-color: rgb" + self.parent().color + ";") # type: ignore
        self.statusbar.setObjectName("statusbar")
        sq_menu.parent().setStatusBar(self.statusbar)

        self.retranslate_sq_menu_Ui(sq_menu)
        QtCore.QMetaObject.connectSlotsByName(sq_menu)

    def retranslate_sq_menu_Ui(self, sq_menu):
        _translate = QtCore.QCoreApplication.translate
        sq_menu.setWindowTitle(_translate("sq_menu", "SquareWindow"))
        self.sq_latextag_perimeter.setText(_translate("sq_menu", "Acquisiton:"))
        self.sq_perimeter_latex.setText(_translate("sq_menu", "Latex"))
        self.sq_valuetag_side.setText(_translate("sq_menu", "Side Value:"))
        self.sq_latextag_diagonal.setText(_translate("sq_menu", "Acquisiton:"))
        self.sq_surface_value.setText(_translate("sq_menu", "TextLabel"))
        self.sq_diagonal_latex.setText(_translate("sq_menu", "Latex"))
        self.sq_latextag_surface.setText(_translate("sq_menu", "Acquisiton:"))
        self.sq_side_latex.setText(_translate("sq_menu", "Latex"))
        self.sq_diagonal_value.setText(_translate("sq_menu", "TextLabel"))
        self.sq_latextag_side.setText(_translate("sq_menu", "Acquisiton:"))
        self.sq_perimeter_value.setText(_translate("sq_menu", "TextLabel"))
        self.sq_side_value.setText(_translate("sq_menu", "TextLabel"))
        self.sq_valuetag_perimeter.setText(_translate("sq_menu", "Perimeter Value:"))
        self.sq_valuetag_surface.setText(_translate("sq_menu", "Surface Value:"))
        self.sq_valuetag_diagonal.setText(_translate("sq_menu", "Diagonal Value:"))
        self.sq_surface_latex.setText(_translate("sq_menu", "Latex"))
        self.sq_decimal_label.setText(_translate("sq_menu", "Decimal Precision:"))
        self.sq_diagonal_label.setText(_translate("sq_menu", "Diagonal:"))
        self.sq_perimeter_label.setText(_translate("sq_menu", "Perimeter:"))
        self.sq_surface_label.setText(_translate("sq_menu", "Surface:"))
        self.sq_side_label.setText(_translate("sq_menu", "Side:"))
        self.clean_sq_screen_button.setText(_translate("sq_menu", "Clean Screen"))
        self.draw_square_button.setText(_translate("sq_menu", "Draw Square"))
        self.goback_button.setText(_translate("sq_menu", "Back to Menu"))
        self.square_help_button.setText(_translate("sq_menu", "Help"))
    
    def goto_sq_help_menu(self):
        self.centralwidget.hide()
        # ui.setup_sq_help_menu_Ui(main_menu)
        self.centralwidget.show()
    
    def draw_square(self):
        side, diagonal, perimeter, surface, decimal = self.get_sq_info() 
        square = shapez2.Square(side=side, diagonal=diagonal, perimeter=perimeter, surface=surface, n=int(decimal)) # type: ignore
        sq_info, sq_latex = square.get_parameters()
        self.update_sq_info(sq_info, sq_latex)
        return
    
    def get_sq_info(self):
        sq_info = [i.text() for i in self.sq_value_entries]
        try:
            if sq_info[-1] == "":
                sq_info[-1] = 2 # type: ignore

            for i, v in enumerate(sq_info):
                if v == "":
                    sq_info[i] = None # type: ignore
                else:
                    sq_info[i] = float(v) # type: ignore
            return sq_info
        except TypeError:
            return ("Enter valid number")
    
    def update_sq_info(self, sq_info, sq_latex):
        for i, v in enumerate(self.sq_value_outputs):
            v.setText(str(sq_info[i]))
        for i, v in enumerate(self.sq_latex_outputs):
            v.setPixmap(self.parent().get_pixmap_from_latex(str(sq_latex[i]))) # type: ignore
            v.setScaledContents(True)
    
    def clean_sq_menu(self):
        for i in self.sq_value_outputs:
            i.setText("")
        for i in self.sq_latex_outputs:
            i.setPixmap(QtGui.QPixmap())
    
    def goto_main_menu(self, main_window):
        self.centralwidget.hide()
        self.parent().setup_main_menu_Ui(main_window) # type: ignore
        self.parent().centralwidget.show() # type: ignore

class Ui_tgl_menu(QtWidgets.QWidget):
    def __init__(self, main_window=None):
        super().__init__(main_window)
        self.main_window = main_window
        self.setup_tgl_menu_Ui(main_window)

    def setup_tgl_menu_Ui(self, tgl_menu):
        tgl_menu.setObjectName("tgl_menu")
        tgl_menu.resize(self.parent().width_, self.parent().height_) # type: ignore
        self.centralwidget = QtWidgets.QWidget(tgl_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb" + self.parent().color + ";") # type: ignore

        # Set up output grid
        self.tgl_output_grid_obj = QtWidgets.QWidget(self.centralwidget)
        self.tgl_output_grid_obj.setGeometry(QtCore.QRect(610, 220, 332, 311))
        self.tgl_output_grid_obj.setObjectName("tgl_output_grid_obj")
        self.tgl_output_grid = QtWidgets.QGridLayout(self.tgl_output_grid_obj)
        self.tgl_output_grid.setContentsMargins(0, 0, 0, 0)
        self.tgl_output_grid.setObjectName("tgl_output_grid")
        # Angle1 row
        self.tgl_valuetag_angle1 = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_valuetag_angle1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_valuetag_angle1.setObjectName("tgl_valuetag_angle1")
        self.tgl_output_grid.addWidget(self.tgl_valuetag_angle1, 0, 0, 1, 1)
        self.tgl_angle1_value = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_angle1_value.setObjectName("tgl_angle1_value")
        self.tgl_output_grid.addWidget(self.tgl_angle1_value, 0, 1, 1, 1)
        self.tgl_latextag_angle1 = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_latextag_angle1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_latextag_angle1.setObjectName("tgl_latextag_angle1")
        self.tgl_output_grid.addWidget(self.tgl_latextag_angle1, 0, 2, 1, 1)
        self.tgl_angle1_latex = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_angle1_latex.setObjectName("tgl_angle1_latex")
        self.tgl_output_grid.addWidget(self.tgl_angle1_latex, 0, 3, 1, 1)
        # Angle2 row
        self.tgl_valuetag_angle2 = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_valuetag_angle2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_valuetag_angle2.setObjectName("tgl_valuetag_angle2")
        self.tgl_output_grid.addWidget(self.tgl_valuetag_angle2, 1, 0, 1, 1)
        self.tgl_angle2_value = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_angle2_value.setObjectName("tgl_angle2_value")
        self.tgl_output_grid.addWidget(self.tgl_angle2_value, 1, 1, 1, 1)
        self.tgl_latextag_angle2 = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_latextag_angle2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_latextag_angle2.setObjectName("tgl_latextag_angle2")
        self.tgl_output_grid.addWidget(self.tgl_latextag_angle2, 1, 2, 1, 1)
        self.tgl_angle2_latex = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_angle2_latex.setObjectName("tgl_angle2_latex")
        self.tgl_output_grid.addWidget(self.tgl_angle2_latex, 1, 3, 1, 1)
        # Angle3 row
        self.tgl_valuetag_angle3 = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_valuetag_angle3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_valuetag_angle3.setObjectName("tgl_valuetag_angle3")
        self.tgl_output_grid.addWidget(self.tgl_valuetag_angle3, 2, 0, 1, 1)
        self.tgl_angle3_value = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_angle3_value.setObjectName("tgl_angle3_value")
        self.tgl_output_grid.addWidget(self.tgl_angle3_value, 2, 1, 1, 1)
        self.tgl_latextag_angle3 = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_latextag_angle3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_latextag_angle3.setObjectName("tgl_latextag_angle3")
        self.tgl_output_grid.addWidget(self.tgl_latextag_angle3, 2, 2, 1, 1)
        self.tgl_angle3_latex = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_angle3_latex.setObjectName("tgl_angle3_latex")
        self.tgl_output_grid.addWidget(self.tgl_angle3_latex, 2, 3, 1, 1)
        # Side1 row
        self.tgl_valuetag_side1 = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_valuetag_side1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_valuetag_side1.setObjectName("tgl_valuetag_side1")
        self.tgl_output_grid.addWidget(self.tgl_valuetag_side1, 3, 0, 1, 1)
        self.tgl_side1_value = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_side1_value.setObjectName("tgl_side1_value")
        self.tgl_output_grid.addWidget(self.tgl_side1_value, 3, 1, 1, 1)
        self.tgl_latextag_side1 = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_latextag_side1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_latextag_side1.setObjectName("tgl_latextag_side1")
        self.tgl_output_grid.addWidget(self.tgl_latextag_side1, 3, 2, 1, 1)
        self.tgl_side1_latex = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_side1_latex.setObjectName("tgl_side1_latex")
        self.tgl_output_grid.addWidget(self.tgl_side1_latex, 3, 3, 1, 1)
        # Side2 row
        self.tgl_valuetag_side2 = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_valuetag_side2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_valuetag_side2.setObjectName("tgl_valuetag_side2")
        self.tgl_output_grid.addWidget(self.tgl_valuetag_side2, 4, 0, 1, 1)
        self.tgl_side2_value = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_side2_value.setObjectName("tgl_side2_value")
        self.tgl_output_grid.addWidget(self.tgl_side2_value, 4, 1, 1, 1)
        self.tgl_latextag_side2 = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_latextag_side2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_latextag_side2.setObjectName("tgl_latextag_side2")
        self.tgl_output_grid.addWidget(self.tgl_latextag_side2, 4, 2, 1, 1)
        self.tgl_side2_latex = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_side2_latex.setObjectName("tgl_side2_latex")
        self.tgl_output_grid.addWidget(self.tgl_side2_latex, 4, 3, 1, 1)
        # Side3 row      
        self.tgl_valuetag_side3 = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_valuetag_side3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_valuetag_side3.setObjectName("tgl_valuetag_side3")
        self.tgl_output_grid.addWidget(self.tgl_valuetag_side3, 5, 0, 1, 1)
        self.tgl_side3_value = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_side3_value.setObjectName("tgl_side3_value")
        self.tgl_output_grid.addWidget(self.tgl_side3_value, 5, 1, 1, 1)
        self.tgl_latextag_side3 = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_latextag_side3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_latextag_side3.setObjectName("tgl_latextag_side3")
        self.tgl_output_grid.addWidget(self.tgl_latextag_side3, 5, 2, 1, 1)
        self.tgl_side3_latex = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_side3_latex.setObjectName("tgl_side3_latex")
        self.tgl_output_grid.addWidget(self.tgl_side3_latex, 5, 3, 1, 1)
        # Perimeter row
        self.tgl_valuetag_perimeter = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_valuetag_perimeter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_valuetag_perimeter.setObjectName("tgl_valuetag_perimeter")
        self.tgl_output_grid.addWidget(self.tgl_valuetag_perimeter, 6, 0, 1, 1)
        self.tgl_perimeter_value = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_perimeter_value.setObjectName("tgl_perimeter_value")
        self.tgl_output_grid.addWidget(self.tgl_perimeter_value, 6, 1, 1, 1)
        self.tgl_latextag_perimeter = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_latextag_perimeter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_latextag_perimeter.setObjectName("tgl_latextag_perimeter")
        self.tgl_output_grid.addWidget(self.tgl_latextag_perimeter, 6, 2, 1, 1)
        self.tgl_perimeter_latex = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_perimeter_latex.setObjectName("tgl_perimeter_latex")
        self.tgl_output_grid.addWidget(self.tgl_perimeter_latex, 6, 3, 1, 1)
        # Surface row
        self.tgl_valuetag_surface = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_valuetag_surface.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_valuetag_surface.setObjectName("tgl_valuetag_surface")
        self.tgl_output_grid.addWidget(self.tgl_valuetag_surface, 7, 0, 1, 1)
        self.tgl_surface_value = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_surface_value.setObjectName("tgl_surface_value")
        self.tgl_output_grid.addWidget(self.tgl_surface_value, 7, 1, 1, 1)
        self.tgl_latextag_surface = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_latextag_surface.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_latextag_surface.setObjectName("tgl_latextag_surface")
        self.tgl_output_grid.addWidget(self.tgl_latextag_surface, 7, 2, 1, 1)
        self.tgl_surface_latex = QtWidgets.QLabel(self.tgl_output_grid_obj)
        self.tgl_surface_latex.setObjectName("tgl_surface_latex")
        self.tgl_output_grid.addWidget(self.tgl_surface_latex, 7, 3, 1, 1)

        # Set up entry grid
        self.tgl_entry_grid_obj = QtWidgets.QWidget(self.centralwidget)
        self.tgl_entry_grid_obj.setGeometry(QtCore.QRect(210, 230, 351, 301))
        self.tgl_entry_grid_obj.setObjectName("tgl_entry_grid_obj")
        self.tgl_entry_grid = QtWidgets.QGridLayout(self.tgl_entry_grid_obj)
        self.tgl_entry_grid.setContentsMargins(0, 0, 0, 0)
        self.tgl_entry_grid.setObjectName("tgl_entry_grid")
        # Angle1 row
        self.tgl_angle1_label = QtWidgets.QLabel(self.tgl_entry_grid_obj)
        self.tgl_angle1_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_angle1_label.setObjectName("tgl_angle1_label")
        self.tgl_entry_grid.addWidget(self.tgl_angle1_label, 0, 0, 1, 1)
        self.tgl_angle1_entry = QtWidgets.QLineEdit(self.tgl_entry_grid_obj)
        self.tgl_angle1_entry.setObjectName("tgl_angle1_entry")
        self.tgl_entry_grid.addWidget(self.tgl_angle1_entry, 0, 1, 1, 1)
        # Angle2 row
        self.tgl_angle2_label = QtWidgets.QLabel(self.tgl_entry_grid_obj)
        self.tgl_angle2_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_angle2_label.setObjectName("tgl_angle2_label")
        self.tgl_entry_grid.addWidget(self.tgl_angle2_label, 1, 0, 1, 1)
        self.tgl_angle2_entry = QtWidgets.QLineEdit(self.tgl_entry_grid_obj)
        self.tgl_angle2_entry.setObjectName("tgl_angle2_entry")
        self.tgl_entry_grid.addWidget(self.tgl_angle2_entry, 1, 1, 1, 1)
        # Angle3 row
        self.tgl_angle3_label = QtWidgets.QLabel(self.tgl_entry_grid_obj)
        self.tgl_angle3_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_angle3_label.setObjectName("tgl_angle3_label")
        self.tgl_entry_grid.addWidget(self.tgl_angle3_label, 2, 0, 1, 1)
        self.tgl_angle3_entry = QtWidgets.QLineEdit(self.tgl_entry_grid_obj)
        self.tgl_angle3_entry.setObjectName("tgl_angle3_entry")
        self.tgl_entry_grid.addWidget(self.tgl_angle3_entry, 2, 1, 1, 1)
        # Side1 row
        self.tgl_side1_label = QtWidgets.QLabel(self.tgl_entry_grid_obj)
        self.tgl_side1_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_side1_label.setObjectName("tgl_side1_label")
        self.tgl_entry_grid.addWidget(self.tgl_side1_label, 3, 0, 1, 1)
        self.tgl_side1_entry = QtWidgets.QLineEdit(self.tgl_entry_grid_obj)
        self.tgl_side1_entry.setObjectName("tgl_side1_entry")
        self.tgl_entry_grid.addWidget(self.tgl_side1_entry, 3, 1, 1, 1)
        # Side2 row
        self.tgl_side2_label = QtWidgets.QLabel(self.tgl_entry_grid_obj)
        self.tgl_side2_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_side2_label.setObjectName("tgl_side2_label")
        self.tgl_entry_grid.addWidget(self.tgl_side2_label, 4, 0, 1, 1)
        self.tgl_side2_entry = QtWidgets.QLineEdit(self.tgl_entry_grid_obj)
        self.tgl_side2_entry.setObjectName("tgl_side2_entry")
        self.tgl_entry_grid.addWidget(self.tgl_side2_entry, 4, 1, 1, 1)
        # Side3 row
        self.tgl_side3_label = QtWidgets.QLabel(self.tgl_entry_grid_obj)
        self.tgl_side3_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_side3_label.setObjectName("tgl_side3_label")
        self.tgl_entry_grid.addWidget(self.tgl_side3_label, 5, 0, 1, 1)
        self.tgl_side3_entry = QtWidgets.QLineEdit(self.tgl_entry_grid_obj)
        self.tgl_side3_entry.setObjectName("tgl_side3_entry")
        self.tgl_entry_grid.addWidget(self.tgl_side3_entry, 5, 1, 1, 1)
        # Perimeter row
        self.tgl_perimeter_label = QtWidgets.QLabel(self.tgl_entry_grid_obj)
        self.tgl_perimeter_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_perimeter_label.setObjectName("tgl_perimeter_label")
        self.tgl_entry_grid.addWidget(self.tgl_perimeter_label, 6, 0, 1, 1)
        self.tgl_perimeter_entry = QtWidgets.QLineEdit(self.tgl_entry_grid_obj)
        self.tgl_perimeter_entry.setObjectName("tgl_perimeter_entry")
        self.tgl_entry_grid.addWidget(self.tgl_perimeter_entry, 6, 1, 1, 1)
        # Surface row
        self.tgl_surface_label = QtWidgets.QLabel(self.tgl_entry_grid_obj)
        self.tgl_surface_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_surface_label.setObjectName("tgl_surface_label")
        self.tgl_entry_grid.addWidget(self.tgl_surface_label, 7, 0, 1, 1)
        self.tgl_surface_entry = QtWidgets.QLineEdit(self.tgl_entry_grid_obj)
        self.tgl_surface_entry.setObjectName("tgl_surface_entry")
        self.tgl_entry_grid.addWidget(self.tgl_surface_entry, 7, 1, 1, 1)
        # Decimal row
        self.tgl_decimal_label = QtWidgets.QLabel(self.tgl_entry_grid_obj)
        self.tgl_decimal_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter) # type: ignore
        self.tgl_decimal_label.setObjectName("tgl_decimal_label")
        self.tgl_entry_grid.addWidget(self.tgl_decimal_label, 8, 0, 1, 1)
        self.tgl_decimal_entry = QtWidgets.QLineEdit(self.tgl_entry_grid_obj)
        self.tgl_decimal_entry.setObjectName("tgl_decimal_entry")
        self.tgl_entry_grid.addWidget(self.tgl_decimal_entry, 8, 1, 1, 1)

        # Set up the canvas
        self.canvas_triangle = QtWidgets.QGraphicsView(self.centralwidget)
        self.canvas_triangle.setGeometry(QtCore.QRect(1150, 140, 500, 500))
        self.canvas_triangle.setObjectName("canvas_triangle")

        # Set up utility buttons
        self.clean_tgl_screen_button = QtWidgets.QPushButton(self.centralwidget)
        self.clean_tgl_screen_button.setGeometry(QtCore.QRect(230, 550, 130, 50))
        self.clean_tgl_screen_button.setObjectName("clean_tgl_screen_button")
        self.clean_tgl_screen_button.clicked.connect(self.clean_tgl_menu)

        self.draw_triangle_button = QtWidgets.QPushButton(self.centralwidget)
        self.draw_triangle_button.setGeometry(QtCore.QRect(410, 550, 130, 50))
        self.draw_triangle_button.setObjectName("draw_triangle_button")
        self.draw_triangle_button.clicked.connect(self.draw_triangle)

        self.goback_button = QtWidgets.QPushButton(self.centralwidget)
        self.goback_button.setGeometry(QtCore.QRect(410, 630, 130, 50))
        self.goback_button.setObjectName("goback_button")
        self.goback_button.clicked.connect(lambda x: self.goto_main_menu(self.main_window.parent())) # type: ignore

        self.triangle_help_button = QtWidgets.QPushButton(self.centralwidget)
        self.triangle_help_button.setGeometry(QtCore.QRect(230, 630, 130, 50))
        self.triangle_help_button.setObjectName("triangle_help_button")
        self.triangle_help_button.clicked.connect(self.goto_tgl_help_menu)

        self.tgl_value_entries = [self.tgl_angle1_entry, self.tgl_angle2_entry, self.tgl_angle3_entry, self.tgl_side1_entry, self.tgl_side2_entry, self.tgl_side3_entry, self.tgl_perimeter_entry, self.tgl_surface_entry, self.tgl_decimal_entry]
        self.tgl_value_outputs = [self.tgl_angle1_value, self.tgl_angle2_value, self.tgl_angle3_value, self.tgl_side1_value, self.tgl_side2_value, self.tgl_side3_value, self.tgl_perimeter_value, self.tgl_surface_value]
        self.tgl_latex_outputs = [self.tgl_angle1_latex, self.tgl_angle2_latex, self.tgl_angle3_latex, self.tgl_side1_latex, self.tgl_side2_latex, self.tgl_side3_latex, self.tgl_perimeter_latex, self.tgl_surface_latex]
        self.tgl_buttons = [self.clean_tgl_screen_button, self.draw_triangle_button, self.goback_button, self.triangle_help_button, self.tgl_output_grid_obj, self.tgl_entry_grid_obj]

        for i in self.tgl_buttons:
            i.setStyleSheet("background-color: rgb" + self.parent().button_color + "; border-radius: 10px;") # type: ignore

        for i in self.tgl_value_entries:
            i.setStyleSheet("background-color: white;")

        # Set up other menu stuff
        tgl_menu.parent().setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(tgl_menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        tgl_menu.parent().setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(tgl_menu)
        self.menubar.setStyleSheet("background-color: rgb" + self.parent().color + ";") # type: ignore
        self.statusbar.setStyleSheet("background-color: rgb" + self.parent().color + ";") # type: ignore
        self.statusbar.setObjectName("statusbar")
        tgl_menu.parent().setStatusBar(self.statusbar)

        self.retranslate_tgl_menu_Ui(tgl_menu)
        QtCore.QMetaObject.connectSlotsByName(tgl_menu)

    def retranslate_tgl_menu_Ui(self, tgl_menu):
        _translate = QtCore.QCoreApplication.translate
        tgl_menu.setWindowTitle(_translate("tgl_menu", "MainWindow"))
        self.tgl_latextag_perimeter.setText(_translate("tgl_menu", "Acquisiton:"))
        self.tgl_valuetag_side1.setText(_translate("tgl_menu", "Side 1 value:"))
        self.tgl_side2_latex.setText(_translate("tgl_menu", "Latex"))
        self.tgl_angle1_latex.setText(_translate("tgl_menu", "Latex"))
        self.tgl_latextag_side1.setText(_translate("tgl_menu", "Acquisiton:"))
        self.tgl_latextag_side2.setText(_translate("tgl_menu", "Acquisiton:"))
        self.tgl_valuetag_surface.setText(_translate("tgl_menu", "Surface Value:"))
        self.tgl_valuetag_angle3.setText(_translate("tgl_menu", "Angle 3 value:"))
        self.tgl_latextag_angle3.setText(_translate("tgl_menu", "Acquisiton:"))
        self.tgl_angle2_latex.setText(_translate("tgl_menu", "Latex"))
        self.tgl_valuetag_angle2.setText(_translate("tgl_menu", "Angle 2 value:"))
        self.tgl_perimeter_value.setText(_translate("tgl_menu", "TextLabel"))
        self.tgl_surface_value.setText(_translate("tgl_menu", "TextLabel"))
        self.tgl_valuetag_side2.setText(_translate("tgl_menu", "Side 2 value:"))
        self.tgl_valuetag_perimeter.setText(_translate("tgl_menu", "Perimeter Value:"))
        self.tgl_valuetag_angle1.setText(_translate("tgl_menu", "Angle 1 value:"))
        self.tgl_perimeter_latex.setText(_translate("tgl_menu", "Latex"))
        self.tgl_side1_value.setText(_translate("tgl_menu", "TextLabel"))
        self.tgl_latextag_angle2.setText(_translate("tgl_menu", "Acquisiton:"))
        self.tgl_angle3_latex.setText(_translate("tgl_menu", "Latex"))
        self.tgl_angle1_value.setText(_translate("tgl_menu", "TextLabel"))
        self.tgl_surface_latex.setText(_translate("tgl_menu", "Latex"))
        self.tgl_angle3_value.setText(_translate("tgl_menu", "TextLabel"))
        self.tgl_side1_latex.setText(_translate("tgl_menu", "Latex"))
        self.tgl_angle2_value.setText(_translate("tgl_menu", "TextLabel"))
        self.tgl_latextag_angle1.setText(_translate("tgl_menu", "Acquisiton:"))
        self.tgl_side2_value.setText(_translate("tgl_menu", "TextLabel"))
        self.tgl_latextag_surface.setText(_translate("tgl_menu", "Acquisiton:"))
        self.tgl_valuetag_side3.setText(_translate("tgl_menu", "Side 3 value:"))
        self.tgl_side3_value.setText(_translate("tgl_menu", "TextLabel"))
        self.tgl_latextag_side3.setText(_translate("tgl_menu", "Acquisiton:"))
        self.tgl_side3_latex.setText(_translate("tgl_menu", "Latex"))
        self.tgl_angle1_label.setText(_translate("tgl_menu", "Angle 1:"))
        self.tgl_surface_label.setText(_translate("tgl_menu", "Surface:"))
        self.tgl_angle2_label.setText(_translate("tgl_menu", "Angle 2:"))
        self.tgl_side2_label.setText(_translate("tgl_menu", "Side 2:"))
        self.tgl_perimeter_label.setText(_translate("tgl_menu", "Perimeter:"))
        self.tgl_decimal_label.setText(_translate("tgl_menu", "Decimal Precision:"))
        self.tgl_angle3_label.setText(_translate("tgl_menu", "Angle 3:"))
        self.tgl_side1_label.setText(_translate("tgl_menu", "Side 1:"))
        self.tgl_side3_label.setText(_translate("tgl_menu", "Side 3:"))
        self.clean_tgl_screen_button.setText(_translate("tgl_menu", "Clean Screen"))
        self.draw_triangle_button.setText(_translate("tgl_menu", "Draw Triangle"))
        self.goback_button.setText(_translate("tgl_menu", "Back to Menu"))
        self.triangle_help_button.setText(_translate("tgl_menu", "Help"))

    def goto_tgl_help_menu(self):
        self.centralwidget.hide()
        # ui.setup_tgl_help_menu_Ui(main_menu)
        self.centralwidget.show()
    
    def draw_triangle(self):
        angle1, angle2, angle3, side1, side2, side3, perimeter, surface, decimal = self.get_tgl_info() 
        triangle = shapez2.Triangle(angle1=angle1, angle2=angle2, angle3=angle3, side1=side1, side2=side2, side3=side3, perimeter=perimeter, surface=surface, n=int(decimal)) # type: ignore
        tgl_info, tgl_latex = triangle.get_parameters()
        self.update_tgl_info(tgl_info, tgl_latex)
        return
    
    def get_tgl_info(self):
        tgl_info = [i.text() for i in self.tgl_value_entries]
        try:
            if tgl_info[-1] == "":
                tgl_info[-1] = 2 # type: ignore

            for i, v in enumerate(tgl_info):
                if v == "":
                    tgl_info[i] = None # type: ignore
                else:
                    tgl_info[i] = float(v) # type: ignore
            return tgl_info
        except TypeError:
            return ("Enter valid number")
    
    def update_tgl_info(self, tgl_info, tgl_latex):
        for i, v in enumerate(self.tgl_value_outputs):
            v.setText(str(tgl_info[i]))
        for i, v in enumerate(self.tgl_latex_outputs):
            v.setPixmap(self.parent().get_pixmap_from_latex(str(tgl_latex[i]))) # type: ignore
            v.setScaledContents(True)
    
    def clean_tgl_menu(self):
        for i in self.tgl_value_outputs:
            i.setText("")
        for i in self.tgl_latex_outputs:
            i.setPixmap(QtGui.QPixmap())
    
    def goto_main_menu(self, main_window):
        self.centralwidget.hide()
        self.parent().setup_main_menu_Ui(main_window) # type: ignore
        self.parent().centralwidget.show() # type: ignore

class Ui_ghelp_menu(QtWidgets.QWidget):
    def __init__(self, main_window=None):
        super().__init__(main_window)
        self.main_window = main_window
        self.setup_general_help_menu_Ui(main_window)

    def setup_general_help_menu_Ui(self, ghelp_menu):
        ghelp_menu.setObjectName("ghelp_menu")
        ghelp_menu.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(ghelp_menu)
        self.centralwidget.setObjectName("centralwidget")

        # Set up the go back button
        self.goback_button = QtWidgets.QPushButton(self.centralwidget)
        self.goback_button.setGeometry(QtCore.QRect(1740, 930, 130, 50))
        self.goback_button.setObjectName("goback_button")
        self.goback_button.setStyleSheet("background-color: rgb" + self.parent().button_color + "; border-radius: 10px;") # type: ignore
        self.goback_button.clicked.connect(lambda x: self.goto_main_menu(self.main_window.parent())) # type: ignore

        # Set up the scrolling area
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(50, 130, 1810, 780))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1810, 780))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 1810, 780))
        self.textEdit.setObjectName("textEdit")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        ghelp_menu.parent().setCentralWidget(self.centralwidget)

        # Set up other menu stuff 
        self.menubar = QtWidgets.QMenuBar(ghelp_menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        ghelp_menu.parent().setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ghelp_menu)
        self.statusbar.setObjectName("statusbar")
        ghelp_menu.parent().setStatusBar(self.statusbar)

        self.retranslate_ghelp_menu_Ui(ghelp_menu)
        QtCore.QMetaObject.connectSlotsByName(ghelp_menu)

    def retranslate_ghelp_menu_Ui(self, ghelp_menu):
        _translate = QtCore.QCoreApplication.translate
        ghelp_menu.setWindowTitle(_translate("ghelp_menu", "MainWindow"))
        self.goback_button.setText(_translate("ghelp_menu", "Back to Menu"))
        self.loadFile(cwd + "\\help.txt")
    
    def loadFile(self, filename):
        with open(filename, 'r') as f:
            text = f.read()
        self.textEdit.setText(text)
    
    def goto_main_menu(self, main_window):
        self.centralwidget.hide()
        self.parent().setup_main_menu_Ui(main_window) # type: ignore
        self.parent().centralwidget.show() # type: ignore
    # ^^^ GENERAL HELP MENU ITEMS ^^^ #

