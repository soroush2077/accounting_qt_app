import sys
from PyQt6 import QtWidgets, QtCore
from StartUp import Ui_StartUpWindow
from sign_up import Ui_SignUpWindow
from login import Ui_LoginWindow
from forgotPassword import Ui_ForgotPassWindow
from main_page import Ui_MainPage
from income import Ui_IncomeWindow
from expense import Ui_ExpenseWindow
from categoriy import Ui_Category
from search import Ui_SearchWindow
from report import Ui_ReportWindow
from settings import Ui_Setting
import validation
import dataBase





class StartWindow(QtWidgets.QMainWindow,Ui_StartUpWindow):
    
    def __init__(self):
        super(StartWindow, self).__init__()
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
        
        if validation.valid_first_name(self.lineEdit.text()) != "OK":
            self.label_error.setText(validation.valid_first_name(self.lineEdit.text()))
            
        elif validation.valid_last_name(self.lineEdit_2.text()) != "OK":
            self.label_error.setText(validation.valid_last_name(self.lineEdit_2.text()))
            
        elif validation.valid_phone_number(self.lineEdit_3.text()) != "OK":
            self.label_error.setText(validation.valid_phone_number(self.lineEdit_3.text()))
            
        elif validation.valid_username(self.lineEdit_4.text()) != "OK":
            self.label_error.setText(validation.valid_username(self.lineEdit_4.text()))
            
        elif validation.valid_password(self.lineEdit_5.text()) != "OK":
            self.label_error.setText(validation.valid_password(self.lineEdit_5.text()))
            
        elif self.lineEdit_5.text() != self.lineEdit_6.text():
            self.label_error.setText("Passwords are not the same")
            
        elif validation.valid_email(self.lineEdit_7.text()) != "OK":
            self.label_error.setText(validation.valid_email(self.lineEdit_7.text()))
            
        elif validation.valid_security_answer(self.lineEdit_8.text()) != "OK":
            self.label_error.setText(validation.valid_security_answer(self.lineEdit_8.text()))
            
        elif validation.valid_city(self.comboBox.currentText()) != "OK":
            self.label_error.setText(validation.valid_city(self.comboBox.currentText()))
            
        elif validation.valid_birth_date(self.date.text()) != "OK":
            self.label_error.setText(validation.valid_birth_date(self.date.text()))
            
        else:
            
            result = dataBase.add_account(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(),\
                self.lineEdit_5.text(), self.lineEdit_7.text(), self.lineEdit_8.text(), self.comboBox.currentText(), self.date.text())
            
            if result == "sign up completed":
                self.label_error.setStyleSheet("QLabel { color: white; font-weight: bold;}")
                self.label_error.setText("sign up completed\nyou will be redirected to the login page")
                QtCore.QTimer.singleShot(5000, self.open_login_window)
                
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
        self.pushButton_login.clicked.connect(self.pushButton_login_clicked)
        self.pushButton_forgot_password.clicked.connect(self.open_forgotPassWindow)
        
    def pushButton_login_clicked(self):
        
        result = dataBase.user_login(self.lineEdit_username.text(), self.lineEdit_password.text())
        
        if result == "You have successfully logged in":
            self.label_error.setStyleSheet("QLabel { color: white; font-weight: bold;}")
            self.label_error.setText("You have successfully logged in\nYou will be redirected to the main page in 5 seconds")
            user_class.set_user(self.lineEdit_username.text())
            QtCore.QTimer.singleShot(5000, self.open_main_page)
            
        else:
            self.label_error.setText(f"{result}")        
        
    def open_forgotPassWindow(self):
        self.forgotPassWindow = ForgotPassWindow()
        self.forgotPassWindow.show()
        self.close()
        
    def open_main_page(self):
        self.main_page_window = MainPage()
        self.main_page_window.show()
        self.close()
        
        
