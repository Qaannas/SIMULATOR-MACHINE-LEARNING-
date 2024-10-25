################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (
    QCoreApplication,
    QPropertyAnimation,
    QDate,
    QDateTime,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
    QEvent,
)
from PySide2.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QKeySequence,
    QLinearGradient,
    QPalette,
    QPainter,
    QPixmap,
    QRadialGradient,
)

from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, 250, True)
        )

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.btn_page_1.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
        )

        # PAGE 2
        self.ui.btn_page_2.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        )

        # PAGE 3
        self.ui.btn_page_3.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
        )
        # PAGE 4
        self.ui.pushButton_2.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)
        )
        # PAGE 5
        self.ui.pushButton_4.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_5)
        )
        
        self.ui.pushButton_11.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_6))
                                              
        ## BUTTONS
        self.ui.pushButton.clicked.connect(self.ui.display_selected_plot)

        # Connect radio button toggled events
        self.ui.comboBox.currentTextChanged.connect(self.ui.check)

        self.ui.radioButton.toggled.connect(self.ui.display_selected_plot)

        self.ui.radioButton_2.toggled.connect(self.ui.display_selected_plot)

        self.ui.radioButton_2.toggled.connect(self.ui.radioButtonToggled)
        
        self.ui.pushButton_5.clicked.connect(self.ui.display_knn)

        self.ui.pushButton_7.clicked.connect(self.ui.Simulate_K_Means)

        self.ui.pushButton_9.clicked.connect(self.ui.simulate_svm)

        self.ui.pushButton_10.clicked.connect(self.ui.SVM)

        self.ui.pushButton_4_5.clicked.connect(self.ui.Hamming_plot)

        self.ui.pushButton_4_6.clicked.connect(self.ui.metrics_knn)
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
