import sys
from PyQt6 import QtWidgets
from mainwindow import Ui_MainWindow
from sign_up import Ui_SignUpWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_signup.clicked.connect(self.open_signup_window)
        self.pushButton_login.clicked.connect(self.open_login_window)
    def open_signup_window(self):
        self.signup_window = SignUpWindow()
        self.signup_window.show()
        self.hide()
    def open_login_window(self):
        pass

class SignUpWindow(QtWidgets.QMainWindow, Ui_SignUpWindow):
    def __init__(self):
        super(SignUpWindow, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