class ForgotPassWindow(QtWidgets.QMainWindow,Ui_ForgotPassWindow):
    
    def __init__(self):
        super(ForgotPassWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Recover Password")
        self.pushButton_forgot_pass.clicked.connect(self.pushButton_forgot_pass_clicked)
        
    def pushButton_forgot_pass_clicked(self):
        result = dataBase.user_forgot_pass(self.lineEdit.text(), self.lineEdit_security_answer.text())
        if result == "User not found":
            self.label.setText(f"{result}")
        elif result == "Incorrect answer":
            self.label.setText(f"{result}")
        else:
            self.label.setText(f"Your password: {result}\nyou will be redirected to the login page")
            QtCore.QTimer.singleShot(5000, self.open_login_window)
            
    def open_login_window(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()
            
        
class MainPage(QtWidgets.QMainWindow,Ui_MainPage):
    
    def __init__(self):
        super(MainPage,self).__init__()       
        self.setupUi(self)
        self.setWindowTitle("My accounting app")
        
        self.pushButton_income.clicked.connect(self.open_income_window)
        self.pushButton_expense.clicked.connect(self.open_expense_window)
        self.pushButton_categories.clicked.connect(self.open_category_window)
        self.pushButton_search.clicked.connect(self.open_search_window)
        self.pushButton_reports.clicked.connect(self.open_report_window)
        self.pushButton_settings.clicked.connect(self.open_settings_window)
        self.pushButton_exit.clicked.connect(exit)
    
    def open_income_window(self):
        self.income_window = IncomeWindow()
        self.income_window.show()
        # self.close()
        
    def open_expense_window(self):
        self.expense_window = ExpenseWindow()
        self.expense_window.show()
        # self.close()

    def open_category_window(self):
        self.category_window = Category()
        self.category_window.show()
        # self.close()
        
    def open_search_window(self):
        self.search_window = SearchWindow()
        self.search_window.show()
        # self.close()
        
    def open_report_window(self):
        self.report_window = ReportWindow()
        self.report_window.show()
        # self.close()
    
    def open_settings_window(self):
        self.settings_window = SettingWindow()
        self.settings_window.show()


class IncomeWindow(QtWidgets.QMainWindow,Ui_IncomeWindow):
    
    def __init__(self):
        super(IncomeWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Record Income")
        self.comboBox_source.addItems([item[0] for item in dataBase.get_categories(user_class.curent_user)])       
        self.pushButton_submit.clicked.connect(self.pushButton_submit_clicked)
    
    def pushButton_submit_clicked(self):
        
        if validation.valid_amount(self.lineEdit_income.text()) != "OK":
            self.label_error.setText(validation.valid_amount(self.lineEdit_income.text()))
            
        elif validation.valid_source(self.comboBox_source.currentText()) != "OK":
            self.label_error.setText(validation.valid_source(self.comboBox_source.text()))    
            
        elif validation.valid_date(self.dateEdit_date.text()) != "OK":
            self.label_error.setText(validation.valid_date(self.dateEdit_date.text()))
            
        elif validation.valid_type(self.comboBox_type.currentText()) != "OK":
            self.label_error.setText(validation.valid_type(self.comboBox_type.currentText()))
            
        else:
            dataBase.add_transaction(user_class.curent_user, "income", self.lineEdit_income.text(),\
                                            self.dateEdit_date.text(), self.comboBox_source.currentText(),\
                                            self.comboBox_type.currentText(), self.lineEdit_description.text())
            
            self.label_error.setStyleSheet("QLabel { color: white; font-weight: bold;}")
            self.label_error.setText("Your income has been saved.")
            
            
            
class ExpenseWindow(QtWidgets.QMainWindow,Ui_ExpenseWindow):
    
    def __init__(self):
        super(ExpenseWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Record Expense")
        self.comboBox_source.addItems([item[0] for item in dataBase.get_categories(user_class.curent_user)])
        self.pushButton_submit.clicked.connect(self.pushButton_submit_clicked)
    
    def pushButton_submit_clicked(self):
        
        if validation.valid_amount(self.lineEdit_expense.text()) != "OK":
            self.label_error.setText(validation.valid_amount(self.lineEdit_expense.text()))
            
        elif validation.valid_source(self.comboBox_source.currentText()) != "OK":
            self.label_error.setText(validation.valid_source(self.comboBox_source.text()))    
            
        elif validation.valid_date(self.dateEdit_date.text()) != "OK":
            self.label_error.setText(validation.valid_date(self.dateEdit_date.text()))
            
        elif validation.valid_type(self.comboBox_type.currentText()) != "OK":
            self.label_error.setText(validation.valid_type(self.comboBox_type.currentText()))
               
        else:
            result = dataBase.add_transaction(user_class.curent_user, "expense", self.lineEdit_expense.text(),\
                                            self.dateEdit_date.text(), self.comboBox_source.currentText(),\
                                            self.comboBox_type.currentText(), self.lineEdit_description.text())
            
            self.label_error.setStyleSheet("QLabel { color: white; font-weight: bold;}")
            self.label_error.setText("Your expense has been saved.")
            
            
            
class Category(QtWidgets.QMainWindow,Ui_Category):
    
    def __init__(self):
        super(Category,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Categories")
        self.pushButton_submit.clicked.connect(self.category_submit)
    
    def category_submit(self):
        
        if validation.valid_category(self.lineEdit_category.text()) != "OK":
            self.label_result.setText(validation.valid_category(self.lineEdit_category.text()))
            self.label_result.setStyleSheet("QLabel { color: red; font-weight: bold; font-style: italic; }")
        
        else:
            result = dataBase.add_category(user_class.curent_user, self.lineEdit_category.text())
            if result == "Category already exists":
                self.label_result.setText(result)
                self.label_result.setStyleSheet("QLabel { color: red; font-weight: bold; font-style: italic; }")
            
            elif result == "Category added succesfuly":
                self.label_result.setText(result)
                self.label_result.setStyleSheet("QLabel { color: white; font-weight: bold;}")
                
                
                
class SearchWindow(QtWidgets.QMainWindow, Ui_SearchWindow):
    
    def __init__(self):
        super(SearchWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Search")
        self.pushButton_search.clicked.connect(self.pushButton_search_clicked)
        
        
    def pushButton_search_clicked(self):
        
        if validation.valid_search_text(self.lineEdit_search.text()) != "OK":
            self.label_error.setStyleSheet("QLabel { color: red; font-weight: bold; font-style: italic; }")
            self.label_error.setText(validation.valid_search_text(self.lineEdit_search.text()))
        
        
        else:
            self.label_error.setText("")
            filters = {'search': self.lineEdit_search.text()}    
        
            if self.comboBox_income_or_expense.currentText() == "Income":
                filters["income_or_expense"] = "income"  
            elif self.comboBox_income_or_expense.currentText() == "Expense":
                filters["income_or_expense"] = "expense"
                
            if self.radioButton_date.isChecked():
                filters["date"] = self.dateEdit.text()
            elif self.radioButton_month.isChecked():
                filters["month"] = self.lineEdit_month.text()
            elif self.radioButton_year.isChecked():
                filters["year"] = self.lineEdit_year.text()
            
            if validation.valid_range(int(self.min_amount_spin.value()), int(self.max_amount_spin.value())) == "OK":   
                filters["amount_range"] = [int(self.min_amount_spin.value()), int(self.max_amount_spin.value())]
                
            if self.checkBox_description.isChecked():
                filters["description"] = ""
                
            if self.checkBox_type.isChecked():
                filters["type"] = ""
                    
            if self.checkBox_source.isChecked():
                filters["source"] = ""
                
            result = dataBase.search(user_class.curent_user, self.lineEdit_search.text(), filters)
            self.populate_table(result)



class ReportWindow(QtWidgets.QMainWindow, Ui_ReportWindow):
    
    def __init__(self):
        super(ReportWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Report")
        self.comboBox_source.addItems([item[0] for item in dataBase.get_categories(user_class.curent_user)])
        self.pushButton_report.clicked.connect(self.pushButton_report_clicked)
        
        
    def pushButton_report_clicked(self):
        
        filters = dict()
        
        if self.comboBox_income_or_expense.currentText() == "Income":
            filters["income_or_expense"] = "income"  
        elif self.comboBox_income_or_expense.currentText() == "Expense":
            filters["income_or_expense"] = "expense"
            
        if self.radioButton_date.isChecked():
            filters["date"] = self.dateEdit.text()
        elif self.radioButton_month.isChecked():
            filters["month"] = self.lineEdit_month.text()
        elif self.radioButton_year.isChecked():
            filters["year"] = self.lineEdit_year.text()
        elif self.radioButton_last_day.isChecked():
            filters["last_day"] = ""
        elif self.radioButton_last_three_days.isChecked():
            filters["last_three_days"] = ""
        elif self.radioButton_date_range.isChecked():
            filters["date_range"] = [self.dateRange_start.text(), self.dateRange_end.text()]
        
        if validation.valid_range(int(self.min_amount_spin.value()), int(self.max_amount_spin.value())) == "OK":   
            filters["amount_range"] = [int(self.min_amount_spin.value()), int(self.max_amount_spin.value())]
            
        if self.checkBox_type.isChecked():
            if self.comboBox_type.currentText() != "Select Type":
                filters["type"] = self.comboBox_type.currentText()
                
        if self.checkBox_source.isChecked():
            if self.comboBox_source.currentText() != "Select Source":
                filters["source"] = self.comboBox_source.currentText()
            
        result = dataBase.report(user_class.curent_user, filters)
        self.populate_table(result)
        self.label_total.setText(f"Total in this filters = {dataBase.results_total(result)}")
        try:
            self.label_division.setText(f"Division =\
            {round(dataBase.results_total(result) / dataBase.total(user_class.curent_user, self.comboBox_income_or_expense.currentText().lower()), 2)}")
        except ZeroDivisionError:
            self.label_division.setText("Division = 0")


class SettingWindow(QtWidgets.QMainWindow, Ui_Setting):
    
    def __init__(self):
        super(SettingWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Settings")
        self.pushButton_editprofile.clicked.connect(self.edit_profile)
        self.pushButton_deleteAcount.clicked.connect(self.delete_account)
        self.pushButton_all_trans.clicked.connect(self.delete_all_trans)
        self.pushButton_expense_trans.clicked.connect(self.delete_expense_trans)
        self.pushButton_income_trans.clicked.connect(self.delete_income_trans)
    
    
    def edit_profile(self):
        
        updates = dict()
        
        if validation.valid_first_name(self.lineEdit_firstname.text()) == "OK":
            updates["first_name"] = self.lineEdit_firstname.text()
        
        if validation.valid_last_name(self.lineEdit_lastname.text()) == "OK":
            updates["last_name"] = self.lineEdit_lastname.text()
        
        if validation.valid_phone_number(self.lineEdit_phonenumber.text()) == "OK":
            updates["phone_number"] = self.lineEdit_phonenumber.text()
        
        if validation.valid_password(self.lineEdit_password.text()) == "Ok":
            updates["password"] = self.lineEdit_password.text()
        
        if validation.valid_security_answer(self.lineEdit_security_answer.text()) == "OK":
            updates["security_answer"] = self.lineEdit_security_answer.text()
        
        if validation.valid_city(self.comboBox.currentText()) == "OK":
            updates["city"] = self.comboBox.currentText()
        
        if (validation.valid_birth_date(self.date.text()) == "OK") and self.date.text() != "2000-01-01":
            updates["birth_date"] = self.date.text()
            
        result = dataBase.edit_account(user_class.curent_user, updates)
        self.label_result.setText(result)
    
    def delete_account(self):
        dataBase.delete_user(user_class.curent_user)
        self.label_result.setText("User deleted\nGood Bye")
        QtCore.QTimer.singleShot(2000, exit)
    
    def delete_income_trans(self):
        dataBase.delete_income(user_class.curent_user)
        self.label_result.setText("All income transactions deleted")
    
    def delete_expense_trans(self):
        dataBase.delete_expense(user_class.curent_user)
        self.label_result.setText("All expense transaction deleted")
        
    def delete_all_trans(self):
        self.delete_income_trans()
        self.delete_expense_trans()
        self.label_result.setText("All transactions deleted")



class user_class:
    curent_user = ""
    def set_user(user):
        user_class.curent_user = user



def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = StartWindow()
    main_window.show()
    app.exec()



if __name__ == "__main__":
    main()
