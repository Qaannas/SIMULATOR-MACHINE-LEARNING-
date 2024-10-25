# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainguarlY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from sklearn import svm
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.datasets import make_classification


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 622)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet("background-color:rgb(45, 45, 45);")
        MainWindow.setWindowTitle("Simulation of Machine Learning")
        icon = QIcon("icon.png")  
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName("Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName("frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName("Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "border: 0px solid;"
        )

        self.verticalLayout_2.addWidget(self.Btn_Toggle)

        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName("frame_top")
        self.frame_top.setStyleSheet("background-color: rgb(37, 39, 48);")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.label_11 = QLabel(self.frame_top)
        self.label_11.setObjectName("label_11")
        self.label_11.setGeometry(QRect(130, -10, 641, 71))
        font = QFont()
        font.setFamily("Helvetica")
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(
            "/* Apply styles to the QLabel class for a UI design title */\n"
            "QLabel {\n"
            "  /* Set font properties */\n"
            "  font-family: 'Helvetica', sans-serif;\n"
            "  font-size: 24px;\n"
            "  font-weight: bold;\n"
            "  \n"
            "  /* Set text color */\n"
            "   /* You can use your preferred text color */\n"
            "	color: rgb(85, 170, 255);\n"
            "  \n"
            "  /* Set padding and margin */\n"
            "  padding: 10px;\n"
            "  margin: 10px 0;\n"
            "  \n"
            "  /* Set background color */\n"
            "   /* Your specified background color */\n"
            "\n"
            "  /* Set text alignment */\n"
            "  text-align: center; /* You can use 'left', 'center', or 'right' */\n"
            "  \n"
            "  /* Add some additional styling if needed */\n"
            "  /* Example box shadow effect */\n"
            "}\n"
            ""
        )

        self.horizontalLayout.addWidget(self.frame_top)

        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName("Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.frame_top_menus.setEnabled(True)
        self.frame_top_menus.setLayoutDirection(Qt.LeftToRight)
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName("btn_page_1")
        self.btn_page_1.setMinimumSize(QSize(0, 40))
        self.btn_page_1.setStyleSheet(
            "QPushButton {\n"
            "	color: rgb(255, 255, 255);\n"
            "	background-color: rgb(35, 35, 35);\n"
            "	border: 0px solid;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:focus{\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}"
        )

        self.verticalLayout_4.addWidget(self.btn_page_1)

        self.pushButton_4 = QPushButton(self.frame_top_menus)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 40))
        self.pushButton_4.setStyleSheet(
            "QPushButton {\n"
            "	color: rgb(255, 255, 255);\n"
            "	background-color: rgb(35, 35, 35);\n"
            "	border: 0px solid;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:focus{\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}"
        )

        self.verticalLayout_4.addWidget(self.pushButton_4)

        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName("btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 40))
        self.btn_page_2.setStyleSheet(
            "QPushButton {\n"
            "	color: rgb(255, 255, 255);\n"
            "	background-color: rgb(35, 35, 35);\n"
            "	border: 0px solid;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:focus{\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}"
        )

        self.verticalLayout_4.addWidget(self.btn_page_2)

        self.pushButton_11 = QPushButton(self.frame_top_menus)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(0, 40))
        self.pushButton_11.setStyleSheet(
            "QPushButton {\n"
            "	color: rgb(255, 255, 255);\n"
            "	background-color: rgb(35, 35, 35);\n"
            "	border: 0px solid;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:focus{\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}"
        )

        self.verticalLayout_4.addWidget(self.pushButton_11)

        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName("btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 40))
        self.btn_page_3.setStyleSheet(
            "QPushButton {\n"
            "	color: rgb(255, 255, 255);\n"
            "	background-color: rgb(35, 35, 35);\n"
            "	border: 0px solid;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:focus{\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}"
        )

        self.verticalLayout_4.addWidget(self.btn_page_3)

        self.pushButton_2 = QPushButton(self.frame_top_menus)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 40))
        self.pushButton_2.setStyleSheet(
            "QPushButton {\n"
            "	color: rgb(255, 255, 255);\n"
            "	background-color: rgb(35, 35, 35);\n"
            "	border: 0px solid;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:focus{\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}"
        )

        self.verticalLayout_4.addWidget(self.pushButton_2)

        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)

        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName("frame_pages")
        self.frame_pages.setStyleSheet("background-color: rgb(37, 39, 48);")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame = QFrame(self.page_1)
        self.frame.setObjectName("frame")
        self.frame.setEnabled(True)
        font1 = QFont()
        font1.setPointSize(1)
        self.frame.setFont(font1)
        self.frame.setStyleSheet("background-color: rgb(37, 39, 48);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setGeometry(QRect(120, 70, 41, 31))
        font2 = QFont()
        font2.setFamily("Segoe UI")
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(
            "QLineEdit {\n"
            "  border: 2px solid  rgb(190,190,190); \n"
            "  border-radius: 10px;  \n"
            "  color : #FFF;\n"
            "  padding-left : 12px;\n"
            "  padding-right : 10px;\n"
            "	background-color: rgb(34, 36, 44);\n"
            "}\n"
            "QLineEdit:hover{\n"
            "border : 2px solid  rgb(48,50,62);\n"
            "}\n"
            "QLineEdit:focus{\n"
            "border : 2px solid  rgb(85,170,255);\n"
            "}"
        )
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(20, 60, 81, 51))
        font3 = QFont()
        font3.setFamily("Segoe UI Symbol")
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(100, 40, 21, 81))
        font4 = QFont()
        font4.setFamily("Segoe UI Symbol")
        font4.setPointSize(21)
        font4.setBold(False)
        font4.setWeight(50)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(170, 70, 16, 31))
        font5 = QFont()
        font5.setFamily("Segoe UI Symbol")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(180, 70, 41, 31))
        self.lineEdit_2.setStyleSheet(
            "QLineEdit {\n"
            "  border: 2px solid  rgb(190,190,190); \n"
            "  border-radius: 10px;  \n"
            "  color : #FFF;\n"
            "  padding-left : 12px;\n"
            "  padding-right : 10px;\n"
            "	background-color: rgb(34, 36, 44);\n"
            "}\n"
            "QLineEdit:hover{\n"
            "border : 2px solid  rgb(48,50,62);\n"
            "}\n"
            "QLineEdit:focus{\n"
            "border : 2px solid  rgb(85,170,255);\n"
            "}"
        )
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.label_6.setGeometry(QRect(230, 60, 21, 41))
        font6 = QFont()
        font6.setFamily("Segoe UI Semibold")
        font6.setPointSize(21)
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.label_7.setGeometry(QRect(460, 40, 21, 81))
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName("label_8")
        self.label_8.setGeometry(QRect(590, 60, 21, 41))
        self.label_8.setFont(font6)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(540, 70, 41, 31))
        self.lineEdit_3.setStyleSheet(
            "QLineEdit {\n"
            "  border: 2px solid  rgb(190,190,190); \n"
            "  border-radius: 10px;  \n"
            "  color : #FFF;\n"
            "  padding-left : 12px;\n"
            "  padding-right : 10px;\n"
            "	background-color: rgb(34, 36, 44);\n"
            "}\n"
            "QLineEdit:hover{\n"
            "border : 2px solid  rgb(48,50,62);\n"
            "}\n"
            "QLineEdit:focus{\n"
            "border : 2px solid  rgb(85,170,255);\n"
            "}"
        )
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName("label_9")
        self.label_9.setGeometry(QRect(380, 60, 81, 51))
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(480, 70, 41, 31))
        self.lineEdit_4.setFont(font2)
        self.lineEdit_4.setStyleSheet(
            "QLineEdit {\n"
            "  border: 2px solid  rgb(190,190,190); \n"
            "  border-radius: 10px;  \n"
            "  color : #FFF;\n"
            "  padding-left : 12px;\n"
            "  padding-right : 10px;\n"
            "	background-color: rgb(34, 36, 44);\n"
            "}\n"
            "QLineEdit:hover{\n"
            "border : 2px solid  rgb(48,50,62);\n"
            "}\n"
            "QLineEdit:focus{\n"
            "border : 2px solid  rgb(85,170,255);\n"
            
            "}"
        )
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName("label_10")
        self.label_10.setGeometry(QRect(530, 70, 16, 31))
        self.label_10.setFont(font5)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QRect(720, 190, 121, 31))
        font7 = QFont()
        font7.setBold(True)
        font7.setWeight(75)
        self.pushButton.setFont(font7)
        self.pushButton.setStyleSheet(
            "QPushButton{\n"
            "border-radius: 10px;\n"
            "border-right: 1px solid #aaaaaa; \n"
            "}\n"
            "QPushButton:enabled {\n"
            "background-color: rgb(85, 170, 255);\n"
            "color: white;\n"
            "}\n"
            "QPushButton:pressed {\n"
            " \n"
            "	background-color: rgb(37, 39, 48);\n"
            "color: #fffffe;\n"
            "}\n"
            "QPushButton :hover {\n"
            "	background-color: rgb(255, 255, 255);\n"
            " color: #0c2f70;\n"
            "}\n"
            "QPushButton:disabled {\n"
            "background-color: #aaaaaa;\n"
            "color: #ffffff;\n"
            "}"
        )
        self.radioButton = QRadioButton(self.frame)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setGeometry(QRect(710, 10, 71, 41))
        self.radioButton.setAutoFillBackground(False)
        self.radioButton.setStyleSheet(
            "/* Apply styles to the QRadioButton class */\n"
            "QRadioButton {\n"
            "  /* Set font properties */\n"
            "  font-family: 'Helvetica', sans-serif;\n"
            "  font-size: 14px;\n"
            "  \n"
            "  /* Set text color */\n"
            "  color: #ffffff; /* You can use your preferred text color */\n"
            "  \n"
            "  /* Set background color */\n"
            "  background-color: rgb(37, 39, 48); /* Your specified background color */\n"
            "  \n"
            "  /* Set padding and margin */\n"
            "  padding: 8px;\n"
            "  margin: 5px;\n"
            "  \n"
            "  /* Set border properties */\n"
            "  border: 2px solid #2c3e50; /* Border color */\n"
            "  border-radius: 5px; /* Border radius for rounded corners */\n"
            "  \n"
            "  /* Add some additional styling if needed */\n"
            "  /* Example box shadow effect */\n"
            "\n"
            "}\n"
            "\n"
            "/* Apply styles when the QRadioButton is checked */\n"
            "QRadioButton:checked {\n"
            "  background-color: #2c3e50; /* Change background color when checked */\n"
            "  border-color: #1a252f; /* Change border color when checked */\n"
            "  color: #ffffff; "
            "/* Change text color when checked */\n"
            "}\n"
            ""
        )
        self.radioButton.setChecked(True)
        self.radioButton_2 = QRadioButton(self.frame)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setGeometry(QRect(780, 10, 71, 41))
        self.radioButton_2.setStyleSheet(
            "/* Apply styles to the QRadioButton class */\n"
            "QRadioButton {\n"
            "  /* Set font properties */\n"
            "  font-family: 'Helvetica', sans-serif;\n"
            "  font-size: 14px;\n"
            "  \n"
            "  /* Set text color */\n"
            "  color: #ffffff; /* You can use your preferred text color */\n"
            "  \n"
            "  /* Set background color */\n"
            "  background-color: rgb(37, 39, 48); /* Your specified background color */\n"
            "  \n"
            "  /* Set padding and margin */\n"
            "  padding: 8px;\n"
            "  margin: 5px;\n"
            "  \n"
            "  /* Set border properties */\n"
            "  border: 2px solid #2c3e50; /* Border color */\n"
            "  border-radius: 5px; /* Border radius for rounded corners */\n"
            "  \n"
            "  /* Add some additional styling if needed */\n"
            "  /* Example box shadow effect */\n"
            "\n"
            "}\n"
            "\n"
            "/* Apply styles when the QRadioButton is checked */\n"
            "QRadioButton:checked {\n"
            "  background-color: #2c3e50; /* Change background color when checked */\n"
            "  border-color: #1a252f; /* Change border color when checked */\n"
            "  color: #ffffff; "
            "/* Change text color when checked */\n"
            "}"
        )
        self.lineEdit_5 = QLineEdit(self.frame)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(240, 70, 41, 31))
        self.lineEdit_5.setVisible(False)
        self.lineEdit_5.setStyleSheet(
            "QLineEdit {\n"
            "  border: 2px solid  rgb(190,190,190); \n"
            "  border-radius: 10px;  \n"
            "  color : #FFF;\n"
            "  padding-left : 12px;\n"
            "  padding-right : 10px;\n"
            "	background-color: rgb(34, 36, 44);\n"
            "}\n"
            "QLineEdit:hover{\n"
            "border : 2px solid  rgb(48,50,62);\n"
            "}\n"
            "QLineEdit:focus{\n"
            "border : 2px solid  rgb(85,170,255);\n"
            "}"
        )
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName("label_12")
        self.label_12.setEnabled(True)
        self.label_12.setGeometry(QRect(290, 60, 21, 41))
        self.label_12.setFont(font6)
        self.label_12.setVisible(False)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName("label_13")
        self.label_13.setGeometry(QRect(230, 70, 16, 31))
        self.label_13.setFont(font5)
        self.label_13.setVisible(False)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName("label_15")
        self.label_15.setEnabled(True)
        self.label_15.setGeometry(QRect(650, 60, 21, 41))
        self.label_15.setFont(font6)
        self.label_15.setVisible(False)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_6 = QLineEdit(self.frame)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(600, 70, 41, 31))
        self.lineEdit_6.setVisible(False)
        self.lineEdit_6.setStyleSheet(
            "QLineEdit {\n"
            "  border: 2px solid  rgb(190,190,190); \n"
            "  border-radius: 10px;  \n"
            "  color : #FFF;\n"
            "  padding-left : 12px;\n"
            "  padding-right : 10px;\n"
            "	background-color: rgb(34, 36, 44);\n"
            "}\n"
            "QLineEdit:hover{\n"
            "border : 2px solid  rgb(48,50,62);\n"
            "}\n"
            "QLineEdit:focus{\n"
            "border : 2px solid  rgb(85,170,255);\n"
            "}"
        )
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName("label_14")
        self.label_14.setGeometry(QRect(590, 70, 16, 31))
        self.label_14.setFont(font5)
        self.label_14.setVisible(False)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_7 = QLineEdit(self.frame)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(720, 130, 121, 31))
        self.lineEdit_7.setAutoFillBackground(False)
        self.lineEdit_7.setStyleSheet(
            "QLineEdit {\n"
            "  border: 2px solid  rgb(190,190,190); \n"
            "  border-radius: 10px;  \n"
            "  color : #FFF;\n"
            "  padding-left : 12px;\n"
            "  padding-right : 10px;\n"
            "	background-color: rgb(34, 36, 44);\n"
            "}\n"
            "QLineEdit:hover{\n"
            "border : 2px solid  rgb(48,50,62);\n"
            "}\n"
            "QLineEdit:focus{\n"
            "border : 2px solid  rgb(85,170,255);\n"
            "}"
        )
        self.lineEdit_7.setReadOnly(True)
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName("label_16")
        self.label_16.setGeometry(QRect(10, 0, 171, 71))
        self.label_16.setFont(font)
        self.label_16.setToolTipDuration(-1)
        self.label_16.setStyleSheet(
            "/* Apply styles to the QLabel class for a UI design title */\n"
            "QLabel {\n"
            "  /* Set font properties */\n"
            "  font-family: 'Helvetica', sans-serif;\n"
            "  font-size: 24px;\n"
            "  font-weight: bold;\n"
            "  \n"
            "  /* Set text color */\n"
            "   /* You can use your preferred text color */\n"
            "	color: rgb(85, 170, 255);\n"
            "  \n"
            "  /* Set padding and margin */\n"
            "  padding: 1px;\n"
            "  margin: 1px 0;\n"
            "  \n"
            "  /* Set background color */\n"
            "   /* Your specified background color */\n"
            "\n"
            "  /* Set text alignment */\n"
            "  text-align: center; /* You can use 'left', 'center', or 'right' */\n"
            "  \n"
            "  /* Add some additional styling if needed */\n"
            "  /* Example box shadow effect */\n"
            "}\n"
            ""
        )
        self.widget = QWidget(self.frame)
        self.widget.setObjectName("widget")
        self.widget.setGeometry(QRect(30, 140, 601, 361))
        self.widget.setStyleSheet("border-radius : 12px;""background-color: white;\n")
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName("label_17")
        self.label_17.setGeometry(QRect(20, 130, 621, 381))
        self.label_17.setStyleSheet(
            "background-color: rgb(85, 170, 255);\n" "border-radius : 15px;"
        )
        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setGeometry(QRect(720, 70, 121, 31))
        font8 = QFont()
        font8.setFamily("Segoe UI Semilight")
        font8.setPointSize(8)
        font8.setBold(True)
        font8.setWeight(75)
        self.comboBox.setFont(font8)
        self.comboBox.setStyleSheet(
            "QComboBox {\n"
            "    \n"
            "	background-color: rgb(85, 170, 255);\n"
            "    border-radius: 10px;\n"
            "    color: white;\n"
            "    padding-left: 6px;\n"
            "}\n"
            "\n"
            "QComboBox:editable {\n"
            "    \n"
            "}\n"
            "\n"
            "QComboBox::drop-down {\n"
            "    border: none;\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView {\n"
            "    background-color: rgb(85, 170, 255);\n"
            "    color: white;\n"
            "      /* Change selection background color if needed */\n"
            "    border-radius:10px;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow {\n"
            "    /* Replace placeholder_url with the actual image URL */\n"
            "    image: url(:/icons/Downloads/icons8-chevron-down-30.png);\n"
            "    width: 20px;  /* Adjust the width to your desired size */\n"
            "    height: 16px;  /* Adjust the height to your desired size */\n"
            "    margin-right: 25px;\n"
            "    margin-top: 3px;\n"
            "    \n"
            "}\n"
            "\n"
            "QComboBox:down-arrow:on {\n"
            "       \n"
            "	image: url(:/icons/Downloads/icons8-chevron-up-30.png);\n"
            "    width: 20px;  /* Adjust the width to your desired size */\n"
            "    height: 16px;  /* Adjust t"
            "he height to your desired size */\n"
            "    margin-right: 25px;\n"
            "    margin-top: 3px;\n"
            "    \n"
            "\n"
            "}\n"
            ""
        )
        self.comboBox.setEditable(False)
        self.comboBox.setInsertPolicy(QComboBox.NoInsert)
        self.lineEdit_8 = QLineEdit(self.frame)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(790, 260, 41, 31))
        self.lineEdit_8.setStyleSheet(
            "QLineEdit {\n"
            "  border: 2px solid  rgb(190,190,190); \n"
            "  border-radius: 10px;  \n"
            "  color : #FFF;\n"
            "  padding-left : 12px;\n"
            "  padding-right : 10px;\n"
            "	background-color: rgb(34, 36, 44);\n"
            "}\n"
            "QLineEdit:hover{\n"
            "border : 2px solid  rgb(48,50,62);\n"
            "}\n"
            "QLineEdit:focus{\n"
            "border : 2px solid  rgb(85,170,255);\n"
            "}"
        )
        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName("label_18")
        self.label_18.setGeometry(QRect(720, 250, 71, 51))
        font9 = QFont()
        font9.setFamily("Segoe UI Symbol")
        font9.setPointSize(8)
        font9.setBold(True)
        font9.setItalic(False)
        font9.setWeight(75)
        self.label_18.setFont(font9)
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setGeometry(QRect(720, 470, 121, 31))
        self.pushButton_3.setFont(font7)
        self.pushButton_3.setStyleSheet(
            "QPushButton{\n"
            "border-radius: 10px;\n"
            "border-right: 1px solid #aaaaaa; \n"
            "}\n"
            "QPushButton:enabled {\n"
            "background-color: rgb(85, 170, 255);\n"
            "color: white;\n"
            "}\n"
            "QPushButton:pressed {\n"
            " \n"
            "	background-color: rgb(37, 39, 48);\n"
            "color: #fffffe;\n"
            "}\n"
            "QPushButton :hover {\n"
            "	background-color: rgb(255, 255, 255);\n"
            " color: #0c2f70;\n"
            "}\n"
            "QPushButton:disabled {\n"
            "background-color: #aaaaaa;\n"
            "color: #ffffff;\n"
            "}"
        )
        self.lineEdit.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.lineEdit_2.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.lineEdit_4.raise_()
        self.label_10.raise_()
        self.lineEdit_3.raise_()
        self.pushButton.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.lineEdit_5.raise_()
        self.label_15.raise_()
        self.label_14.raise_()
        self.lineEdit_6.raise_()
        self.lineEdit_7.raise_()
        self.widget.raise_()
        self.comboBox.raise_()
        self.lineEdit_8.raise_()
        self.label_18.raise_()
        self.label_16.raise_()
        self.pushButton_3.raise_()

        self.verticalLayout_7.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setEnabled(True)
        self.frame_2.setFont(font1)
        self.frame_2.setStyleSheet("background-color: rgb(37, 39, 48);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName("label_19")
        self.label_19.setGeometry(QRect(90, 40, 21, 81))
        self.label_19.setFont(font4)
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_10 = QLineEdit(self.frame_2)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(490, 70, 51, 31))
        self.lineEdit_10.setAutoFillBackground(False)
        self.lineEdit_10.setStyleSheet(
            "QLineEdit {\n"
            "  border: 2px solid  rgb(190,190,190); \n"
            "  border-radius: 10px;  \n"
            "  color : #FFF;\n"
            "  padding-left : 12px;\n"
            "  padding-right : 10px;\n"
            "	background-color: rgb(34, 36, 44);\n"
            "}\n"
            "QLineEdit:hover{\n"
            "border : 2px solid  rgb(48,50,62);\n"
            "}\n"
            "QLineEdit:focus{\n"
            "border : 2px solid  rgb(85,170,255);\n"
            "}"
        )
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_11 = QLineEdit(self.frame_2)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(110, 70, 41, 31))
        self.lineEdit_11.setFont(font2)
        self.lineEdit_11.setStyleSheet(
            "QLineEdit {\n"
            "  border: 2px solid  rgb(190,190,190); \n"
            "  border-radius: 10px;  \n"
            "  color : #FFF;\n"
            "  padding-left : 12px;\n"
            "  padding-right : 10px;\n"
            "	background-color: rgb(34, 36, 44);\n"
            "}\n"
            "QLineEdit:hover{\n"
            "border : 2px solid  rgb(48,50,62);\n"
            "}\n"
            "QLineEdit:focus{\n"
            "border : 2px solid  rgb(85,170,255);\n"
            "}"
        )
        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setGeometry(QRect(710, 70, 121, 31))
        self.pushButton_5.setFont(font7)
        self.pushButton_5.setStyleSheet(
            "QPushButton{\n"
            "border-radius: 10px;\n"
            "border-right: 1px solid #aaaaaa; \n"
            "}\n"
            "QPushButton:enabled {\n"
            "background-color: rgb(85, 170, 255);\n"
            "color: white;\n"
            "}\n"
            "QPushButton:pressed {\n"
            " \n"
            "	background-color: rgb(37, 39, 48);\n"
            "color: #fffffe;\n"
            "}\n"
            "QPushButton :hover {\n"
            "	background-color: rgb(255, 255, 255);\n"
            " color: #0c2f70;\n"
            "}\n"
            "QPushButton:disabled {\n"
            "background-color: #aaaaaa;\n"
            "color: #ffffff;\n"
            "}"
        )
        self.lineEdit_12 = QLineEdit(self.frame_2)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(170, 70, 41, 31))
        self.lineEdit_12.setStyleSheet(
            "QLineEdit {\n"
            "  border: 2px solid  rgb(190,190,190); \n"
            "  border-radius: 10px;  \n"
            "  color : #FFF;\n"
            "  padding-left : 12px;\n"
            "  padding-right : 10px;\n"
            "	background-color: rgb(34, 36, 44);\n"
            "}\n"
            "QLineEdit:hover{\n"
            "border : 2px solid  rgb(48,50,62);\n"
            "}\n"
            "QLineEdit:focus{\n"
            "border : 2px solid  rgb(85,170,255);\n"
            "}"
        )
        self.label_20 = QLabel(self.frame_2)
        self.label_20.setObjectName("label_20")
        self.label_20.setGeometry(QRect(20, 60, 71, 51))
        self.label_20.setFont(font3)
        self.label_20.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName("label_21")
        self.label_21.setGeometry(QRect(220, 60, 21, 41))
        self.label_21.setFont(font6)
        self.label_21.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_22 = QLabel(self.frame_2)
        self.label_22.setObjectName("label_22")
        self.label_22.setGeometry(QRect(10, 0, 271, 71))
        self.label_22.setFont(font)
        self.label_22.setStyleSheet(
            "/* Apply styles to the QLabel class for a UI design title */\n"
            "QLabel {\n"
            "  /* Set font properties */\n"
            "  font-family: 'Helvetica', sans-serif;\n"
            "  font-size: 24px;\n"
            "  font-weight: bold;\n"
            "  \n"
            "  /* Set text color */\n"
            "   /* You can use your preferred text color */\n"
            "	color: rgb(85, 170, 255);\n"
            "  \n"
            "  /* Set padding and margin */\n"
            "  padding: 1px;\n"
            "  margin: 1px 0;\n"
            "  \n"
            "  /* Set background color */\n"
            "   /* Your specified background color */\n"
            "\n"
            "  /* Set text alignment */\n"
            "  text-align: center; /* You can use 'left', 'center', or 'right' */\n"
            "  \n"
            "  /* Add some additional styling if needed */\n"
            "  /* Example box shadow effect */\n"
            "}\n"
            ""
        )
        self.label_23 = QLabel(self.frame_2)
        self.label_23.setObjectName("label_23")
        self.label_23.setGeometry(QRect(160, 70, 16, 31))
        self.label_23.setFont(font5)
        self.label_23.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_6 = QPushButton(self.frame_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setGeometry(QRect(710, 160, 121, 31))
        self.pushButton_6.setFont(font7)
        self.pushButton_6.setStyleSheet(
            "QPushButton{\n"
            "border-radius: 10px;\n"
            "border-right: 1px solid #aaaaaa; \n"
            "}\n"
            "QPushButton:enabled {\n"
            "background-color: rgb(85, 170, 255);\n"
            "color: white;\n"
            "}\n"
            "QPushButton:pressed {\n"
            " \n"
            "	background-color: rgb(37, 39, 48);\n"
            "color: #fffffe;\n"
            "}\n"
            "QPushButton :hover {\n"
            "	background-color: rgb(255, 255, 255);\n"
            " color: #0c2f70;\n"
            "}\n"
            "QPushButton:disabled {\n"
            "background-color: #aaaaaa;\n"
            "color: #ffffff;\n"
            "}"
        )
        self.label_24 = QLabel(self.frame_2)
        self.label_24.setObjectName("label_24")
        self.label_24.setGeometry(QRect(240, 60, 241, 51))
        self.label_24.setFont(font3)
        self.label_24.setStyleSheet("color: rgb(255, 255, 255);")
        self.widget_3 = QWidget(self.frame_2)
        self.widget_3.setObjectName("widget_3")
        self.widget_3.setGeometry(QRect(30, 140, 601, 361))
        self.widget_3.setStyleSheet(
            "border-radius : 12px;" "background-color: white;\n"
        )
        self.label_3_6 = QLabel(self.frame_2)
        self.label_3_6.setObjectName("label_3_6")
        self.label_3_6.setGeometry(QRect(20, 130, 621, 381))
        self.label_3_6.setStyleSheet(
            "background-color: rgb(85, 170, 255);\n" "border-radius : 15px;"
        )
        self.label_19.raise_()
        self.lineEdit_10.raise_()
        self.lineEdit_11.raise_()
        self.pushButton_5.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.pushButton_6.raise_()
        self.lineEdit_12.raise_()
        self.label_24.raise_()
        self.label_3_6.raise_()
        self.widget_3.raise_()

        self.verticalLayout_6.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_4 = QFrame(self.page_3)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.setEnabled(True)
        self.frame_4.setFont(font1)
        self.frame_4.setStyleSheet("background-color: rgb(37, 39, 48);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Sunken)
        self.pushButton_7 = QPushButton(self.frame_4)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setGeometry(QRect(710, 70, 121, 31))
        self.pushButton_7.setFont(font7)
        self.pushButton_7.setStyleSheet(
            "QPushButton{\n"
            "border-radius: 10px;\n"
            "border-right: 1px solid #aaaaaa; \n"
            "}\n"
            "QPushButton:enabled {\n"
            "background-color: rgb(85, 170, 255);\n"
            "color: white;\n"
            "}\n"
            "QPushButton:pressed {\n"
            " \n"
            "	background-color: rgb(37, 39, 48);\n"
            "color: #fffffe;\n"
            "}\n"
            "QPushButton :hover {\n"
            "	background-color: rgb(255, 255, 255);\n"
            " color: #0c2f70;\n"
            "}\n"
            "QPushButton:disabled {\n"
            "background-color: #aaaaaa;\n"
            "color: #ffffff;\n"
            "}"
        )
        self.label_25 = QLabel(self.frame_4)
        self.label_25.setObjectName("label_25")
        self.label_25.setGeometry(QRect(10, 0, 301, 61))
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(
            "/* Apply styles to the QLabel class for a UI design title */\n"
            "QLabel {\n"
            "  /* Set font properties */\n"
            "  font-family: 'Helvetica', sans-serif;\n"
            "  font-size: 24px;\n"
            "  font-weight: bold;\n"
            "  \n"
            "  /* Set text color */\n"
            "   /* You can use your preferred text color */\n"
            "	color: rgb(85, 170, 255);\n"
            "  \n"
            "  /* Set padding and margin */\n"
            "  padding: 1px;\n"
            "  margin: 1px 0;\n"
            "  \n"
            "  /* Set background color */\n"
            "   /* Your specified background color */\n"
            "\n"
            "  /* Set text alignment */\n"
            "  text-align: center; /* You can use 'left', 'center', or 'right' */\n"
            "  \n"
            "  /* Add some additional styling if needed */\n"
            "  /* Example box shadow effect */\n"
            "}\n"
            ""
        )
        self.pushButton_8 = QPushButton(self.frame_4)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setGeometry(QRect(710, 160, 121, 31))
        self.pushButton_8.setFont(font7)
        self.pushButton_8.setStyleSheet(
            "QPushButton{\n"
            "border-radius: 10px;\n"
            "border-right: 1px solid #aaaaaa; \n"
            "}\n"
            "QPushButton:enabled {\n"
            "background-color: rgb(85, 170, 255);\n"
            "color: white;\n"
            "}\n"
            "QPushButton:pressed {\n"
            " \n"
            "	background-color: rgb(37, 39, 48);\n"
            "color: #fffffe;\n"
            "}\n"
            "QPushButton :hover {\n"
            "	background-color: rgb(255, 255, 255);\n"
            " color: #0c2f70;\n"
            "}\n"
            "QPushButton:disabled {\n"
            "background-color: #aaaaaa;\n"
            "color: #ffffff;\n"
            "}"
        )
        self.spinBox = QSpinBox(self.frame_4)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setGeometry(QRect(280, 60, 71, 41))
        self.spinBox.setStyleSheet(
            "QSpinBox {\n"
            "                border: 2px solid rgb(85, 170, 255);\n"
            "                border-radius: 4px;\n"
            "                padding: 2px;\n"
            "                background-color: rgb(34, 36, 44);\n"
            "                color: white;\n"
            "                selection-background-color: rgb(85, 170, 255);\n"
            "            }\n"
            "\n"
            "            QSpinBox::up-button, QSpinBox::down-button {\n"
            "                width: 16px;\n"
            "                height: 16px;\n"
            "                background-color: rgb(63, 126, 191);\n"
            "                border: 2px solid rgb(85, 170, 255);\n"
            "                border-radius: 4px;\n"
            "            }\n"
            "\n"
            "            QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
            "                background-color: rgb(85, 170, 255);\n"
            "            }\n"
            "\n"
            "            QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
            "                background-color: rgb(48, 95, 143);\n"
            "            }"
        )
        self.label_26 = QLabel(self.frame_4)
        self.label_26.setObjectName("label_26")
        self.label_26.setGeometry(QRect(20, 60, 251, 51))
        self.label_26.setFont(font)
        self.label_26.setStyleSheet(
            "/* Apply styles to the QLabel class for a UI design title */\n"
            "QLabel {\n"
            "  /* Set font properties */\n"
            "  font-family: 'Helvetica', sans-serif;\n"
            "  font-size: 24px;\n"
            "  font-weight: bold;\n"
            "  \n"
            "  /* Set text color */\n"
            "   /* You can use your preferred text color */\n"
            "	color: rgb(85, 170, 255);\n"
            "  \n"
            "  /* Set padding and margin */\n"
            "  padding: 1px;\n"
            "  margin: 1px 0;\n"
            "  \n"
            "  /* Set background color */\n"
            "   /* Your specified background color */\n"
            "\n"
            "  /* Set text alignment */\n"
            "  text-align: center; /* You can use 'left', 'center', or 'right' */\n"
            "  \n"
            "  /* Add some additional styling if needed */\n"
            "  /* Example box shadow effect */\n"
            "}\n"
            ""
        )
        self.label_27 = QLabel(self.frame_4)
        self.label_27.setObjectName("label_27")
        self.label_27.setGeometry(QRect(370, 50, 251, 71))
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(
            "/* Apply styles to the QLabel class for a UI design title */\n"
            "QLabel {\n"
            "  /* Set font properties */\n"
            "  font-family: 'Helvetica', sans-serif;\n"
            "  font-size: 24px;\n"
            "  font-weight: bold;\n"
            "  \n"
            "  /* Set text color */\n"
            "   /* You can use your preferred text color */\n"
            "	color: rgb(85, 170, 255);\n"
            "  \n"
            "  /* Set padding and margin */\n"
            "  padding: 10px;\n"
            "  margin: 10px 0;\n"
            "  \n"
            "  /* Set background color */\n"
            "   /* Your specified background color */\n"
            "\n"
            "  /* Set text alignment */\n"
            "  text-align: center; /* You can use 'left', 'center', or 'right' */\n"
            "  \n"
            "  /* Add some additional styling if needed */\n"
            "  /* Example box shadow effect */\n"
            
            "}\n"
            ""
        )
        self.label_28 = QLabel(self.frame_4)
        self.label_28.setObjectName("label_28")
        self.label_28.setGeometry(QRect(20, 130, 621, 381))
        self.label_28.setStyleSheet(
            "background-color: rgb(85, 170, 255);\n" "border-radius : 15px;"
        )
        self.widget_4 = QWidget(self.frame_4)
        self.widget_4.setObjectName("widget_4")
        self.widget_4.setGeometry(QRect(30, 140, 601, 361))
        self.widget_4.setStyleSheet(
            "border-radius : 12px;" "background-color: white;\n"
        )

        self.verticalLayout_8.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_9 = QVBoxLayout(self.page_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_5 = QFrame(self.page_4)
        self.frame_5.setObjectName("frame_5")
        self.frame_5.setEnabled(True)
        self.frame_5.setFont(font1)
        self.frame_5.setStyleSheet("background-color: rgb(37, 39, 48);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Sunken)
        self.label_29 = QLabel(self.frame_5)
        self.label_29.setObjectName("label_29")
        self.label_29.setGeometry(QRect(10, 0, 251, 71))
        self.label_29.setFont(font)
        self.label_29.setStyleSheet(
            "/* Apply styles to the QLabel class for a UI design title */\n"
            "QLabel {\n"
            "  /* Set font properties */\n"
            "  font-family: 'Helvetica', sans-serif;\n"
            "  font-size: 24px;\n"
            "  font-weight: bold;\n"
            "  \n"
            "  /* Set text color */\n"
            "   /* You can use your preferred text color */\n"
            "	color: rgb(85, 170, 255);\n"
            "  \n"
            "  /* Set padding and margin */\n"
            "  padding: 1px;\n"
            "  margin: 1px 0;\n"
            "  \n"
            "  /* Set background color */\n"
            "   /* Your specified background color */\n"
            "\n"
            "  /* Set text alignment */\n"
            "  text-align: center; /* You can use 'left', 'center', or 'right' */\n"
            "  \n"
            "  /* Add some additional styling if needed */\n"
            "  /* Example box shadow effect */\n"
           
            "}\n"
            ""
        )
        self.pushButton_9 = QPushButton(self.frame_5)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setGeometry(QRect(710, 70, 121, 31))
        self.pushButton_9.setFont(font7)
        self.pushButton_9.setStyleSheet(
            "QPushButton{\n"
            "border-radius: 10px;\n"
            "border-right: 1px solid #aaaaaa; \n"
            "}\n"
            "QPushButton:enabled {\n"
            "background-color: rgb(85, 170, 255);\n"
            "color: white;\n"
            "}\n"
            "QPushButton:pressed {\n"
            " \n"
            "	background-color: rgb(37, 39, 48);\n"
            "color: #fffffe;\n"
            "}\n"
            "QPushButton :hover {\n"
            "	background-color: rgb(255, 255, 255);\n"
            " color: #0c2f70;\n"
            "}\n"
            "QPushButton:disabled {\n"
            "background-color: #aaaaaa;\n"
            "color: #ffffff;\n"
            "}"
        )
        self.pushButton_10 = QPushButton(self.frame_5)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setGeometry(QRect(710, 160, 121, 31))
        self.pushButton_10.setFont(font7)
        self.pushButton_10.setStyleSheet(
            "QPushButton{\n"
            "border-radius: 10px;\n"
            "border-right: 1px solid #aaaaaa; \n"
            "}\n"
            "QPushButton:enabled {\n"
            "background-color: rgb(85, 170, 255);\n"
            "color: white;\n"
            "}\n"
            "QPushButton:pressed {\n"
            " \n"
            "	background-color: rgb(37, 39, 48);\n"
            "color: #fffffe;\n"
            "}\n"
            "QPushButton :hover {\n"
            "	background-color: rgb(255, 255, 255);\n"
            " color: #0c2f70;\n"
            "}\n"
            "QPushButton:disabled {\n"
            "background-color: #aaaaaa;\n"
            "color: #ffffff;\n"
            "}"
        )
        self.widget_5 = QWidget(self.frame_5)
        self.widget_5.setObjectName("widget_5")
        self.widget_5.setGeometry(QRect(30, 140, 601, 361))
        self.widget_5.setStyleSheet(
            "border-radius : 12px;" "background-color: white;\n"
        )
        self.label_3_7 = QLabel(self.frame_5)
        self.label_3_7.setObjectName("label_3_7")
        self.label_3_7.setGeometry(QRect(20, 130, 621, 381))
        self.label_3_7.setStyleSheet(
            "background-color: rgb(85, 170, 255);\n" "border-radius : 15px;"
        )
        self.lineEdit_2_6 = QLineEdit(self.frame_5)
        self.lineEdit_2_6.setObjectName("lineEdit_2_6")
        self.lineEdit_2_6.setGeometry(QRect(320, 70, 51, 31))
        self.lineEdit_2_6.setFont(font2)
        self.lineEdit_2_6.setStyleSheet(
            "QLineEdit {\n"
            "  border: 2px solid  rgb(190,190,190); \n"
            "  border-radius: 10px;  \n"
            "  color : #FFF;\n"
            "  padding-left : 12px;\n"
            "  padding-right : 10px;\n"
            "	background-color: rgb(34, 36, 44);\n"
            "}\n"
            "QLineEdit:hover{\n"
            "border : 2px solid  rgb(48,50,62);\n"
            "}\n"
            "QLineEdit:focus{\n"
            "border : 2px solid  rgb(85,170,255);\n"
            "}"
        )
        self.label_30 = QLabel(self.frame_5)
        self.label_30.setObjectName("label_30")
        self.label_30.setGeometry(QRect(10, 50, 311, 71))
        self.label_30.setFont(font)
        self.label_30.setStyleSheet(
            "/* Apply styles to the QLabel class for a UI design title */\n"
            "QLabel {\n"
            "  /* Set font properties */\n"
            "  font-family: 'Helvetica', sans-serif;\n"
            "  font-size: 24px;\n"
            "  font-weight: bold;\n"
            "  \n"
            "  /* Set text color */\n"
            "   /* You can use your preferred text color */\n"
            "	color: rgb(85, 170, 255);\n"
            "  \n"
            "  /* Set padding and margin */\n"
            "  padding: 1px;\n"
            "  margin: 1px 0;\n"
            "  \n"
            "  /* Set background color */\n"
            "   /* Your specified background color */\n"
            "\n"
            "  /* Set text alignment */\n"
            "  text-align: center; /* You can use 'left', 'center', or 'right' */\n"
            "  \n"
            "  /* Add some additional styling if needed */\n"
            "  /* Example box shadow effect */\n"
           
            "}\n"
            ""
        )
        self.lineEdit_2_7 = QLineEdit(self.frame_5)
        self.lineEdit_2_7.setObjectName("lineEdit_2_7")
        self.lineEdit_2_7.setGeometry(QRect(530, 70, 51, 31))
        self.lineEdit_2_7.setFont(font2)
        self.lineEdit_2_7.setStyleSheet(
            "QLineEdit {\n"
            "  border: 2px solid  rgb(190,190,190); \n"
            "  border-radius: 10px;  \n"
            "  color : #FFF;\n"
            "  padding-left : 12px;\n"
            "  padding-right : 10px;\n"
            "	background-color: rgb(34, 36, 44);\n"
            "}\n"
            "QLineEdit:hover{\n"
            "border : 2px solid  rgb(48,50,62);\n"
            "}\n"
            "QLineEdit:focus{\n"
            "border : 2px solid  rgb(85,170,255);\n"
            "}"
        )
        self.label_31 = QLabel(self.frame_5)
        self.label_31.setObjectName("label_31")
        self.label_31.setGeometry(QRect(390, 50, 151, 71))
        self.label_31.setFont(font)
        self.label_31.setStyleSheet(
            "/* Apply styles to the QLabel class for a UI design title */\n"
            "QLabel {\n"
            "  /* Set font properties */\n"
            "  font-family: 'Helvetica', sans-serif;\n"
            "  font-size: 24px;\n"
            "  font-weight: bold;\n"
            "  \n"
            "  /* Set text color */\n"
            "   /* You can use your preferred text color */\n"
            "	color: rgb(85, 170, 255);\n"
            "  \n"
            "  /* Set padding and margin */\n"
            "  padding: 10px;\n"
            "  margin: 10px 0;\n"
            "  \n"
            "  /* Set background color */\n"
            "   /* Your specified background color */\n"
            "\n"
            "  /* Set text alignment */\n"
            "  text-align: center; /* You can use 'left', 'center', or 'right' */\n"
            "  \n"
            "  /* Add some additional styling if needed */\n"
            "  /* Example box shadow effect */\n"
           
            "}\n"
            ""
        )
        self.label_29.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.label_3_7.raise_()
        self.widget_5.raise_()

        self.lineEdit_2_6.raise_()
        self.label_30.raise_()
        self.label_31.raise_()
        self.lineEdit_2_7.raise_()

        self.verticalLayout_9.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_10 = QVBoxLayout(self.page_5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_3 = QFrame(self.page_5)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setEnabled(True)
        self.frame_3.setFont(font1)
        self.frame_3.setStyleSheet("background-color: rgb(37, 39, 48);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Sunken)
        self.lineEdit_2_5 = QLineEdit(self.frame_3)
        self.lineEdit_2_5.setObjectName("lineEdit_2_5")
        self.lineEdit_2_5.setGeometry(QRect(20, 70, 201, 31))
        self.lineEdit_2_5.setFont(font2)
        self.lineEdit_2_5.setStyleSheet(
            "QLineEdit {\n"
            "  border: 2px solid  rgb(190,190,190); \n"
            "  border-radius: 10px;  \n"
            "  color : #FFF;\n"
            "  padding-left : 12px;\n"
            "  padding-right : 10px;\n"
            "	background-color: rgb(34, 36, 44);\n"
            "}\n"
            "QLineEdit:hover{\n"
            "border : 2px solid  rgb(48,50,62);\n"
            "}\n"
            "QLineEdit:focus{\n"
            "border : 2px solid  rgb(85,170,255);\n"
            "}"
        )
        self.pushButton_4_5 = QPushButton(self.frame_3)
        self.pushButton_4_5.setObjectName("pushButton_4_5")
        self.pushButton_4_5.setGeometry(QRect(730, 70, 121, 31))
        self.pushButton_4_5.setFont(font7)
        self.pushButton_4_5.setStyleSheet(
            "QPushButton{\n"
            "border-radius: 10px;\n"
            "border-right: 1px solid #aaaaaa; \n"
            "}\n"
            "QPushButton:enabled {\n"
            "background-color: rgb(85, 170, 255);\n"
            "color: white;\n"
            "}\n"
            "QPushButton:pressed {\n"
            " \n"
            "	background-color: rgb(37, 39, 48);\n"
            "color: #fffffe;\n"
            "}\n"
            "QPushButton :hover {\n"
            "	background-color: rgb(255, 255, 255);\n"
            " color: #0c2f70;\n"
            "}\n"
            "QPushButton:disabled {\n"
            "background-color: #aaaaaa;\n"
            "color: #ffffff;\n"
            "}"
        )
        self.lineEdit_1_5 = QLineEdit(self.frame_3)
        self.lineEdit_1_5.setObjectName("lineEdit_1_5")
        self.lineEdit_1_5.setGeometry(QRect(260, 70, 201, 31))
        self.lineEdit_1_5.setStyleSheet(
            "QLineEdit {\n"
            "  border: 2px solid  rgb(190,190,190); \n"
            "  border-radius: 10px;  \n"
            "  color : #FFF;\n"
            "  padding-left : 12px;\n"
            "  padding-right : 10px;\n"
            "	background-color: rgb(34, 36, 44);\n"
            "}\n"
            "QLineEdit:hover{\n"
            "border : 2px solid  rgb(48,50,62);\n"
            "}\n"
            "QLineEdit:focus{\n"
            "border : 2px solid  rgb(85,170,255);\n"
            "}"
        )
        self.label_1_5 = QLabel(self.frame_3)
        self.label_1_5.setObjectName("label_1_5")
        self.label_1_5.setGeometry(QRect(10, 0, 301, 71))
        self.label_1_5.setFont(font)
        self.label_1_5.setStyleSheet(
            "/* Apply styles to the QLabel class for a UI design title */\n"
            "QLabel {\n"
            "  /* Set font properties */\n"
            "  font-family: 'Helvetica', sans-serif;\n"
            "  font-size: 24px;\n"
            "  font-weight: bold;\n"
            "  \n"
            "  /* Set text color */\n"
            "   /* You can use your preferred text color */\n"
            "	color: rgb(85, 170, 255);\n"
            "  \n"
            "  /* Set padding and margin */\n"
            "  padding: 1px;\n"
            "  margin: 1px 0;\n"
            "  \n"
            "  /* Set background color */\n"
            "   /* Your specified background color */\n"
            "\n"
            "  /* Set text alignment */\n"
            "  text-align: center; /* You can use 'left', 'center', or 'right' */\n"
            "  \n"
            "  /* Add some additional styling if needed */\n"
            "  /* Example box shadow effect */\n"
           
            "}\n"
            ""
        )
        self.lineEdit_9 = QLineEdit(self.frame_3)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(730, 120, 121, 31))
        self.lineEdit_9.setAutoFillBackground(False)
        self.lineEdit_9.setStyleSheet(
            "QLineEdit {\n"
            "  border: 2px solid  rgb(190,190,190); \n"
            "  border-radius: 10px;  \n"
            "  color : #FFF;\n"
            "  padding-left : 12px;\n"
            "  padding-right : 10px;\n"
            "	background-color: rgb(34, 36, 44);\n"
            "}\n"
            "QLineEdit:hover{\n"
            "border : 2px solid  rgb(48,50,62);\n"
            "}\n"
            "QLineEdit:focus{\n"
            "border : 2px solid  rgb(85,170,255);\n"
            "}"
        )
        self.lineEdit_9.setReadOnly(True)
        self.label_3_5 = QLabel(self.frame_3)
        self.label_3_5.setObjectName("label_3_5")
        self.label_3_5.setGeometry(QRect(20, 130, 621, 381))
        self.label_3_5.setStyleSheet(
            "background-color: rgb(85, 170, 255);\n" "border-radius : 15px;"
        )
        self.widget_2 = QWidget(self.frame_3)
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setGeometry(QRect(30, 140, 601, 361))
        self.widget_2.setStyleSheet(
            "border-radius : 12px;" "background-color: white;\n"
        )

        self.verticalLayout_10.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName("page_6")
        self.verticalLayout_20 = QVBoxLayout(self.page_6)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.frame_6 = QFrame(self.page_6)
        self.frame_6.setObjectName("frame_6")
        self.frame_6.setEnabled(True)
        self.frame_6.setFont(font1)
        self.frame_6.setStyleSheet("background-color: rgb(37, 39, 48);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Sunken)
        self.pushButton_4_6 = QPushButton(self.frame_6)
        self.pushButton_4_6.setObjectName("pushButton_4_6")
        self.pushButton_4_6.setGeometry(QRect(730, 70, 121, 31))
        self.pushButton_4_6.setFont(font7)
        self.pushButton_4_6.setStyleSheet(
            "QPushButton{\n"
            "border-radius: 10px;\n"
            "border-right: 1px solid #aaaaaa; \n"
            "}\n"
            "QPushButton:enabled {\n"
            "background-color: rgb(85, 170, 255);\n"
            "color: white;\n"
            "}\n"
            "QPushButton:pressed {\n"
            " \n"
            "	background-color: rgb(37, 39, 48);\n"
            "color: #fffffe;\n"
            "}\n"
            "QPushButton :hover {\n"
            "	background-color: rgb(255, 255, 255);\n"
            " color: #0c2f70;\n"
            "}\n"
            "QPushButton:disabled {\n"
            "background-color: #aaaaaa;\n"
            "color: #ffffff;\n"
            "}"
        )

        self.label_1_6 = QLabel(self.frame_6)
        self.label_1_6.setObjectName("label_1_6")
        self.label_1_6.setGeometry(QRect(10, 0, 301, 71))
        self.label_1_6.setFont(font)
        self.label_1_6.setStyleSheet(
            "/* Apply styles to the QLabel class for a UI design title */\n"
            "QLabel {\n"
            "  /* Set font properties */\n"
            "  font-family: 'Helvetica', sans-serif;\n"
            "  font-size: 24px;\n"
            "  font-weight: bold;\n"
            "  \n"
            "  /* Set text color */\n"
            "   /* You can use your preferred text color */\n"
            "	color: rgb(85, 170, 255);\n"
            "  \n"
            "  /* Set padding and margin */\n"
            "  padding: 1px;\n"
            "  margin: 1px 0;\n"
            "  \n"
            "  /* Set background color */\n"
            "   /* Your specified background color */\n"
            "\n"
            "  /* Set text alignment */\n"
            "  text-align: center; /* You can use 'left', 'center', or 'right' */\n"
            "  \n"
            "  /* Add some additional styling if needed */\n"
            "  /* Example box shadow effect */\n"
            
            "}\n"
            ""
        )

        self.label_3_61 = QLabel(self.frame_6)
        self.label_3_61.setObjectName("label_3_61")
        self.label_3_61.setGeometry(QRect(20, 130, 621, 381))
        self.label_3_61.setStyleSheet(
            "background-color: rgb(85, 170, 255);\n" "border-radius : 15px;"
        )
        self.widget_7 = QWidget(self.frame_6)
        self.widget_7.setObjectName("widget_7")
        self.widget_7.setGeometry(QRect(30, 140, 601, 361))
        self.widget_7.setStyleSheet(
            "background-color: white;\n" "border-radius : 12px;"
        )
        self.label = QLabel(self.frame_6)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(10, 70, 511, 31))
        self.label.setStyleSheet(
            "/* Apply styles to the QLabel class for a UI design title */\n"
            "QLabel {\n"
            "  /* Set font properties */\n"
            "  font-family: 'Helvetica', sans-serif;\n"
            "  font-size: 24px;\n"
            "  font-weight: bold;\n"
            "  \n"
            "  /* Set text color */\n"
            "   /* You can use your preferred text color */\n"
            "	color: rgb(85, 170, 255);\n"
            "  \n"
            "  /* Set padding and margin */\n"
            "  padding: 1px;\n"
            "  margin: 1px 0;\n"
            "  \n"
            "  /* Set background color */\n"
            "   /* Your specified background color */\n"
            "\n"
            "  /* Set text alignment */\n"
            "  text-align: center; /* You can use 'left', 'center', or 'right' */\n"
            "  \n"
            "  /* Add some additional styling if needed */\n"
            "  /* Example box shadow effect */\n"
          
            "}\n"
            ""
        )

        self.verticalLayout_20.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.page_6)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.horizontalLayout_2.addWidget(self.frame_pages)

        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)

        self.fig_2d, self.ax_2d = plt.subplots()
        self.canvas_2d = FigureCanvas(self.fig_2d)

        # Create a 3D Matplotlib figure and axis
        self.fig_3d = plt.figure(figsize=(8, 6))
        self.ax_3d = self.fig_3d.add_subplot(111, projection="3d")
        self.canvas_3d = FigureCanvas(self.fig_3d)

        # Embed Matplotlib canvas in the widget
        layout = QVBoxLayout(self.widget)
        layout.addWidget(self.canvas_2d)
        self.current_canvas = self.canvas_2d

        self.dataset_size = 20
        np.random.seed(42)  # For reproducibility
        self.dataset = np.random.randint(0, 20, size=(self.dataset_size, 2)).tolist()
        self.labels = [
            "A" if np.random.rand() > 0.5 else "B" for _ in range(self.dataset_size)
        ]
        self.dataset = [
            (*point, label) for point, label in zip(self.dataset, self.labels)
        ]

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", "Menu", None))
        self.label_11.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" color:#e3e3e3;">Simulation</span> OF MACHINE LEARNING ALGORITHME  </p></body></html>',
                None,
            )
        )
        self.btn_page_1.setText(
            QCoreApplication.translate("MainWindow", "Distance", None)
        )
        self.pushButton_4.setText(
            QCoreApplication.translate("MainWindow", "Hamming", None)
        )
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", "K-N-N", None))
        self.pushButton_11.setText(
            QCoreApplication.translate("MainWindow", "Metrics", None)
        )
        self.btn_page_3.setText(
            QCoreApplication.translate("MainWindow", "K-means", None)
        )
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", "SVM", None))
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "X", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", "Point 1 :", None)
        )
        self.label_4.setText(QCoreApplication.translate("MainWindow", "(", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", ",", None))
        self.lineEdit_2.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Y", None)
        )
        self.label_6.setText(QCoreApplication.translate("MainWindow", ")", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", "(", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", ")", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Y", None)
        )
        self.label_9.setText(
            QCoreApplication.translate("MainWindow", " Point 2 :", None)
        )
        self.lineEdit_4.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "X", None)
        )
        self.label_10.setText(QCoreApplication.translate("MainWindow", ",", None))
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", "Calculate", None)
        )
        self.radioButton.setText(QCoreApplication.translate("MainWindow", "2D", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", "3D", None))
        self.lineEdit_5.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Z", None)
        )
        self.label_12.setText(QCoreApplication.translate("MainWindow", ")", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", ",", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", ")", None))
        self.lineEdit_6.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Z", None)
        )
        self.label_14.setText(QCoreApplication.translate("MainWindow", ",", None))
        self.lineEdit_7.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Resultat", None)
        )
        self.label_16.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p>DISTANCE :</p></body></html>", None
            )
        )
        self.label_17.setText("")
        self.comboBox.setItemText(
            0, QCoreApplication.translate("MainWindow", "Euclidien", None)
        )
        self.comboBox.setItemText(
            1, QCoreApplication.translate("MainWindow", "Manhattan", None)
        )
        self.comboBox.setItemText(
            2, QCoreApplication.translate("MainWindow", "Minkowski", None)
        )

        self.comboBox.setCurrentText(
            QCoreApplication.translate("MainWindow", "Euclidien", None)
        )
        self.comboBox.setPlaceholderText("")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "P", None)
        )
        self.label_18.setText(
            QCoreApplication.translate("MainWindow", " Entrer P :", None)
        )
        self.pushButton_3.setText(
            QCoreApplication.translate("MainWindow", "View Graph", None)
        )
        self.label_19.setText(QCoreApplication.translate("MainWindow", "(", None))
        self.lineEdit_10.setPlaceholderText("")
        self.lineEdit_11.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "X", None)
        )
        self.pushButton_5.setText(
            QCoreApplication.translate("MainWindow", "Apply", None)
        )
        self.lineEdit_12.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Y", None)
        )
        self.label_20.setText(
            QCoreApplication.translate("MainWindow", "Point  :", None)
        )
        self.label_21.setText(QCoreApplication.translate("MainWindow", ")", None))
        self.label_22.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" color:#ffffff;">ALGORITHM</span> K-N-N :</p></body></html>',
                None,
            )
        )
        self.label_23.setText(QCoreApplication.translate("MainWindow", ",", None))
        self.pushButton_6.setText(
            QCoreApplication.translate("MainWindow", "View Graph", None)
        )
        self.label_24.setText(
            QCoreApplication.translate(
                "MainWindow", "This Point is near to Group ", None
            )
        )
        self.label_3_6.setText("")
        self.pushButton_7.setText(
            QCoreApplication.translate("MainWindow", "Simulate ", None)
        )
        self.label_25.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" color:#ffffff;">ALGORITHM </span>K-MEANS :</p></body></html>',
                None,
            )
        )
        self.pushButton_8.setText(
            QCoreApplication.translate("MainWindow", "View Graph", None)
        )
        self.label_26.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:10pt; color:#eeeeee;">Choose nymber of Clusters :</span></p></body></html>',
                None,
            )
        )
        self.label_27.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:10pt; color:#ee3131;">Reminder : (Clusters&gt;=2)</span></p></body></html>',
                None,
            )
        )
        self.label_28.setText("")
        self.label_29.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" color:#ffffff;">ALGORITHM </span><span style=" color:#55aaff;">SVM </span>:</p></body></html>',
                None,
            )
        )
        self.pushButton_9.setText(
            QCoreApplication.translate("MainWindow", "Simulate ", None)
        )
        self.pushButton_10.setText(
            QCoreApplication.translate("MainWindow", "View Graph", None)
        )
        self.label_3_7.setText("")
        self.lineEdit_2_6.setPlaceholderText("")
        self.label_30.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:9pt; color:#ebebeb;">Enter the number of points to generate </span></p></body></html>',
                None,
            )
        )
        self.lineEdit_2_7.setPlaceholderText("")
        self.label_31.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:9pt; color:#ebebeb;"> parameter (C)</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_2_5.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Chaine 1", None)
        )
        self.pushButton_4_5.setText(
            QCoreApplication.translate("MainWindow", "Calculate", None)
        )
        self.lineEdit_1_5.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Chaine 2", None)
        )
        self.label_1_5.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>HAMMING <span style=" color:#ffffff;">DISTANCE :</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_9.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Resultat", None)
        )
        self.label_3_5.setText("")
        self.pushButton_4_6.setText(
            QCoreApplication.translate("MainWindow", "Simulate", None)
        )
        self.label_1_6.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" color:#ffffff;">Metrics :</span></p></body></html>',
                None,
            )
        )
        self.label_3_61.setText("")
        self.label.setText(
            QCoreApplication.translate(
                "MainWindow", "Evaluation Metrics for K-N-N Algorithm :", None
            )
        )

    # retranslateUi
    def update_plot2D(self, x1, y1, x2, y2):
        # Calculate Euclidean distance
        distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        distance = round(float(distance), 2)
        # Update the QLineEdit for displaying the distance
        self.lineEdit_7.setText(str(distance))

        # Your 2D plotting logic here
        self.ax_2d.clear()
        self.ax_2d.scatter(
            [x1, x2], [y1, y2], c="blue", marker="o", s=100, label="Points"
        )
        self.ax_2d.text(
            x1, y1, "Point 1", fontsize=12, ha="right", va="bottom", color="black"
        )
        self.ax_2d.text(
            x2, y2, "Point 2", fontsize=12, ha="right", va="bottom", color="black"
        )
        self.ax_2d.plot(
            [x1, x2],
            [y1, y2],
            c="red",
            linestyle="--",
            linewidth=2,
            label=f"Euclidean Distance: {distance:.2f}",
        )
        self.ax_2d.set_title("Euclidean Distance Visualization in 2D")
        self.ax_2d.set_xlabel("X-axis")
        self.ax_2d.set_ylabel("Y-axis")
        self.ax_2d.legend()
        self.canvas_2d.draw()

    def update_plot3D(self, x1, y1, z1, x2, y2, z2):
        # Calculate Euclidean distance
        distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
        distance = round(float(distance), 2)
        # Update the QLineEdit for displaying the distance
        self.lineEdit_7.setText(str(distance))

        # Your 3D plotting logic here
        self.ax_3d.clear()
        self.ax_3d.scatter(
            [x1, x2], [y1, y2], [z1, z2], c="blue", marker="o", s=100, label="Points"
        )
        self.ax_3d.text(
            x1, y1, z1, "Point 1", fontsize=12, ha="right", va="bottom", color="black"
        )
        self.ax_3d.text(
            x2, y2, z2, "Point 2", fontsize=12, ha="right", va="bottom", color="black"
        )
        self.ax_3d.plot(
            [x1, x2],
            [y1, y2],
            [z1, z2],
            c="red",
            linestyle="--",
            linewidth=2,
            label=f"Euclidean Distance: {distance:.2f}",
        )
        self.ax_3d.set_title("Euclidean Distance Visualization in 3D")
        self.ax_3d.set_xlabel("X-axis")
        self.ax_3d.set_ylabel("Y-axis")
        self.ax_3d.set_zlabel("Z-axis")
        self.ax_3d.legend()
        self.canvas_3d.draw()

    def radioButtonToggled(self, checked):
        self.label_12.setHidden(not checked)
        self.label_13.setHidden(not checked)
        self.label_14.setHidden(not checked)
        self.label_15.setHidden(not checked)
        self.lineEdit_5.setHidden(not checked)
        self.lineEdit_6.setHidden(not checked)

    def update_plot2D_Manhatten(self, x1, y1, x2, y2):
        # Calculate Manhattan distance
        distance = np.abs(x2 - x1) + np.abs(y2 - y1)

        # Update the QLineEdit for displaying the distance
        self.lineEdit_7.setText(str(distance))

        # Your 2D plotting logic here
        self.ax_2d.clear()
        self.ax_2d.scatter(
            [x1, x2], [y1, y2], c="blue", marker="o", s=100, label="Points"
        )
        self.ax_2d.text(
            x1, y1, "Point 1", fontsize=12, ha="right", va="bottom", color="black"
        )
        self.ax_2d.text(
            x2, y2, "Point 2", fontsize=12, ha="right", va="bottom", color="black"
        )
        self.ax_2d.plot(
            [x1, x2],
            [y1, y2],
            c="red",
            linestyle="--",
            linewidth=2,
            label=f"Manhattan Distance: {distance:.2f}",
        )
        self.ax_2d.set_title("Minkowski Distance Visualization in 2D")
        self.ax_2d.set_xlabel("X-axis")
        self.ax_2d.set_ylabel("Y-axis")
        self.ax_2d.legend()
        self.canvas_2d.draw()

    def update_plot3D_Manhatten(self, x1, y1, z1, x2, y2, z2):
        # Calculate Manhattan distance
        distance = np.abs(x2 - x1) + np.abs(y2 - y1) + np.abs(z2 - z1)
        distance = int(distance)

        # Update the QLineEdit for displaying the distance
        self.lineEdit_7.setText(str(distance))

        # Your 3D plotting logic here
        self.ax_3d.clear()
        self.ax_3d.scatter(
            [x1, x2], [y1, y2], [z1, z2], c="blue", marker="o", s=100, label="Points"
        )
        self.ax_3d.text(
            x1, y1, z1, "Point 1", fontsize=12, ha="right", va="bottom", color="black"
        )
        self.ax_3d.text(
            x2, y2, z2, "Point 2", fontsize=12, ha="right", va="bottom", color="black"
        )
        self.ax_3d.plot(
            [x1, x2],
            [y1, y2],
            [z1, z2],
            c="red",
            linestyle="--",
            linewidth=2,
            label=f"Manhattan Distance: {distance:.2f}",
        )
        self.ax_3d.set_title("Minkowski Distance Visualization in 3D")
        self.ax_3d.set_xlabel("X-axis")
        self.ax_3d.set_ylabel("Y-axis")
        self.ax_3d.set_zlabel("Z-axis")
        self.ax_3d.legend()
        self.canvas_3d.draw()

    def update_plot2D_Minkowski(self, x1, y1, x2, y2):
        # Calculate Minkowski distance
        distance = abs(x2 - x1) + abs(y2 - y1)

        # Update the QLineEdit for displaying the distance
        self.lineEdit_7.setText(str(round(distance, 2)))

        # Your 2D plotting logic here
        self.ax_2d.clear()
        self.ax_2d.scatter(
            [x1, x2], [y1, y2], c="blue", marker="o", s=100, label="Points"
        )
        self.ax_2d.text(
            x1, y1, "Point 1", fontsize=12, ha="right", va="bottom", color="black"
        )
        self.ax_2d.text(
            x2, y2, "Point 2", fontsize=12, ha="right", va="bottom", color="black"
        )
        self.ax_2d.plot(
            [x1, x2],
            [y1, y2],
            c="red",
            linestyle="--",
            linewidth=2,
            label=f"Manhatten Distance: {distance:.2f}",
        )
        self.ax_2d.set_title(f"Manhatten Distance ")
        self.ax_2d.set_xlabel("X-axis")
        self.ax_2d.set_ylabel("Y-axis")
        self.ax_2d.legend()
        self.canvas_2d.draw()

    def update_plot3D_Minkowski(self, x1, y1, z1, x2, y2, z2):
        # Calculate Minkowski distance
        distance = np.abs(x2 - x1) + np.abs(y2 - y1) + np.abs(z2 - z1)
        distance = round(distance, 2)

        # Update the QLineEdit for displaying the distance
        self.lineEdit_7.setText(str(distance))

        # Your 3D plotting logic here
        self.ax_3d.clear()
        self.ax_3d.scatter(
            [x1, x2], [y1, y2], [z1, z2], c="blue", marker="o", s=100, label="Points"
        )
        self.ax_3d.text(
            x1, y1, z1, "Point 1", fontsize=12, ha="right", va="bottom", color="black"
        )
        self.ax_3d.text(
            x2, y2, z2, "Point 2", fontsize=12, ha="right", va="bottom", color="black"
        )
        self.ax_3d.plot(
            [x1, x2],
            [y1, y2],
            [z1, z2],
            c="red",
            linestyle="--",
            linewidth=2,
            label=f"Manhatten Distance: {distance:.2f}",
        )
        self.ax_3d.set_title(f"Manhatten Distance ")
        self.ax_3d.set_xlabel("X-axis")
        self.ax_3d.set_ylabel("Y-axis")
        self.ax_3d.set_zlabel("Z-axis")
        self.ax_3d.legend()
        self.canvas_3d.draw()

    def display_selected_plot(self):
        method = self.comboBox.currentText()  # Get the selected text from the combo box

        if method == "Euclidien":
            if self.radioButton.isChecked():
                self.lineEdit_7.clear()
                # Show 2D plot
                x1 = int(self.lineEdit.text())
                y1 = int(self.lineEdit_2.text())
                x2 = int(self.lineEdit_4.text())
                y2 = int(self.lineEdit_3.text())
                self.update_plot2D(x1, y1, x2, y2)
                self.show_canvas(self.canvas_2d)
            elif self.radioButton_2.isChecked():
                self.lineEdit_7.clear()
                # Show 3D plot
                x1 = int(self.lineEdit.text())
                y1 = int(self.lineEdit_2.text())
                x2 = int(self.lineEdit_4.text())
                y2 = int(self.lineEdit_3.text())
                if self.lineEdit_5.text() == "" and self.lineEdit_6.text() == "":
                    self.update_plot3D(x1, y1, 0, x2, y2, 0)
                else:
                    z1 = int(self.lineEdit_5.text())
                    z2 = int(self.lineEdit_6.text())
                    self.update_plot3D(x1, y1, z1, x2, y2, z2)
                self.show_canvas(self.canvas_3d)
        elif method == "Minkowski":
            if self.radioButton.isChecked():
                self.lineEdit_7.clear()
                # Show 2D plot
                x1 = int(self.lineEdit.text())
                y1 = int(self.lineEdit_2.text())
                x2 = int(self.lineEdit_4.text())
                y2 = int(self.lineEdit_3.text())
                p = int(self.lineEdit_8.text())
                self.update_plot2D_Manhatten(x1, y1, x2, y2, p)
                self.show_canvas(self.canvas_2d)
            elif self.radioButton_2.isChecked():
                self.lineEdit_7.clear()
                # Show 3D plot
                x1 = int(self.lineEdit.text())
                y1 = int(self.lineEdit_2.text())
                x2 = int(self.lineEdit_4.text())
                y2 = int(self.lineEdit_3.text())

                if self.lineEdit_5.text() == "" and self.lineEdit_6.text() == "":
                    self.update_plot3D_Manhatten(x1, y1, 0, x2, y2, 0, 1)
                else:
                    z1 = int(self.lineEdit_5.text())
                    z2 = int(self.lineEdit_6.text())
                    p = int(self.lineEdit_8.text())
                    self.update_plot3D_Manhatten(x1, y1, z1, x2, y2, z2, p)
                self.show_canvas(self.canvas_3d)
        elif method == "Manhattan":
            if self.radioButton.isChecked():
                self.lineEdit_7.clear()
                # Show 2D plot
                x1 = int(self.lineEdit.text())
                y1 = int(self.lineEdit_2.text())
                x2 = int(self.lineEdit_4.text())
                y2 = int(self.lineEdit_3.text())
                self.update_plot2D_Minkowski(x1, y1, x2, y2)
                self.show_canvas(self.canvas_2d)
            elif self.radioButton_2.isChecked():
                self.lineEdit_7.clear()
                # Show 3D plot
                x1 = int(self.lineEdit.text())
                y1 = int(self.lineEdit_2.text())
                x2 = int(self.lineEdit_4.text())
                y2 = int(self.lineEdit_3.text())
                if self.lineEdit_5.text() == "" and self.lineEdit_6.text() == "":
                    self.update_plot3D_Minkowski(x1, y1, 0, x2, y2, 0)
                else:
                    z1 = int(self.lineEdit_5.text())
                    z2 = int(self.lineEdit_6.text())
                    self.update_plot3D_Minkowski(x1, y1, z1, x2, y2, z2)
                self.show_canvas(self.canvas_3d)

    def show_canvas(self, canvas):
        # Replace the current canvas with the new one in the layout
        if self.current_canvas is not None:
            self.widget.layout().removeWidget(self.current_canvas)
            self.current_canvas.setParent(None)
        self.widget.layout().addWidget(canvas)
        self.current_canvas = canvas

    def update_plot2D_Manhatten(self, x1, y1, x2, y2, p):
        # Calculate Minkowski distance
        distance = (np.abs(x2 - x1) ** p + np.abs(y2 - y1) ** p) ** (1 / p)
        distance = round(distance)
        # Update the QLineEdit for displaying the distance
        self.lineEdit_7.setText(str(round(distance, 2)))

        # Your 2D plotting logic here
        self.ax_2d.clear()
        self.ax_2d.scatter(
            [x1, x2], [y1, y2], c="blue", marker="o", s=100, label="Points"
        )
        self.ax_2d.text(
            x1, y1, "Point 1", fontsize=12, ha="right", va="bottom", color="black"
        )
        self.ax_2d.text(
            x2, y2, "Point 2", fontsize=12, ha="right", va="bottom", color="black"
        )
        self.ax_2d.plot(
            [x1, x2],
            [y1, y2],
            c="red",
            linestyle="--",
            linewidth=2,
            label=f"Minkowski Distance: {distance:.2f}",
        )
        self.ax_2d.set_title(f"Minkowski Distance (p={p}) Visualization in 2D")
        self.ax_2d.set_xlabel("X-axis")
        self.ax_2d.set_ylabel("Y-axis")
        self.ax_2d.legend()
        self.canvas_2d.draw()

    def update_plot3D_Manhatten(self, x1, y1, z1, x2, y2, z2, p):
        # Calculate Minkowski distance
        distance = (
            np.abs(x2 - x1) ** p + np.abs(y2 - y1) ** p + np.abs(z2 - z1) ** p
        ) ** (1 / p)
        distance = round(distance)

        # Update the QLineEdit for displaying the distance
        self.lineEdit_7.setText(str(distance))

        # Your 3D plotting logic here
        self.ax_3d.clear()
        self.ax_3d.scatter(
            [x1, x2], [y1, y2], [z1, z2], c="blue", marker="o", s=100, label="Points"
        )
        self.ax_3d.text(
            x1, y1, z1, "Point 1", fontsize=12, ha="right", va="bottom", color="black"
        )
        self.ax_3d.text(
            x2, y2, z2, "Point 2", fontsize=12, ha="right", va="bottom", color="black"
        )
        self.ax_3d.plot(
            [x1, x2],
            [y1, y2],
            [z1, z2],
            c="red",
            linestyle="--",
            linewidth=2,
            label=f"Minkowski Distance: {distance:.2f}",
        )
        self.ax_3d.set_title(f"Minkowski Distance (p={p}) Visualization in 3D")
        self.ax_3d.set_xlabel("X-axis")
        self.ax_3d.set_ylabel("Y-axis")
        self.ax_3d.set_zlabel("Z-axis")
        self.ax_3d.legend()
        self.canvas_3d.draw()

    def check(self):
        text = self.comboBox.currentText()
        if text == "Minkowski":
            self.lineEdit_8.setHidden(False)
            self.label_18.setHidden(False)
        else:
            self.lineEdit_8.setHidden(True)
            self.label_18.setHidden(True)

    def hamming_distance(self, str1, str2):
        if len(str1) != len(str2):
            raise ValueError("Strings must be of equal length")
        return sum(c1 != c2 for c1, c2 in zip(str1, str2))

    def Hamming_plot(self):
        str1 = self.lineEdit_2_5.text()
        str2 = self.lineEdit_1_5.text()
        try:
            distance = self.hamming_distance(str1, str2)
            self.lineEdit_9.setText(str(distance))
            self.plot_hamming_distance(str1, str2)
        except ValueError as e:
            print(e)

    def plot_hamming_distance(self, bin_str1, bin_str2):
        if len(bin_str1) != len(bin_str2):
            raise ValueError("Strings must be of equal length")

        distances = [
            int(c1 != c2) for c1, c2 in zip(bin_str1, bin_str2)
        ]  # Hamming distance

        fig = Figure(figsize=(5, 4))
        ax = fig.add_subplot(111)
        ax.plot(range(1, len(bin_str1) + 1), distances, marker="o", linestyle="-")
        ax.set_title("Hamming Distance")
        ax.set_xlabel("Position")
        ax.set_ylabel("Hamming Distance")

        canvas = FigureCanvas(fig)

        if self.widget_2.layout() is not None:
            # Clear the previous plot
            for i in reversed(range(self.widget_2.layout().count())):
                widgetToRemove = self.widget_2.layout().itemAt(i).widget()
                # remove it from the layout list
                self.widget_2.layout().removeWidget(widgetToRemove)
                # remove it from the gui
                widgetToRemove.setParent(None)
        # Check if the widget has a layout, if not create one
        if not self.widget_2.layout():
            self.widget_2.setLayout(QVBoxLayout())

        # Add the canvas to the layout of self._widget_2
        self.widget_2.layout().addWidget(canvas)

    def knn(self, test_point, k, dataset):
        distances = [
            np.sqrt(np.sum((np.array(test_point) - np.array(point[:-1])) ** 2))
            for point in dataset
        ]

        indices_of_k_neighbors = np.argsort(distances)[:k]

        k_nearest_labels = [dataset[i][-1] for i in indices_of_k_neighbors]

        label_counts = Counter(k_nearest_labels)

        majority_label = label_counts.most_common(1)[0][0]

        return majority_label, indices_of_k_neighbors

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

    def display_knn(self):
        x1 = int(self.lineEdit_11.text())
        y1 = int(self.lineEdit_12.text())
        test_point = (x1, y1)
        k = 5

        result_label, indices_of_k_neighbors = self.knn(test_point, k, self.dataset)

        x_values = [item[0] for item in self.dataset]
        y_values = [item[1] for item in self.dataset]
        labels = [1 if item[2] == "A" else 0 for item in self.dataset]

        self.lineEdit_10.setText(result_label)

        # Ensure there is a layout set for self.widget_3
        if self.widget_3.layout() is not None:
            # Clear the previous plot
            for i in reversed(range(self.widget_3.layout().count())):
                widgetToRemove = self.widget_3.layout().itemAt(i).widget()
                # remove it from the layout list
                self.widget_3.layout().removeWidget(widgetToRemove)
                # remove it from the gui
                widgetToRemove.setParent(None)

        # Create a new subplot
        fig, ax = plt.subplots()

        # Scatter plot of the dataset
        scatter = ax.scatter(
            x_values, y_values, c=labels, cmap="viridis", marker="o", s=100
        )

        # Mark the test point
        test_point_plot = ax.scatter(
            test_point[0], test_point[1], c="r", marker="x", s=150, label="Test Point"
        )

        # Mark the k-nearest neighbors
        k_neighbors_plot = ax.scatter(
            [self.dataset[i][0] for i in indices_of_k_neighbors],
            [self.dataset[i][1] for i in indices_of_k_neighbors],
            c="b",
            marker="s",
            s=100,
            label=f"{k}-Nearest Neighbors",
        )

        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_title("KNN Visualization for a Single Test Point")
        ax.legend()

        # Ensure the plot fits within the widget
        fig.tight_layout()

        # Create a FigureCanvas object and set it as the widget's layout
        canvas = FigureCanvas(fig)
        self.widget_3.setLayout(QVBoxLayout())
        self.widget_3.layout().addWidget(canvas)

    def generate_data(self, num_points, num_clusters=3):
        np.random.seed(42)
        data = []
        for _ in range(num_clusters):
            cluster_center = np.random.rand(2) * 10  # Generate random cluster centers
            cluster = cluster_center + np.random.randn(num_points // num_clusters, 2)
            data.extend(cluster)
        return np.array(data)

    def k_means_simulator(self, data, k, max_iterations=100):
        cluster_centers = data[np.random.choice(len(data), k, replace=False)]

        for _ in range(max_iterations):
            distances = np.linalg.norm(data[:, np.newaxis] - cluster_centers, axis=2)
            labels = np.argmin(distances, axis=1)

            new_centers = np.array([data[labels == j].mean(axis=0) for j in range(k)])

            if np.all(new_centers == cluster_centers):
                break

        cluster_centers = new_centers

        return cluster_centers, labels

    def plot_clusters(self, data, cluster_centers, labels, new_point=None, widget=None):
        fig, ax = plt.subplots(figsize=(6, 4))

        if widget.layout() is not None:
            # Clear the previous plot
            for i in reversed(range(widget.layout().count())):
                widgetToRemove = widget.layout().itemAt(i).widget()
                # remove it from the layout list
                widget.layout().removeWidget(widgetToRemove)
                # remove it from the gui
                widgetToRemove.setParent(None)

        ax.scatter(data[:, 0], data[:, 1], c=labels, cmap="viridis", edgecolors="k")
        ax.scatter(
            cluster_centers[:, 0],
            cluster_centers[:, 1],
            c="red",
            marker="X",
            s=200,
            label="Cluster Centers",
        )

        if new_point is not None:
            ax.scatter(
                new_point[0],
                new_point[1],
                c="blue",
                marker="*",
                s=200,
                label="New Point",
            )

        ax.set_title("K-Means Clustering Simulator")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.legend()

        # Convert the plot to a widget
        canvas = FigureCanvas(fig)

        # Set a layout to the widget
        canvas = FigureCanvas(fig)
        widget.setLayout(QVBoxLayout())
        widget.layout().addWidget(canvas)

    def Simulate_K_Means(self):
        num_clusters = self.spinBox.value()
        num_points = 300

        # Generate random data
        data_points = self.generate_data(num_points)

        # Simulate k-means algorithm
        final_cluster_centers, cluster_assignments = self.k_means_simulator(
            data_points, num_clusters
        )

        # Plot the results in widget_4
        self.plot_clusters(
            data_points, final_cluster_centers, cluster_assignments, None, self.widget_4
        )

    def generate_random_points(self, num_points, seed=None):
        if seed is not None:
            np.random.seed(seed)
        X = np.random.rand(num_points, 2) * 10
        y = (X[:, 1] > X[:, 0] + np.random.randn(num_points)) * 2 - 1
        return X, y

    def plot_decision_boundary(self, X, y, clf, widget):
        fig, ax = plt.subplots(figsize=(6, 4))

        ax.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired, edgecolors="k")
        if self.widget_5.layout() is not None:
            # Clear the previous plot
            for i in reversed(range(self.widget_5.layout().count())):
                widgetToRemove = self.widget_5.layout().itemAt(i).widget()
                # remove it from the layout list
                self.widget_5.layout().removeWidget(widgetToRemove)
                # remove it from the gui
                widgetToRemove.setParent(None)
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()

        xx, yy = np.meshgrid(
            np.linspace(xlim[0], xlim[1], 100), np.linspace(ylim[0], ylim[1], 100)
        )
        Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)

        ax.contour(
            xx,
            yy,
            Z,
            colors="k",
            levels=[-1, 0, 1],
            alpha=0.5,
            linestyles=["--", "-", "--"],
        )

        ax.set_title("SVM Decision Boundary")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")

        canvas = FigureCanvas(fig)
        widget.setLayout(QVBoxLayout())
        widget.layout().addWidget(canvas)

    def simulate_svm(self):
        num_points_text = self.lineEdit_2_6.text()
        C_value_text = self.lineEdit_2_7.text()

        try:
            num_points = int(num_points_text)
            C_value = float(C_value_text)
        except ValueError:
            print("Invalid input for number of points or C value")
            return

        X, y = self.generate_random_points(num_points)
        clf = svm.SVC(kernel="linear", C=C_value)
        clf.fit(X, y)

        self.plot_decision_boundary(X, y, clf, self.widget_5)

    def generate_random(self, num_points):
        X = np.random.rand(num_points, 2) * 10
        y = (X[:, 1] > X[:, 0] + np.random.randn(num_points)) * 2 - 1
        return X, y

    def plot_show(self, X, y, clf):
        fig, ax = plt.subplots(figsize=(6, 4))

        # Scatter plot with labeled points
        ax.scatter(
            X[:, 0],
            X[:, 1],
            c=y,
            cmap=plt.cm.Paired,
            edgecolors="k",
            label="Data Points",
        )

        xlim = ax.get_xlim()
        ylim = ax.get_ylim()

        xx, yy = np.meshgrid(
            np.linspace(xlim[0], xlim[1], 100), np.linspace(ylim[0], ylim[1], 100)
        )
        Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])

        Z = Z.reshape(xx.shape)
        # Contour lines with labels
        ax.contour(
            xx,
            yy,
            Z,
            colors="k",
            levels=[-1, 0, 1],
            alpha=0.5,
            linestyles=["--", "-", "--"],
            label="Decision Boundary",
        )

        ax.set_title("SVM Decision Boundary")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.legend()

        canvas = FigureCanvas(fig)

        # Show the plot in a separate window
        new_window = QWidget()
        new_window.setWindowTitle("SVM Decision Boundary")
        layout = QVBoxLayout(new_window)
        layout.addWidget(canvas)
        new_window.show()

    def SVM(self):
        # Get user input
        num_points_text = self.lineEdit_2_6.text()
        C_value_text = self.lineEdit_2_7.text()

        # Convert num_points_text and C_value_text to integers and floats respectively
        try:
            num_points = int(num_points_text)
            C_value = float(C_value_text)
        except ValueError:
            print("Invalid input for number of points or C value")
            return

        # Generate random points
        X, y = self.generate_random(num_points)

        # Create and train the linear SVM model
        clf = svm.SVC(kernel="linear", C=C_value)
        clf.fit(X, y)

        # Plot the decision boundary
        self.plot_show(X, y, clf)

    def metrics_knn(self):
        # Define the range for random coordinates
        x_min, x_max = 0, 10
        y_min, y_max = 0, 10

        # Define the number of data points
        num_points = 50

        # Generate random coordinates within the specified range
        np.random.seed(42)
        X = np.random.uniform(x_min, x_max, size=(num_points, 2))
        y = np.random.randint(0, 3, size=num_points)  # Random labels (0, 1, or 2)

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        k = 3

        knn = KNeighborsClassifier(n_neighbors=k)

        knn.fit(X_train, y_train)

        y_pred = knn.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average="weighted", zero_division=1)
        recall = recall_score(y_test, y_pred, average="weighted")
        f1 = f1_score(y_test, y_pred, average="weighted")

        # Plot decision boundary
        xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))

        Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.contourf(xx, yy, Z, alpha=0.8)
        ax.scatter(X[:, 0], X[:, 1], c=y, edgecolors="k")
        ax.set_xlabel("Feature 1")
        ax.set_ylabel("Feature 2")
        ax.set_title("KNN Decision Boundary (k = {})".format(k))

        # Annotate the plot with evaluation metrics
        ax.text(
            x_min,
            y_max,
            f"Accuracy: {accuracy:.2f}\nPrecision: {precision:.2f}\nRecall: {recall:.2f}\nF1 Score: {f1:.2f}",
            horizontalalignment="left",
            verticalalignment="top",
            fontsize=12,
            bbox=dict(facecolor="white", alpha=0.5),
        )

        canvas = FigureCanvas(fig)
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        self.widget_7.setLayout(layout)
