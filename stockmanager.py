from PyQt5 import QtWidgets, QtGui
import os
import datetime
import manipulation as mp
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import (QWidget, QPushButton, QMainWindow,
                             QHBoxLayout, QAction)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QStackedWidget, QListWidget, QAction, QPushButton, QHBoxLayout, QTableWidget, QLabel, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator

# Create the "stock.txt" file if it doesn't exist
if not os.path.exists("stock.txt"):
    with open("stock.txt", "w") as myfile:
        myfile.write("")

class Example(QMainWindow):


    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.st = stackedExample()
        exitAct = QAction(QIcon('exit_icon.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        self.statusBar()

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)

        self.setCentralWidget(self.st)

        self.setStyleSheet("""
            /* Example stylesheet for the application background */
            QMainWindow {
                background-color: #f0f0f0;
            }
            /* Example stylesheet for the buttons */
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: 2px solid #4CAF50;
                border-radius: 8px;
                font-size: 14px;
                padding: 6px;
            }
            /* Example stylesheet for the list widget */
            QListWidget {
                background-color: #e0e0e0;
                border: 1px solid #4CAF50;
                border-radius: 8px;
                font-size: 14px;
            }
            /* Add more stylesheets for other widgets as needed */

        """)

        self.show()

class stackedExample(QWidget):
    def __init__(self):

        super(stackedExample, self).__init__()


        font = QFont("Poppins", 10)
        QApplication.setFont(font)

        self.leftlist = QListWidget()
        self.leftlist.setFixedWidth(400)
        self.leftlist.insertItem(0, 'Add Raw Material')
        self.leftlist.insertItem(1, 'Manage Raw Material')
        self.leftlist.insertItem(2, 'View Raw Material')
        self.leftlist.insertItem(3, 'View Transaction History')

        # Center align the items in the QListWidget
        for i in range(self.leftlist.count()):

            print('\n')
            item = self.leftlist.item(i)
            item.setTextAlignment(Qt.AlignLeft)


        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack4 = QWidget()

        self.stack1UI()
        self.stack2UI()
        self.stack3UI()
        self.stack4UI()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)
        self.Stack.addWidget(self.stack4)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.leftlist.currentRowChanged.connect(self.display)
        self.setGeometry(700, 550, 400, 400)
        self.setWindowTitle('Raw Material Management')
        self.show()


    def stack1UI(self):
        layout = QVBoxLayout()

        self.ok = QPushButton('Add Raw Material', self)
        cancel = QPushButton('Cancel', self)

        self.stock_name = QLineEdit()
        self.stock_name.setPlaceholderText("Enter Raw Material Name (mandatory)")
        layout.addWidget(self.stock_name)

        # Create a QDoubleValidator to allow decimal point input
        validator = QDoubleValidator(self)
        validator.setNotation(QDoubleValidator.StandardNotation)  # Allow standard decimal notation
        validator.setDecimals(2)  # Set the maximum number of decimals to 2

        self.stock_count = QLineEdit()
        self.stock_count.setPlaceholderText("Enter Quantity (mandatory)")
        layout.addWidget(self.stock_count)
        self.stock_count.setValidator(validator)  # Set the validator for the QLineEdit

        self.stock_cost = QLineEdit()
        self.stock_cost.setPlaceholderText("Enter Cost of Raw Material (per item) (mandatory)")
        layout.addWidget(self.stock_cost)
        self.stock_cost.setValidator(validator)  # Set the validator for the QLineEdit

        layout.addWidget(self.ok)
        layout.addWidget(cancel)

        self.ok.clicked.connect(self.on_click)

        cancel.clicked.connect(self.stock_name.clear)
        cancel.clicked.connect(self.stock_cost.clear)
        cancel.clicked.connect(self.stock_count.clear)

        self.text_block = QLabel()
        layout.addWidget(self.text_block)

        self.stack1.setLayout(layout)

    def on_click(self):
        # Validation checks for mandatory fields
        if not self.stock_name.text() or not self.stock_count.text() or not self.stock_cost.text():
            QtWidgets.QMessageBox.critical(self, "Error", "Please fill in all the mandatory fields.")
            return
        else:
            inserted_data = f"Raw Material successfully Inserted:\n\nRaw Material Name: {self.stock_name.text()}\nQuantity: {self.stock_count.text()}\nCost of Raw Material (per item): {self.stock_cost.text()}"
            self.text_block.setText(inserted_data)


        now = datetime.datetime.now()
        stock_name_inp = self.stock_name.text().replace(' ', '_').lower()
        stock_count_inp = int(self.stock_count.text())
        stock_cost_inp = int(self.stock_cost.text())

        stock_add_date_time = now.strftime("%Y-%m-%d %H:%M")
        d = mp.insert_prod(stock_name_inp, stock_count_inp, stock_cost_inp, stock_add_date_time)
        print(d)
        # Need to add the above details to table

        # Clear the input fields after processing the data
        self.stock_name.clear()
        self.stock_cost.clear()
        self.stock_count.clear()

    def stack2UI(self):

        layout = QHBoxLayout()
        layout.setGeometry(QRect(0,300,1150,500))
        tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        tabs.addTab(self.tab1, 'Add Quantity')
        tabs.addTab(self.tab2, 'Reduce Quantity')
        tabs.addTab(self.tab3, 'Delete Raw Material')

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

        layout.addWidget(tabs)
        self.stack2.setLayout(layout)

    def tab1UI(self):
        # Create a QDoubleValidator to allow decimal point input
        validator = QDoubleValidator(self)
        validator.setNotation(QDoubleValidator.StandardNotation)  # Allow standard decimal notation
        validator.setDecimals(2)  # Set the maximum number of decimals to 2

        layout = QFormLayout()
        self.ok_add = QPushButton('Add Raw Material', self)
        cancel = QPushButton('Cancel', self)

        self.stock_name_add = QLineEdit()
        self.stock_name_add.setPlaceholderText("Enter Raw Material Name (mandatory)")
        layout.addRow("Raw Material Name", self.stock_name_add)

        self.stock_count_add = QLineEdit()
        self.stock_count_add.setPlaceholderText("Enter Quantity to add (mandatory)")
        layout.addRow("Quantity to add", self.stock_count_add)
        self.stock_count_add.setValidator(validator)

        layout.addWidget(self.ok_add)
        layout.addWidget(cancel)
        self.tab1.setLayout(layout)

        self.ok_add.clicked.connect(self.call_add)       # need to write function to add quantity
        cancel.clicked.connect(self.stock_name_add.clear)
        cancel.clicked.connect(self.stock_count_add.clear)

        self.text_block1 = QLabel()
        layout.addWidget(self.text_block1)

    def tab2UI(self):
        # Create a QDoubleValidator to allow decimal point input
        validator = QDoubleValidator(self)
        validator.setNotation(QDoubleValidator.StandardNotation)  # Allow standard decimal notation
        validator.setDecimals(2)  # Set the maximum number of decimals to 2

        layout = QFormLayout()
        self.ok_red = QPushButton('Reduce Raw Material', self)
        cancel = QPushButton('Cancel', self)

        self.stock_name_red = QLineEdit()
        self.stock_name_red.setPlaceholderText("Enter Raw Material Name (mandatory)")
        layout.addRow("Raw Material Name", self.stock_name_red)

        self.stock_count_red = QLineEdit()
        self.stock_count_red.setPlaceholderText("Enter Quantity to add (mandatory)")
        layout.addRow("Quantity to reduce", self.stock_count_red)
        self.stock_count_red.setValidator(validator)


        layout.addWidget(self.ok_red)
        layout.addWidget(cancel)
        self.tab2.setLayout(layout)

        self.ok_red.clicked.connect(self.call_red)  # need to write function to reduce quantity
        cancel.clicked.connect(self.stock_name_red.clear)
        cancel.clicked.connect(self.stock_count_red.clear)

        self.text_block2 = QLabel()
        layout.addWidget(self.text_block2)

    def tab3UI(self):


        layout = QFormLayout()
        self.ok_del = QPushButton('Delete Raw Material', self)
        cancel = QPushButton('Cancel', self)

        self.stock_name_del = QLineEdit()
        self.stock_name_del.setPlaceholderText("Enter Raw Material Name (mandatory)")

        layout.addRow("Raw Material Name", self.stock_name_del)
        layout.addWidget(self.ok_del)
        layout.addWidget(cancel)
        self.tab3.setLayout(layout)

        self.ok_del.clicked.connect(self.call_del)  # need to write function to delete stock
        cancel.clicked.connect(self.stock_name_del.clear)

        self.text_block3 = QLabel()
        layout.addWidget(self.text_block3)

    def call_del(self):

        # Validation checks for mandatory fields
        if not self.stock_name_del.text():
            QtWidgets.QMessageBox.critical(self, "Error", "Please fill in all the mandatory fields.")
            return
        else:
            red_data = f"Raw Material successfully Deleted:\n\nRaw Material Name: {self.stock_name_del.text()}"
            self.text_block3.setText(red_data)




        now = datetime.datetime.now()
        stock_del_date_time = now.strftime("%Y-%m-%d %H:%M")
        stock_name = self.stock_name_del.text().replace(' ', '_').lower()
        current_stock_value = mp.get_current_stock_value(stock_name)
        current_stock_cost = mp.get_current_stock_cost(stock_name)
        mp.remove_stock(stock_name,current_stock_value,current_stock_cost, stock_del_date_time)

        # Clear the input fields after processing the data
        self.stock_name_del.clear()

    def call_red(self):
        # Validation checks for mandatory fields
        if not self.stock_name_red.text() or not self.stock_count_red.text():
            QtWidgets.QMessageBox.critical(self, "Error", "Please fill in all the mandatory fields.")
            return
        else:
            stock_name = self.stock_name_red.text().replace(' ', '_').lower()
            current_stock_value = mp.get_current_stock_value(stock_name)  # Using the function directly
            stock_count_red = int(self.stock_count_red.text())

            if current_stock_value is None:
                QtWidgets.QMessageBox.critical(self, "Error", f"Stock with name '{stock_name}' not found.")
                return
            elif current_stock_value < stock_count_red:
                QtWidgets.QMessageBox.critical(self, "Error",
                                               f"Current stock level is low. Cannot reduce by {stock_count_red}.")
                return

            red_data = f"Raw Material successfully Reduced:\n\nRaw Material Name: {self.stock_name_red.text()}\nQuantity: {self.stock_count_red.text()}"
            self.text_block2.setText(red_data)

        now = datetime.datetime.now()
        stock_red_date_time = now.strftime("%Y-%m-%d %H:%M")
        stock_val = -stock_count_red
        mp.update_quantity(stock_name, stock_val, stock_red_date_time)  # Using the function directly from manipulation.py

        # Clear the input fields after processing the data
        self.stock_name_red.clear()
        self.stock_count_red.clear()

    def call_add(self):
        # Validation checks for mandatory fields
        if not self.stock_name_add.text() or not self.stock_count_add.text():
            QtWidgets.QMessageBox.critical(self, "Error", "Please fill in all the mandatory fields.")
            return
        else:
            add_data = f"Raw Material successfully Added:\n\nRaw Material Name: {self.stock_name_add.text()}\nQuantity: {self.stock_count_add.text()}"
            self.text_block1.setText(add_data)


        now = datetime.datetime.now()
        stock_call_add_date_time = now.strftime("%Y-%m-%d %H:%M")
        stock_name = self.stock_name_add.text().replace(' ', '_').lower()
        stock_val = int(self.stock_count_add.text())
        mp.update_quantity(stock_name, stock_val, stock_call_add_date_time)


        # Clear the input fields after processing the data
        self.stock_name_add.clear()
        self.stock_count_add.clear()


    def stack3UI(self):

        table = mp.show_stock()
        print('show')
        print(table)
        layout = QVBoxLayout()
        self.srb = QPushButton()
        self.srb.setText("Get Search Result.")
        self.View = QTableWidget()
        self.lbl3 = QLabel()
        self.lbl_conf_text = QLabel()
        self.lbl_conf_text.setText("Enter the search keyword:")
        self.conf_text = QLineEdit()

        self.View.setColumnCount(3)
        self.View.setColumnWidth(0, 400)
        self.View.setColumnWidth(1, 400)
        self.View.setColumnWidth(2, 400)
        self.View.insertRow(0)
        self.View.setItem(0, 0, QTableWidgetItem('Raw Material Name'))
        self.View.setItem(0, 1, QTableWidgetItem('Quantity'))
        self.View.setItem(0, 2, QTableWidgetItem('Cost(Per Unit)'))

        layout.addWidget(self.View)
        layout.addWidget(self.lbl_conf_text)
        layout.addWidget(self.conf_text)
        layout.addWidget(self.srb)
        layout.addWidget(self.lbl3)
        self.srb.clicked.connect(self.show_search)
        self.stack3.setLayout(layout)

    def show_search(self):
        if self.View.rowCount()>1:
            for i in range(1,self.View.rowCount()):
                self.View.removeRow(1)


        x_act = mp.show_stock()
        x = []
        if self.conf_text.text() != '':
            for i in range(0,len(x_act)):
                a = list(x_act[i])
                if self.conf_text.text().lower() in a[0].lower():
                    x.append(a)
        else:
            x = mp.show_stock()

        if len(x)!=0:
            for i in range(1,len(x)+1):
                self.View.insertRow(i)
                a = list(x[i-1])
                self.View.setItem(i, 0, QTableWidgetItem(a[0].replace('_',' ').upper()))
                self.View.setItem(i, 1, QTableWidgetItem(str(a[1])))
                self.View.setItem(i, 2, QTableWidgetItem(str(a[2])))
                self.View.setRowHeight(i, 50)
            self.lbl3.setText('Viewing Raw Material in Stock File.')
        else:
            self.lbl3.setText('No valid information in Stock File.')

    def stack4UI(self):
        layout = QVBoxLayout()
        self.srt = QPushButton()
        self.srt.setText("Get Transaction History.")
        self.Trans = QTableWidget()
        self.lbl4 = QLabel()
        self.lbl_trans_text = QLabel()
        self.lbl_trans_text.setText("Enter the search keyword:")
        self.trans_text = QLineEdit()


        self.Trans.setColumnCount(6)
        self.Trans.setColumnWidth(0, 150)
        self.Trans.setColumnWidth(1, 150)
        self.Trans.setColumnWidth(2, 150)
        self.Trans.setColumnWidth(3, 100)
        self.Trans.setColumnWidth(4, 100)
        self.Trans.setColumnWidth(5, 500)
        self.Trans.insertRow(0)
        self.Trans.setItem(0, 0, QTableWidgetItem('Transaction ID'))
        self.Trans.setItem(0, 1, QTableWidgetItem('Raw Material Name'))
        self.Trans.setItem(0, 2, QTableWidgetItem('Transaction Type'))
        self.Trans.setItem(0, 3, QTableWidgetItem('Date'))
        self.Trans.setItem(0, 4, QTableWidgetItem('Time'))
        self.Trans.setItem(0, 5, QTableWidgetItem('Transaction Specific'))
        self.Trans.setRowHeight(0, 50)

        layout.addWidget(self.Trans)
        layout.addWidget(self.lbl_trans_text)
        layout.addWidget(self.trans_text)
        layout.addWidget(self.srt)
        layout.addWidget(self.lbl4)
        self.srt.clicked.connect(self.show_trans_history)
        self.stack4.setLayout(layout)

    def show_trans_history(self):
        if self.Trans.rowCount() > 1:
            for i in range(1, self.Trans.rowCount()):
                self.Trans.removeRow(1)

        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'transaction.txt')
        if os.path.exists(path):
            with open(path, 'r') as tsearch:
                x_c = tsearch.readlines()

            x = []
            if self.trans_text.text() != '':
                key = self.trans_text.text()
                for line in x_c:
                    a = line.split(" ")
                    name = a[0]
                    action = a[-2]
                    if (key.lower() in name.lower()) or (key.lower() in action.lower()):
                        x.append(a)
            else:
                x = [line.split() for line in x_c]

            x.sort(key=lambda a: a[4])

            tid = 1900001
            for i, a in enumerate(x, 1):
                self.Trans.insertRow(i)
                if a[5] == 'ADD':
                    p = 'Quantity of Raw Material ADD ' + a[1] +' With Previous Quantity'
                elif a[5] == 'INSERT':
                    p = 'Raw Material added with Quantity: ' + a[1] + ' and Cost(Per Unit in Rs.): ' + a[2]
                elif a[5] == 'REDUCE':
                    p = 'Quantity of Raw Material REDUCE ' + a[1] +' With Previous Quantity'
                elif a[5] == 'REMOVE':
                    p = 'Raw Material information deleted.'
                else:
                    p = 'None'

                self.Trans.setItem(i, 0, QTableWidgetItem(str(tid)))
                self.Trans.setItem(i, 1, QTableWidgetItem(a[0].replace('_', ' ')))
                self.Trans.setItem(i, 2, QTableWidgetItem(a[5]))
                self.Trans.setItem(i, 3, QTableWidgetItem(a[3]))
                self.Trans.setItem(i, 4, QTableWidgetItem(a[4]))
                self.Trans.setItem(i, 5, QTableWidgetItem(p))
                self.Trans.setRowHeight(i, 50)
                tid += 1

            self.lbl4.setText('Transaction History.')
        else:
            self.lbl4.setText('No valid information found.')

    def display(self, i):
        self.Stack.setCurrentIndex(i)




if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Example()
    sys.exit(app.exec_())
