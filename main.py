import sys
import io
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        # abc = io.StringIO(template)
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.get_data)

    def get_data(self):
        with sqlite3.connect('coffee.sqlite') as file:
            cursor = file.cursor()
            query = """ SELECT * FROM Coffee """
            data = cursor.execute(query).fetchall()
            row = 0
            for i in data:
                # print(i)
                self.tableWidget.insertRow(row)
                for j in range(len(i)):
                    # print(data.index(i), j, i[j])
                    self.tableWidget.setItem(data.index(i), j, QTableWidgetItem(str(i[j])))
                row += 1



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())