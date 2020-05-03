import math
import sys
from PySide2 import QtWidgets
from PySide2.QtCore import Qt, Slot
from PySide2.QtWidgets import QApplication

from UI.MainWindow import Ui_MainWindow
from UI.Widget import Window
# ui to py: pyside2-uic "you_file.ui" -o "your_file.py"
# pyside2-lupdate main.pro
# pyinstaller -w icon=icon.ico –clean -n Main main.py

class LabOne(QtWidgets.QMainWindow, Ui_MainWindow):
    # Конструктор класса
    def __init__(self, parent=None):
        super().__init__(parent)
        # Создание формы и Ui (наш дизайн)
        self.setupUi(self)
        # Показать наше окно
        self.show()

        # LCDnumber starter
        self.lcdNumber.setDigitCount(3)
        self.digit = 0
        self.lcdNumber.display(self.digit)

        # Button pressed
        self.pushButton.clicked.connect(self.counterDigitUp)
        self.pushButton_2.clicked.connect(self.Quit)
        # self.pushButton_2.clicked.connect()
        # self.pushButton_3.clicked.connect()

        # RadiButton pressed
        self.radioButton.pressed.connect(self.switcher)
        self.radioButton_2.pressed.connect(self.switcher)
        self.radioButton_3.pressed.connect(self.switcher)
        self.radioButton_4.pressed.connect(self.menu)
        self.radioButton_5.pressed.connect(self.menu)

        #self.checkBox_4.setChecked(True)
        # self.checkBox.stateChanged.connect(self.switcher(self.checkBox))

    def counterDigitUp(self):
        if self.digit == 99:
            self.checkBox_4.setChecked(True)
        if self.digit == -99:
            self.checkBox_4.setChecked(False)

        #buttom = self.render()
        if self.checkBox_4.isChecked():
            self.digit -= 1
            self.lcdNumber.display(self.digit)
        else:
            self.digit += 1
            self.lcdNumber.display(self.digit)

    def switcher(self):
        radioButton = self.sender()
        # index = self.__cursorsButtons.index(radioButton)
        # print(index)
        if self.radioButton.isChecked():
            print("LOG_TAG: ", radioButton.text())
            self.setCursor(Qt.ArrowCursor)

        elif self.radioButton_2.isChecked():
            print("LOG_TAG: ", radioButton.text())
            self.setCursor(Qt.CrossCursor)

        elif self.radioButton_3.isChecked():
            print("LOG_TAG: ", radioButton.text())
            self.setCursor(Qt.PointingHandCursor)


    def Quit(self):
        QApplication.quit()

    def menu(self):
        if self.radioButton_4.isChecked():
            self.setWindowFlags(Qt.Window)

        elif self.radioButton_5.isChecked():
            self.setWindowFlags(Qt.FramelessWindowHint)

        self.show()


    # self.lineEdit.setText('0')
    # lineEdit - белое поле, в котором будут транслироваться все цифры и операции
    # text() - возвращает текст, который написан на нашей кнопке
    # setText() - кладет текст в объект от которого мы вызываем его
    # sender() - функция, которая возвращает отправителя сигнала (какая кнопка была нажата, от какой идет сигнал)
    # button.text() - текст кнопки

    # def on_digit_pressed(self):
    #     button = self.sender()
    #     if self.lineEdit.text() == '0':
    #         # Если у нас в нашем поле результата "0", то заменяем его на текст, который написан на кнопке
    #         self.lineEdit.setText(button.text())
    #     else:
    #         if self.result == self.lineEdit.text():
    #             self.lineEdit.setText(button.text())
    #         else:
    #             self.lineEdit.setText(self.lineEdit.text() + button.text())
    #     self.result = 0

    # clear() - отчищает строку, которую от которой мы его вызываем
    # str(object) - делает из int > str
    # float(object) - делает float num.num
    # int(object) - делает integer

if __name__ == '__main__':
    # Новый экземпляр QApplication
    app = QtWidgets.QApplication(sys.argv)
    # Сздание инстанса класса LabOne, который мы создадим далее
    lab = LabOne()
    # Запуск
    sys.exit(app.exec_())