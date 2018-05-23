# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/gui02.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(504, 850)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.bill_box = QtWidgets.QGroupBox(self.centralwidget)
        self.bill_box.setObjectName("bill_box")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bill_box)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bill_frame = QtWidgets.QFrame(self.bill_box)
        self.bill_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bill_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bill_frame.setObjectName("bill_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bill_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.bill_frame_upper = QtWidgets.QFrame(self.bill_frame)
        self.bill_frame_upper.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bill_frame_upper.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bill_frame_upper.setObjectName("bill_frame_upper")
        self.formLayout = QtWidgets.QFormLayout(self.bill_frame_upper)
        self.formLayout.setObjectName("formLayout")
        self.bill_year_label = QtWidgets.QLabel(self.bill_frame_upper)
        self.bill_year_label.setObjectName("bill_year_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.bill_year_label)
        self.bill_year_edit = QtWidgets.QLineEdit(self.bill_frame_upper)
        self.bill_year_edit.setObjectName("bill_year_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.bill_year_edit)
        self.bill_month_label = QtWidgets.QLabel(self.bill_frame_upper)
        self.bill_month_label.setObjectName("bill_month_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.bill_month_label)
        self.bill_month_edit = QtWidgets.QLineEdit(self.bill_frame_upper)
        self.bill_month_edit.setObjectName("bill_month_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.bill_month_edit)
        self.bill_date_label = QtWidgets.QLabel(self.bill_frame_upper)
        self.bill_date_label.setObjectName("bill_date_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.bill_date_label)
        self.bill_date_edit = QtWidgets.QDateEdit(self.bill_frame_upper)
        self.bill_date_edit.setDate(QtCore.QDate(2018, 1, 1))
        self.bill_date_edit.setObjectName("bill_date_edit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bill_date_edit)
        self.verticalLayout_2.addWidget(self.bill_frame_upper)
        self.bill_out_widget = QtWidgets.QWidget(self.bill_frame)
        self.bill_out_widget.setObjectName("bill_out_widget")
        self.formLayout_5 = QtWidgets.QFormLayout(self.bill_out_widget)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.bill_out_label = QtWidgets.QLabel(self.bill_out_widget)
        self.bill_out_label.setObjectName("bill_out_label")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.bill_out_label)
        self.bill_out_edit = QtWidgets.QLineEdit(self.bill_out_widget)
        self.bill_out_edit.setObjectName("bill_out_edit")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.bill_out_edit)
        self.verticalLayout_2.addWidget(self.bill_out_widget)
        self.bill_create_button = QtWidgets.QPushButton(self.bill_frame)
        self.bill_create_button.setObjectName("bill_create_button")
        self.verticalLayout_2.addWidget(self.bill_create_button)
        self.horizontalLayout_2.addWidget(self.bill_frame)
        self.gridLayout_3.addWidget(self.bill_box, 3, 0, 1, 1)
        self.status_box = QtWidgets.QGroupBox(self.centralwidget)
        self.status_box.setObjectName("status_box")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.status_box)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.status_frame = QtWidgets.QFrame(self.status_box)
        self.status_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.status_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.status_frame.setObjectName("status_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.status_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout.addWidget(self.status_frame)
        self.gridLayout_3.addWidget(self.status_box, 0, 2, 4, 1)
        
        self.qtConsole = ConsoleWidget()
        self.horizontalLayout_4.addWidget(self.qtConsole)



        self.table_box = QtWidgets.QGroupBox(self.centralwidget)
        self.table_box.setObjectName("table_box")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.table_box)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.table_frame = QtWidgets.QFrame(self.table_box)
        self.table_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.table_frame.setObjectName("table_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.table_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.table_select_button = QtWidgets.QPushButton(self.table_frame)
        self.table_select_button.setObjectName("table_select_button")
        self.verticalLayout_3.addWidget(self.table_select_button)
        self.table_new_button = QtWidgets.QPushButton(self.table_frame)
        self.table_new_button.setObjectName("table_new_button")
        self.verticalLayout_3.addWidget(self.table_new_button)
        self.table_widget = QtWidgets.QWidget(self.table_frame)
        self.table_widget.setObjectName("table_widget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.table_widget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.table_file_label = QtWidgets.QLabel(self.table_widget)
        self.table_file_label.setObjectName("table_file_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.table_file_label)
        self.table_file_edit = QtWidgets.QLineEdit(self.table_widget)
        self.table_file_edit.setObjectName("table_file_edit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.table_file_edit)
        self.verticalLayout_3.addWidget(self.table_widget)
        self.gridLayout_2.addWidget(self.table_frame, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.table_box, 0, 0, 1, 1)
        self.log_box = QtWidgets.QGroupBox(self.centralwidget)
        self.log_box.setObjectName("log_box")
        self.gridLayout = QtWidgets.QGridLayout(self.log_box)
        self.gridLayout.setObjectName("gridLayout")
        self.log_frame = QtWidgets.QFrame(self.log_box)
        self.log_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.log_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.log_frame.setObjectName("log_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.log_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.log_select_button = QtWidgets.QPushButton(self.log_frame)
        self.log_select_button.setObjectName("log_select_button")
        self.verticalLayout_4.addWidget(self.log_select_button)
        self.log_new_button = QtWidgets.QPushButton(self.log_frame)
        self.log_new_button.setObjectName("log_new_button")
        self.verticalLayout_4.addWidget(self.log_new_button)
        self.log_file_widget = QtWidgets.QWidget(self.log_frame)
        self.log_file_widget.setObjectName("log_file_widget")
        self.formLayout_3 = QtWidgets.QFormLayout(self.log_file_widget)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.log_file_label = QtWidgets.QLabel(self.log_file_widget)
        self.log_file_label.setObjectName("log_file_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.log_file_label)
        self.log_file_edit = QtWidgets.QLineEdit(self.log_file_widget)
        self.log_file_edit.setObjectName("log_file_edit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.log_file_edit)
        self.verticalLayout_4.addWidget(self.log_file_widget)
        self.gridLayout.addWidget(self.log_frame, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.log_box, 1, 0, 1, 1)
        self.vocab = QtWidgets.QGroupBox(self.centralwidget)
        self.vocab.setObjectName("vocab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.vocab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.vocab_frame = QtWidgets.QFrame(self.vocab)
        self.vocab_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.vocab_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.vocab_frame.setObjectName("vocab_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.vocab_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.vocab_select_button = QtWidgets.QPushButton(self.vocab_frame)
        self.vocab_select_button.setObjectName("vocab_select_button")
        self.verticalLayout.addWidget(self.vocab_select_button)
        self.vocab_new_button = QtWidgets.QPushButton(self.vocab_frame)
        self.vocab_new_button.setObjectName("vocab_new_button")
        self.verticalLayout.addWidget(self.vocab_new_button)
        self.vocab_file_widget = QtWidgets.QWidget(self.vocab_frame)
        self.vocab_file_widget.setObjectName("vocab_file_widget")
        self.formLayout_4 = QtWidgets.QFormLayout(self.vocab_file_widget)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.vocab_file_label = QtWidgets.QLabel(self.vocab_file_widget)
        self.vocab_file_label.setObjectName("vocab_file_label")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.vocab_file_label)
        self.vocab_file_edit = QtWidgets.QLineEdit(self.vocab_file_widget)
        self.vocab_file_edit.setObjectName("vocab_file_edit")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.vocab_file_edit)
        self.verticalLayout.addWidget(self.vocab_file_widget)
        self.horizontalLayout_5.addWidget(self.vocab_frame)
        self.gridLayout_3.addWidget(self.vocab, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 504, 25))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_3.setObjectName("toolBar_3")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bill_box.setTitle(_translate("MainWindow", "Bill"))
        self.bill_year_label.setText(_translate("MainWindow", "Year"))
        self.bill_month_label.setText(_translate("MainWindow", "Month"))
        self.bill_date_label.setText(_translate("MainWindow", "Date of bill"))
        self.bill_date_edit.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.bill_out_label.setText(_translate("MainWindow", "Output directory"))
        self.bill_create_button.setText(_translate("MainWindow", "Create bill"))
        self.status_box.setTitle(_translate("MainWindow", "Status"))
        self.table_box.setTitle(_translate("MainWindow", "Table of drivers (.xlsx-file)"))
        self.table_select_button.setText(_translate("MainWindow", "Select file"))
        self.table_new_button.setText(_translate("MainWindow", "Create a new file"))
        self.table_file_label.setText(_translate("MainWindow", "File"))
        self.log_box.setTitle(_translate("MainWindow", "Logbook (.xlsx-file)"))
        self.log_select_button.setText(_translate("MainWindow", "Select"))
        self.log_new_button.setText(_translate("MainWindow", "Create a new"))
        self.log_file_label.setText(_translate("MainWindow", "File"))
        self.vocab.setTitle(_translate("MainWindow", "Vocabulary (.xlsx-file)"))
        self.vocab_select_button.setText(_translate("MainWindow", "Select"))
        self.vocab_new_button.setText(_translate("MainWindow", "Create a new"))
        self.vocab_file_label.setText(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Menu"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_3"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))


from qtconsole.qt import QtGui
from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager


class ConsoleWidget(RichJupyterWidget):


    def __init__(self, customBanner=None, *args, **kwargs):
        super(ConsoleWidget, self).__init__(*args, **kwargs)

        if customBanner is not None:
            self.banner = customBanner

        self.font_size = 6
        self.kernel_manager = kernel_manager = QtInProcessKernelManager()
        kernel_manager.start_kernel(show_banner=False)
        kernel_manager.kernel.gui = 'qt'
        self.kernel_client = kernel_client = self._kernel_manager.client()
        kernel_client.start_channels()

        def stop():
            kernel_client.stop_channels()
            kernel_manager.shutdown_kernel()
            guisupport.get_app_qt().exit()

        self.exit_requested.connect(stop)

    def push_vars(self, variableDict):
        """
        Given a dictionary containing name / value pairs, push those variables
        to the Jupyter console widget
        """
        self.kernel_manager.kernel.shell.push(variableDict)

    def clear(self):
        """
        Clears the terminal
        """
        self._control.clear()

        # self.kernel_manager

    def print_text(self, text):
        """
        Prints some plain text to the console
        """
        self._append_plain_text(text)

    def execute_command(self, command):
        """
        Execute a command in the frame of the console widget
        """
        self._execute(command, False)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    #widget = ConsoleWidget()
    #widget.show()
    
    MainWindow.show()
    sys.exit(app.exec_())

