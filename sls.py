from PyQt5 import QtCore, QtGui, QtWidgets
from inputform import Ui_inputWindow
import pandas
import os
import database as db



class Ui_SLS(object):
    def setupUi(self, SLS):
        SLS.setObjectName("SLS")
        SLS.resize(904, 732)
        SLS.setMinimumSize(QtCore.QSize(904, 732))
        SLS.setMaximumSize(QtCore.QSize(904, 732))
        self.centralwidget = QtWidgets.QWidget(SLS)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 20, 161, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.activated.connect(self.inputForm)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 60, 561, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(700, 0, 181, 81))
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("gcslogo.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.dataTable = QtWidgets.QTableWidget(self.centralwidget)
        self.dataTable.setGeometry(QtCore.QRect(20, 100, 861, 581))
        self.dataTable.setFrameShape(QtWidgets.QFrame.Panel)
        self.dataTable.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.dataTable.setObjectName("dataTable")
        self.dataTable.setColumnCount(4)
        self.dataTable.setRowCount(0)
        self.dataTable.setColumnWidth(0,90)
        self.dataTable.setColumnWidth(1,90)
        self.dataTable.setColumnWidth(2,95)
        self.dataTable.setColumnWidth(3,565)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(3, item)
        self.submitButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.inputData())
        self.submitButton.setGeometry(QtCore.QRect(600, 57, 93, 26))
        self.submitButton.setObjectName("submitButton")
        SLS.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SLS)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 904, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        SLS.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SLS)
        self.statusbar.setObjectName("statusbar")
        SLS.setStatusBar(self.statusbar)
        self.actionUpdate = QtWidgets.QAction("actionUpdate")
        self.actionUpdate = QtWidgets.QAction(SLS)
        self.actionExport = QtWidgets.QAction(SLS)
        self.actionExport = QtWidgets.QAction("actionExport")
        self.actionExit = QtWidgets.QAction(SLS)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionUpdate)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.actionExit.triggered.connect(lambda: SLS.close())
        self.actionUpdate.triggered.connect(lambda: self.loadData())
        self.actionExport.triggered.connect(lambda: self.exportData())
        self.retranslateUi(SLS)
        QtCore.QMetaObject.connectSlotsByName(SLS)
        self.lineEdit.returnPressed.connect(self.submitButton.click)
        self.loadData()

    def retranslateUi(self, SLS):
        _translate = QtCore.QCoreApplication.translate
        SLS.setWindowTitle(_translate("SLS", "GCSecurity - Security Logging System"))
        self.comboBox.setItemText(0, _translate("SLS", "Complaint"))
        self.comboBox.setItemText(1, _translate("SLS", "Arrival"))
        self.comboBox.setItemText(2, _translate("SLS", "Departure"))
        self.comboBox.setItemText(3, _translate("SLS", "Log Off"))
        self.comboBox.setItemText(4, _translate("SLS", "Log On"))
        self.comboBox.setItemText(5, _translate("SLS", "Vendor On Property"))
        self.comboBox.setItemText(6, _translate("SLS", "Vendor Off Property"))
        self.comboBox.setItemText(7, _translate("SLS", "Radios"))
        self.comboBox.setItemText(8, _translate("SLS", "Service Animal"))
        self.comboBox.setItemText(9, _translate("SLS", "Incident"))
        self.comboBox.setItemText(10, _translate("SLS", "Key Out"))
        self.comboBox.setItemText(11, _translate("SLS", "Key In"))
        self.comboBox.setItemText(12, _translate("SLS", "Employee Login"))
        self.comboBox.setItemText(13, _translate("SLS", "Employee Sign Out"))
        item = self.dataTable.horizontalHeaderItem(0)
        item.setText(_translate("SLS", "Date"))
        item = self.dataTable.horizontalHeaderItem(1)
        item.setText(_translate("SLS", "Time"))
        item = self.dataTable.horizontalHeaderItem(2)
        item.setText(_translate("SLS", "Type"))
        item = self.dataTable.horizontalHeaderItem(3)
        item.setText(_translate("SLS", "Report"))
        self.submitButton.setText(_translate("SLS", "Submit"))
        self.menuFile.setTitle(_translate("SLS", "File"))
        self.actionExit.setText(_translate("SLS", "Exit"))
        self.actionUpdate.setText(_translate("SLS", "Update"))
        self.actionExport.setText(_translate("SLS", "Export"))
        

    def loadData(self): #Loads data into the table.
        tablerow = 0 
        for row in db.cursor.execute(db.dbLogic()):
            self.dataTable.setRowCount(tablerow+1)
            self.dataTable.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.dataTable.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.dataTable.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.dataTable.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[4]))
            tablerow+=1
            
    def showInfoMessage(self, arg): #arg will pass the message within the info message popup.
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(arg)
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle("Info")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        x = msgBox.exec_()

    def showError(self, arg): #Designed that the arg will pass the error message. 
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(arg)
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle("Error")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        x = msgBox.exec_()

    def inputData(self):
        if not self.lineEdit.text():
            print('Skipped')
            self.showError("You need to enter something in the subject line.")
            return
        else:
            currentDate = db.currentTime(2)
            currentTime = db.currentTime(1)
            entryType = 'General'
            entry = self.lineEdit.text()
            entry = entry.replace("'", "''")
            sql = (
                rf"Insert into SHIFT{db.currentShift()} (LoggedDate, LoggedTime, logType, logEntry, backendDate) Values"
                rf" ('{currentDate}','{currentTime}', '{entryType}', '{entry}', '{currentDate}')"
            )
            db.cursor.execute(sql)
            db.cursor.commit()
            self.loadData()
            self.lineEdit.setText("")
            

    def inputForm(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_inputWindow()
        self.ui.setupUi(self.window)
        entryType = self.comboBox.currentText()
        self.ui.dataLabel.setText(entryType)
        self.ui.window_closed.connect(lambda: self.loadData())
        self.window.show()
        
    def exportData(self):
        sqlQuery = pandas.read_sql_query(fr'''{db.dbLogic()}''', db.cnn)
        df = pandas.DataFrame(sqlQuery)
        df.to_excel(f'Shift{db.currentShift()}Report.xlsx', index=False)
        self.showInfoMessage(fr"Shift {db.currentShift()} Report has been saved to {os.getcwd()} as Shift{db.currentShift()}Report.xlsx")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('gcsicon.ico'))
    SLS = QtWidgets.QMainWindow()
    ui = Ui_SLS()
    ui.setupUi(SLS)
    SLS.show()
    sys.exit(app.exec_())
