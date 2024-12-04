# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtWidgets

class Ui_To_Do_List(object):
    """
    This class defines the GUI layout and elements for the To-Do List Manager.
    Generated by QtDesigner.
    """
    def setupUi(self, To_Do_List):
        """
        Set up the user interface for the To-Do List application.
        Args:
            To_Do_List (QMainWindow): The main window of the application.
        """
        To_Do_List.setObjectName("To_Do_List")
        To_Do_List.resize(640, 480)
        To_Do_List.setMinimumSize(QtCore.QSize(0, 0))

        self.centralwidget = QtWidgets.QWidget(parent=To_Do_List)
        self.centralwidget.setObjectName("centralwidget")

        # Input box for task parameters
        self.button_input = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.button_input.setGeometry(QtCore.QRect(90, 10, 471, 31))
        self.button_input.setObjectName("button_input")

        # Table widget for displaying tasks
        self.widget_tasks = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.widget_tasks.setGeometry(QtCore.QRect(170, 130, 311, 211))
        self.widget_tasks.setObjectName("widget_tasks")
        self.widget_tasks.setColumnCount(0)
        self.widget_tasks.setRowCount(0)

        # Horizontal layout for search input & button
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(170, 90, 311, 33))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Search input
        self.lineEditSearch = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.lineEditSearch.setObjectName("lineEditSearch")
        self.horizontalLayout.addWidget(self.lineEditSearch)

        #search button
        self.btn_search = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout.addWidget(self.btn_search)

        #Buttons for Task Management
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(90, 40, 469, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        #Add task button
        self.btn_add = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout_2.addWidget(self.btn_add)

        #Mark as completed button
        self.btn_completed = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.btn_completed.setObjectName("btn_completed")
        self.horizontalLayout_2.addWidget(self.btn_completed)

        #Delete task button
        self.btn_delete = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout_2.addWidget(self.btn_delete)

        #Show completed tasks Button
        self.btn_completed_2 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.btn_completed_2.setObjectName("btn_completed_2")
        self.horizontalLayout_2.addWidget(self.btn_completed_2)

        #show all tasks button
        self.btn_all_tasks = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.btn_all_tasks.setObjectName("btn_all_tasks")
        self.horizontalLayout_2.addWidget(self.btn_all_tasks)

        To_Do_List.setCentralWidget(self.centralwidget)  #central widget

        #menu bar
        self.menubar = QtWidgets.QMenuBar(parent=To_Do_List)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 37))
        self.menubar.setObjectName("menubar")
        To_Do_List.setMenuBar(self.menubar)

        #status bar
        self.statusbar = QtWidgets.QStatusBar(parent=To_Do_List)
        self.statusbar.setObjectName("statusbar")
        To_Do_List.setStatusBar(self.statusbar)

        #finalize translations & signal connections
        self.retranslateUi(To_Do_List)
        QtCore.QMetaObject.connectSlotsByName(To_Do_List)

    def retranslateUi(self, To_Do_List):
        _translate = QtCore.QCoreApplication.translate
        To_Do_List.setWindowTitle(_translate("To_Do_List", "MainWindow"))
        self.button_input.setPlaceholderText(_translate("To_Do_List", "Enter Task Name, Category, Priority"))
        self.lineEditSearch.setPlaceholderText(_translate("To_Do_List", "Enter keyword to search"))
        self.btn_search.setText(_translate("To_Do_List", "Search"))
        self.btn_add.setText(_translate("To_Do_List", "Add"))
        self.btn_completed.setText(_translate("To_Do_List", "Done"))
        self.btn_delete.setText(_translate("To_Do_List", "Delete"))
        self.btn_completed_2.setText(_translate("To_Do_List", "All completed"))
        self.btn_all_tasks.setText(_translate("To_Do_List", "Show All"))
