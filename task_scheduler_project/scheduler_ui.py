# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scheduler_ui.ui'
#
# Created: Tue May 13 14:23:25 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(984, 639)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.NewTaskButton = QtGui.QPushButton(self.centralwidget)
        self.NewTaskButton.setGeometry(QtCore.QRect(140, 100, 171, 27))
        self.NewTaskButton.setObjectName(_fromUtf8("NewTaskButton"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 190, 241, 85))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.NameText = QtGui.QLineEdit(self.layoutWidget)
        self.NameText.setObjectName(_fromUtf8("NameText"))
        self.gridLayout.addWidget(self.NameText, 0, 1, 1, 1)
        self.DurationText = QtGui.QLineEdit(self.layoutWidget)
        self.DurationText.setObjectName(_fromUtf8("DurationText"))
        self.gridLayout.addWidget(self.DurationText, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(140, 270, 241, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.EditButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.EditButton.setObjectName(_fromUtf8("EditButton"))
        self.horizontalLayout_5.addWidget(self.EditButton)
        self.DeleteButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.DeleteButton.setObjectName(_fromUtf8("DeleteButton"))
        self.horizontalLayout_5.addWidget(self.DeleteButton)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(140, 390, 241, 61))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.ResourceText = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.ResourceText.setObjectName(_fromUtf8("ResourceText"))
        self.horizontalLayout_6.addWidget(self.ResourceText)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 170, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(140, 360, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(360, 0, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(140, 70, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(670, 340, 161, 231))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.CreateGraphButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.CreateGraphButton.setObjectName(_fromUtf8("CreateGraphButton"))
        self.verticalLayout.addWidget(self.CreateGraphButton)
        self.LoadFilesButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.LoadFilesButton.setObjectName(_fromUtf8("LoadFilesButton"))
        self.verticalLayout.addWidget(self.LoadFilesButton)
        self.SaveFilesButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.SaveFilesButton.setObjectName(_fromUtf8("SaveFilesButton"))
        self.verticalLayout.addWidget(self.SaveFilesButton)
        self.QuitButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.QuitButton.setObjectName(_fromUtf8("QuitButton"))
        self.verticalLayout.addWidget(self.QuitButton)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(450, 70, 161, 231))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.TaskListWidget = QtGui.QListWidget(self.widget)
        self.TaskListWidget.setObjectName(_fromUtf8("TaskListWidget"))
        self.verticalLayout_2.addWidget(self.TaskListWidget)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(670, 70, 161, 231))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.DependencyListWidget = QtGui.QListWidget(self.verticalLayoutWidget_2)
        self.DependencyListWidget.setObjectName(_fromUtf8("DependencyListWidget"))
        self.verticalLayout_3.addWidget(self.DependencyListWidget)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(450, 340, 161, 221))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_4.addWidget(self.label_7)
        self.ResourceListWidget = QtGui.QListWidget(self.verticalLayoutWidget_3)
        self.ResourceListWidget.setObjectName(_fromUtf8("ResourceListWidget"))
        self.verticalLayout_4.addWidget(self.ResourceListWidget)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(140, 450, 241, 59))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.AddResourceButton = QtGui.QPushButton(self.layoutWidget1)
        self.AddResourceButton.setObjectName(_fromUtf8("AddResourceButton"))
        self.horizontalLayout_4.addWidget(self.AddResourceButton)
        self.DeleteResourceButton = QtGui.QPushButton(self.layoutWidget1)
        self.DeleteResourceButton.setObjectName(_fromUtf8("DeleteResourceButton"))
        self.horizontalLayout_4.addWidget(self.DeleteResourceButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 984, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.NewTaskButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.NameText.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.NewTaskButton.setText(QtGui.QApplication.translate("MainWindow", "Add New Task", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Duration", None, QtGui.QApplication.UnicodeUTF8))
        self.EditButton.setText(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.DeleteButton.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Enter Resource", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Edit Task:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Resources:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Task Scheduler", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "NewTask:", None, QtGui.QApplication.UnicodeUTF8))
        self.CreateGraphButton.setText(QtGui.QApplication.translate("MainWindow", "SCHEDULE  TASKS", None, QtGui.QApplication.UnicodeUTF8))
        self.LoadFilesButton.setText(QtGui.QApplication.translate("MainWindow", "LOAD", None, QtGui.QApplication.UnicodeUTF8))
        self.SaveFilesButton.setText(QtGui.QApplication.translate("MainWindow", "SAVE", None, QtGui.QApplication.UnicodeUTF8))
        self.QuitButton.setText(QtGui.QApplication.translate("MainWindow", "QUIT", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Tasks", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Dependencies", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Resources", None, QtGui.QApplication.UnicodeUTF8))
        self.AddResourceButton.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.DeleteResourceButton.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))

