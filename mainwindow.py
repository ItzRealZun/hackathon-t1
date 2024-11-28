# This Python file uses the following encoding: utf-8
import sys
import pandas as pd

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    flag = False
    path = ""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.openPathButton.clicked.connect(self.open_filemanager)
        self.ui.createGoldenRecordButton.clicked.connect(self.create_golden_record)
        self.show()


    def open_filemanager(self):
        MainWindow.path, _ = QFileDialog.getOpenFileName(self, "Выберите файл формата csv", "", "Таблицы (*.csv)")
        if MainWindow.path:
            self.ui.pathLine.setText(f"{MainWindow.path}")
            MainWindow.flag = True


    def create_golden_record(self):
        if MainWindow.flag:
            successBox = QMessageBox()
            successBox.setText("Какая-то обработка...")
            successBox.exec()
        else:
            alertBox = QMessageBox()
            alertBox.setText("Не выбран csv файл для обработки!")
            alertBox.exec()


    def manipulate(self):
        df = pd.read_csv(MainWindow.path, low_memory=False)
        df.drop_duplicates()
        df = df.drop(df[df["client_last_name"].astype(str) + " " + df["client_first_name"].astype(str) + " " + df["client_middle_name"].astype(str) != df["client_fio_full"].astype(str)].index)
        df = df.loc[(df['client_bday'] >= '1900-01-01')]
        df = df.loc[(df['client_gender'] == 'М') | (df['client_gender'] == 'Ж')]
        df = df.loc[(df['create_date'] <= df['update_date'])]
        df = df.loc[(df['contact_email'].str.match(r'[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+')) | (df['contact_email'].isnull())]
        df = df.loc[(df['contact_phone'].str.match('\+7 \d{3} \d{3} \d{4}')) | (df['contact_phone'].isnull())]
        df['client_snils'] = df['client_snils'].astype(str)
        df = df.loc[(df['client_snils'].str.match(r'\d{11}')) | (df['client_snils'].str.match('nan'))]
        df['client_inn'] = df['client_inn'].astype(str)
        df = df.loc[(df['client_inn'].str.match(r'\d{12}')) | (df['client_inn'].str.match('nan'))]
        df.to_csv('./manipulated.csv', encoding="utf-8")
        alertBox = QMessageBox()
        alertBox.setText("Файл обработан и результат выведен в файл manipulated.csv")
        alertBox.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())





