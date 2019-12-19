import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from win.mainwin import Ui_VishListDialog
from model.vlist import VListModel


class MainWindow(QtWidgets.QDialog):
    '''Окно обновления данных товара (Наименования, цены, ссылки, примечания)
    Данное окно запускается с главного окнa программы, где находятся список товаров (ListView), функции создания и
    добавления INSERT в базу данных товара, Принимает в конструктор id редактируемого товара'''
    def __init__(self, id_obj):
        super().__init__()
        self.ui = Ui_VishListDialog()
        self.ui.setupUi(self)
        self.model = VListModel(id_obj)
        if not self.model.db_config:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Нет данных для подключения к БД", defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            self.ui.nameEdit, self.ui.priceBox, self.ui.linkEdit, self.ui.commentEdit = self.model.data
        self.ui.CancelButton.clicked.connect(self.close)
        self.ui.SaveButton.clicked.connect(self.save_data)

    def save_data(self):
        self.model.data = self.ui.nameEdit, self.ui.priceBox, self.ui.linkEdit, self.ui.commentEdit
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
