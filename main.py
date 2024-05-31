import sys
from PyQt6 import QtWidgets
from StartUp import Ui_StartUpWindow
from sign_up import Ui_SignUpWindow
from login import Ui_LoginWindow
from forgotPassword import Ui_ForgotPassWindow
from main_page import Ui_MainPage
import validation
import dataBase
import time

class MainWindow(QtWidgets.QMainWindow,Ui_StartUpWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login or Sign Up")
        self.pushButton_signup.clicked.connect(self.open_signup_window)
        self.pushButton_login.clicked.connect(self.open_login_window)
    def open_signup_window(self):
        self.signup_window = SignUpWindow()
        self.signup_window.show()
        self.close()
    def open_login_window(self):
        self.login_window= LoginWindow()
        self.login_window.show()
        self.close()

class SignUpWindow(QtWidgets.QMainWindow, Ui_SignUpWindow):
    def __init__(self):
        super(SignUpWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sign up")
        self.pushButton_signUp.clicked.connect(self.pushButton_signup_clicked)
    def pushButton_signup_clicked(self):
        
        validation.valid_first_name(self.lineEdit.text())
        if validation.valid_first_name(self.lineEdit.text())!="OK":
            self.label_error.setText(validation.valid_first_name(self.lineEdit.text()))
        elif validation.valid_last_name(self.lineEdit_2.text())!="OK":
            self.label_error.setText(validation.valid_last_name(self.lineEdit_2.text()))
        elif validation.valid_phone_number(self.lineEdit_3.text())!="OK":
            self.label_error.setText(validation.valid_phone_number(self.lineEdit_3.text()))
        elif validation.valid_username(self.lineEdit_4.text())!="OK":
            self.label_error.setText(validation.valid_username(self.lineEdit_4.text()))
        elif validation.valid_password(self.lineEdit_5.text())!="OK":
            self.label_error.setText(validation.valid_password(self.lineEdit_5.text()))
        elif self.lineEdit_5.text()!=self.lineEdit_6.text():
            self.label_error.setText("Passwords are not the same")
        elif validation.valid_email(self.lineEdit_7.text())!="OK":
            self.label_error.setText(validation.valid_email(self.lineEdit_7.text()))
        elif validation.valid_security_answer(self.lineEdit_8.text())!="OK":
            self.label_error.setText(validation.valid_security_answer(self.lineEdit_8.text()))
        elif validation.valid_city(self.comboBox.currentText())!="OK":
            self.label_error.setText(validation.valid_city(self.comboBox.currentText()))
        elif validation.valid_birth_date(self.date.text()) != "OK":
            self.label_error.setText(validation.valid_birth_date(self.date.text()))
        else:
            result=dataBase.add_account(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(),\
                self.lineEdit_5.text(), self.lineEdit_7.text(), self.lineEdit_8.text(), self.comboBox.currentText(), self.date.text())
            if result=="sign up completed":
                self.label_error.setStyleSheet("QLabel { color: white; font-weight: bold;}")
                self.label_error.setText("sign up completed\nyou will be redirected to the login page")
                time.sleep(5)
                self.open_login_window()
            elif result == "email and username must be unique":
                self.label_error.setText(f"{result}")
    def open_login_window(self):
        self.login_window= LoginWindow()
        self.login_window.show()
        self.close()


class LoginWindow(QtWidgets.QMainWindow,Ui_LoginWindow):
    def __init__(self):
        super(LoginWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login")
        self.pushButton_forgot_password.clicked.connect(self.open_forgotPassWindow)
    def pushButton_login_clicked(self):
        pass
    def open_forgotPassWindow(self):
        self.forgotPassWindow=ForgotPassWindow()
        self.forgotPassWindow.show()
        self.close()
class ForgotPassWindow(QtWidgets.QMainWindow,Ui_ForgotPassWindow):
    def __init__(self):
        super(ForgotPassWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Recover Password")
class MainPage(QtWidgets.QMainWindow,Ui_MainPage):
    def __init__(self):
        super(MainPage,self).__init__()       
        self.setupUi(self)
        self.setWindowTitle("My accounting app")
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()
