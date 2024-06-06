import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QComboBox, QDateEdit, QDoubleSpinBox,
    QPushButton, QCheckBox, QRadioButton, QButtonGroup, QTableWidget, QTableWidgetItem
)
from PyQt6.QtCore import QDate, QSize
from PyQt6 import QtGui

class Ui_SearchWindow(QWidget):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 700)
        MainWindow.setMinimumSize(QSize(620, 700))
        MainWindow.setMaximumSize(QSize(620, 700))
        self.centralwidget = QWidget(parent = MainWindow)
        wid = QWidget(self)
        self.setCentralWidget(wid)
        layout = QVBoxLayout()
        # wid.setLayout(layout)
        
        
        
        layout = QVBoxLayout()
    
        # Search text
        self.lineEdit_search = QLineEdit()
        layout.addWidget(QLabel("Search:"))
        layout.addWidget(self.lineEdit_search)

        # Income or Expense
        self.comboBox_income_or_expense = QComboBox()
        self.comboBox_income_or_expense.addItem("Select", "")
        self.comboBox_income_or_expense.addItem("Income", "income")
        self.comboBox_income_or_expense.addItem("Expense", "expense")
        layout.addWidget(QLabel("Income or Expense:"))
        layout.addWidget(self.comboBox_income_or_expense)

        # Date, Month, Year Selection with Radio Buttons
        self.radioButton_date = QRadioButton("Date")
        self.radioButton_month = QRadioButton("Month")
        self.radioButton_year = QRadioButton("Year")
        
        self.dateEdit = QDateEdit()
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit.setDate(QDate.currentDate())
        
        self.lineEdit_month = QLineEdit()
        self.lineEdit_month.setPlaceholderText("YYYY-MM")
        self.lineEdit_year = QLineEdit()
        self.lineEdit_year.setPlaceholderText("YYYY")

        self.dateEdit.setEnabled(False)
        self.lineEdit_month.setEnabled(False)
        self.lineEdit_year.setEnabled(False)

        date_layout = QHBoxLayout()
        date_layout.addWidget(self.radioButton_date)
        date_layout.addWidget(self.dateEdit)
        
        month_layout = QHBoxLayout()
        month_layout.addWidget(self.radioButton_month)
        month_layout.addWidget(self.lineEdit_month)
        
        year_layout = QHBoxLayout()
        year_layout.addWidget(self.radioButton_year)
        year_layout.addWidget(self.lineEdit_year)
        
        layout.addWidget(QLabel("Select Date/Month/Year:"))
        layout.addLayout(date_layout)
        layout.addLayout(month_layout)
        layout.addLayout(year_layout)
        
        # Button group to ensure only one radio button can be selected
        self.date_group = QButtonGroup()
        self.date_group.addButton(self.radioButton_date)
        self.date_group.addButton(self.radioButton_month)
        self.date_group.addButton(self.radioButton_year)

        self.radioButton_date.toggled.connect(self.toggle_date_fields)
        self.radioButton_month.toggled.connect(self.toggle_date_fields)
        self.radioButton_year.toggled.connect(self.toggle_date_fields)

        # Amount Range
        amount_layout = QHBoxLayout()
        self.min_amount_spin = QDoubleSpinBox()
        self.min_amount_spin.setPrefix("Min: ")
        self.min_amount_spin.setMaximum(1000000)
        amount_layout.addWidget(self.min_amount_spin)

        self.max_amount_spin = QDoubleSpinBox()
        self.max_amount_spin.setPrefix("Max: ")
        self.max_amount_spin.setMaximum(1000000)
        amount_layout.addWidget(self.max_amount_spin)

        layout.addWidget(QLabel("Amount Range:"))
        layout.addLayout(amount_layout)

        # Description
        self.checkBox_description = QCheckBox("Include Description in Search")
        layout.addWidget(self.checkBox_description)

        # Type
        self.checkBox_type = QCheckBox("Include Type in Search")
        layout.addWidget(self.checkBox_type)

        # Source
        self.checkBox_source = QCheckBox("Include Source in Search")

        layout.addWidget(self.checkBox_source)


        # Search Button
        self.pushButton_search = QPushButton("Search")
        layout.addWidget(self.pushButton_search)
        
        # Error label
        self.label_error = QLabel()
        layout.addWidget(self.label_error)

        # Search Results Table
        self.results_table = QTableWidget()
        self.results_table.setColumnCount(6)
        self.results_table.setHorizontalHeaderLabels(["Income/Expense", "Amount", "Date", "Source", "Description", "Type"])
        layout.addWidget(self.results_table)
        wid.setLayout(layout)


    def toggle_date_fields(self):
        self.dateEdit.setEnabled(self.radioButton_date.isChecked())
        self.lineEdit_month.setEnabled(self.radioButton_month.isChecked())
        self.lineEdit_year.setEnabled(self.radioButton_year.isChecked())

    
    def populate_table(self, data):
        self.results_table.setRowCount(len(data))
        for row_idx, row_data in enumerate(data):
            for col_idx, item in enumerate(row_data):
                self.results_table.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))