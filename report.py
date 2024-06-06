from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QComboBox, QCheckBox, QDateEdit, QDoubleSpinBox,
    QPushButton, QRadioButton, QButtonGroup, QTableWidget, QTableWidgetItem
)
from PyQt6.QtCore import QDate, QSize


class Ui_ReportWindow(QWidget):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 700)
        MainWindow.setMinimumSize(QSize(620, 700))
        MainWindow.setMaximumSize(QSize(620, 700))
        self.centralwidget = QWidget(MainWindow)
        wid = QWidget(self)
        self.setCentralWidget(wid)
        layout = QVBoxLayout()
        # wid.setLayout(layout)
        
        # Income or Expense
        self.comboBox_income_or_expense = QComboBox()
        self.comboBox_income_or_expense.addItem("Income", "income")
        self.comboBox_income_or_expense.addItem("Expense", "expense")
        layout.addWidget(QLabel("Income or Expense:"))
        layout.addWidget(self.comboBox_income_or_expense)

        # Date, Month, Year, Last Day, Last 3 Days Selection with Radio Buttons
        self.radioButton_date = QRadioButton("Date")
        self.radioButton_month = QRadioButton("Month")
        self.radioButton_year = QRadioButton("Year")
        self.radioButton_last_day = QRadioButton("Last Day")
        self.radioButton_last_three_days = QRadioButton("Last 3 Days")
        self.radioButton_date_range = QRadioButton("Range")
        
        self.dateEdit = QDateEdit()
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit.setDate(QDate.currentDate())
        
        self.lineEdit_month = QLineEdit()
        self.lineEdit_month.setPlaceholderText("YYYY-MM")
        self.lineEdit_year = QLineEdit()
        self.lineEdit_year.setPlaceholderText("YYYY")
        
        self.dateRange_start = QDateEdit()
        self.dateRange_start.setCalendarPopup(True)
        self.dateRange_start.setDisplayFormat("yyyy-MM-dd")
        self.dateRange_start.setDate(QDate.currentDate())
        self.dateRange_end = QDateEdit()
        self.dateRange_end.setCalendarPopup(True)
        self.dateRange_end.setDisplayFormat("yyyy-MM-dd")
        self.dateRange_end.setDate(QDate.currentDate())

        self.dateEdit.setEnabled(False)
        self.lineEdit_month.setEnabled(False)
        self.lineEdit_year.setEnabled(False)
        self.dateRange_start.setEnabled(False)
        self.dateRange_end.setEnabled(False)

        date_layout = QHBoxLayout()
        date_layout.addWidget(self.radioButton_date)
        date_layout.addWidget(self.dateEdit)
        
        month_layout = QHBoxLayout()
        month_layout.addWidget(self.radioButton_month)
        month_layout.addWidget(self.lineEdit_month)
        
        year_layout = QHBoxLayout()
        year_layout.addWidget(self.radioButton_year)
        year_layout.addWidget(self.lineEdit_year)

        range_layout = QHBoxLayout()
        range_layout.addWidget(self.radioButton_date_range)
        range_layout.addWidget(QLabel("From:"))
        range_layout.addWidget(self.dateRange_start)
        range_layout.addWidget(QLabel("To:"))
        range_layout.addWidget(self.dateRange_end)

        last_days_layout = QHBoxLayout()
        last_days_layout.addWidget(self.radioButton_last_day)
        last_days_layout.addWidget(self.radioButton_last_three_days)
        
        layout.addWidget(QLabel("Select Date/Month/Year/Last Day/Last 3 Days/Range:"))
        layout.addLayout(date_layout)
        layout.addLayout(month_layout)
        layout.addLayout(year_layout)
        layout.addLayout(last_days_layout)
        layout.addLayout(range_layout)
        
        # Button group to ensure only one radio button can be selected
        self.date_group = QButtonGroup()
        self.date_group.addButton(self.radioButton_date)
        self.date_group.addButton(self.radioButton_month)
        self.date_group.addButton(self.radioButton_year)
        self.date_group.addButton(self.radioButton_last_day)
        self.date_group.addButton(self.radioButton_last_three_days)
        self.date_group.addButton(self.radioButton_date_range)

        self.radioButton_date.toggled.connect(self.toggle_date_fields)
        self.radioButton_month.toggled.connect(self.toggle_date_fields)
        self.radioButton_year.toggled.connect(self.toggle_date_fields)
        self.radioButton_last_day.toggled.connect(self.toggle_date_fields)
        self.radioButton_last_three_days.toggled.connect(self.toggle_date_fields)
        self.radioButton_date_range.toggled.connect(self.toggle_date_fields)

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

        layout.addLayout(amount_layout)

        # Type
        self.checkBox_type = QCheckBox("Include Type in Report")
        self.checkBox_type.toggled.connect(self.toggle_type)
        
        self.comboBox_type = QComboBox()
        self.comboBox_type.addItem("Select Type", "")
        self.comboBox_type.addItem("Check")
        self.comboBox_type.addItem("Cash")
        self.comboBox_type.addItem("Digital Currency")
        self.comboBox_type.setEnabled(False)
        layout.addWidget(self.checkBox_type)
        layout.addWidget(self.comboBox_type)

        # Source
        self.checkBox_source = QCheckBox("Include Source in Report")
        self.checkBox_source.toggled.connect(self.toggle_source)
        
        self.comboBox_source = QComboBox()
        self.comboBox_source.addItem("Select Source", "")
        self.comboBox_source.setEnabled(False)
        layout.addWidget(self.checkBox_source)
        layout.addWidget(self.comboBox_source)

        # Report Button
        self.pushButton_report = QPushButton("Report")
        layout.addWidget(self.pushButton_report)
        
        # Error label
        self.label_error = QLabel()
        layout.addWidget(self.label_error)

        # Report Results Table
        self.results_table = QTableWidget()
        self.results_table.setColumnCount(6)
        self.results_table.setHorizontalHeaderLabels(["Income/Expense", "Amount", "Date", "Source", "Description", "Type"])
        layout.addWidget(self.results_table)

        self.label_full_report = QLabel("Full report:")
        self.label_full_report.setStyleSheet("QLabel { color: green; font-weight: bold;}")
        layout.addWidget(self.label_full_report)
        self.label_total = QLabel("Total in this filters = ")
        layout.addWidget(self.label_total)
        self.label_division = QLabel("Division = ")
        layout.addWidget(self.label_division)

        wid.setLayout(layout)


    def toggle_date_fields(self):
        self.dateEdit.setEnabled(self.radioButton_date.isChecked())
        self.lineEdit_month.setEnabled(self.radioButton_month.isChecked())
        self.lineEdit_year.setEnabled(self.radioButton_year.isChecked())
        self.dateRange_start.setEnabled(self.radioButton_date_range.isChecked())
        self.dateRange_end.setEnabled(self.radioButton_date_range.isChecked())
        
        
    def toggle_type(self):
        self.comboBox_type.setEnabled(self.checkBox_type.isChecked())
        
        
    def toggle_source(self):
        self.comboBox_source.setEnabled(self.checkBox_source.isChecked())


    def populate_table(self, data):
        self.results_table.setRowCount(len(data))
        for row_idx, row_data in enumerate(data):
            for col_idx, item in enumerate(row_data):
                self.results_table.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))