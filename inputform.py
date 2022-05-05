from PyQt5 import QtCore, QtGui, QtWidgets
import database as db
from PyQt5.QtCore import pyqtSignal


class Ui_inputWindow(QtCore.QObject):

    def setupUi(self, inputWindow):
        inputWindow.setObjectName("inputWindow")
        inputWindow.resize(815, 75)
        inputWindow.setMinimumSize(QtCore.QSize(815, 75))
        inputWindow.setMaximumSize(QtCore.QSize(815, 75))
        self.centralwidget = QtWidgets.QWidget(inputWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dateTimeEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(5, 15, 141, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setText(db.currentTime(1))
        self.inputLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.inputLineEdit.setGeometry(QtCore.QRect(160, 15, 551, 22))
        self.inputLineEdit.setObjectName("inputLineEdit")
        self.inputButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.sendData(inputWindow))
        self.inputButton.setGeometry(QtCore.QRect(720, 15, 93, 26))
        self.inputButton.setObjectName("inputButton")
        self.dataLabel = QtWidgets.QLabel(self.centralwidget)
        self.dataLabel.setGeometry(QtCore.QRect(10, 80, 55, 10))
        self.dataLabel.setMaximumSize(QtCore.QSize(80, 10))
        self.dataLabel.setObjectName("dataLabel")
        inputWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(inputWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 815, 26))
        self.menubar.setObjectName("menubar")
        inputWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(inputWindow)
        self.statusbar.setObjectName("statusbar")
        inputWindow.setStatusBar(self.statusbar)
        self.retranslateUi(inputWindow)
        QtCore.QMetaObject.connectSlotsByName(inputWindow)
        self.inputLineEdit.returnPressed.connect(self.inputButton.click)
        

    def retranslateUi(self, inputWindow):
        _translate = QtCore.QCoreApplication.translate
        inputWindow.setWindowTitle(_translate("inputWindow", "Input Form"))
        self.inputButton.setText(_translate("inputWindow", "Submit"))
        self.dataLabel.setText(_translate("inputWindow", "TextLabel"))

    def sendData(self, thisWindow):
        if not self.inputLineEdit.text():
            self.showError("No input, you need to type something on the line.")
            return
        else:    
            entry = self.inputLineEdit.text()
            entry = entry.replace("'", "''")
            entryType = self.dataLabel.text()
            currentTime = self.dateTimeEdit.text()
            currentDate = db.currentTime(2)
            sql = (
                rf"Insert into SHIFT{db.currentShift()} (LoggedDate, LoggedTime, logType, logEntry, backendDate) Values"
                rf" ('{currentDate}','{currentTime}', '{entryType}', '{entry}', '{currentDate}')"
            )
            db.cursor.execute(sql)
            db.cursor.commit()
            thisWindow.close()
            self.window_closed.emit()

    def showError(self, arg): #Designed that the ARG will pass the error message. 
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(arg)
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle("Error")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        x = msgBox.exec_()
    
    window_closed = pyqtSignal()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inputWindow = QtWidgets.QMainWindow()
    ui = Ui_inputWindow()
    ui.setupUi(inputWindow)
    inputWindow.show()
    sys.exit(app.exec_())
    
    