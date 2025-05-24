from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTableView, QComboBox,
    QStyledItemDelegate, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton, QDialog
)
from PyQt5.QtCore import Qt, QStringListModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import sys

class WindowRecipe(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Добавить рецептуру")
        self.setMinimumSize(600, 800)

        self.layout_central = QVBoxLayout(self)

        # Верхние поля
        self.layout_top = QHBoxLayout()
        self.label_tops0 = QLabel("Наименование")
        self.line_edit0 = QLineEdit()
        self.label_tops1 = QLabel("Версия")
        self.line_edit1 = QLineEdit()

        self.layout_top.addWidget(self.label_tops0)
        self.layout_top.addWidget(self.line_edit0)
        self.layout_top.addWidget(self.label_tops1)
        self.layout_top.addWidget(self.line_edit1)

        self.layout_central.addLayout(self.layout_top)

        # Таблица
        self.table_view = QTableView()
        self.layout_central.addWidget(self.table_view)

        # Нижние кнопки
        self.layout_buttons = QHBoxLayout()
        self.button_add = QPushButton("Добавить компонент в рецептуру")
        self.button_save = QPushButton("Сохранить")

        self.layout_buttons.addWidget(self.button_add)
        self.layout_buttons.addWidget(self.button_save)

        self.layout_central.addLayout(self.layout_buttons)

        self.button_save.clicked.connect(self.accept)



class ComboBoxDelegate(QStyledItemDelegate):
    def __init__(self, items, parent=None):
        super().__init__(parent)
        self.items = items

    def createEditor(self, parent, option, index):
        combo = QComboBox(parent)
        combo.addItems(self.items)
        return combo

    def setEditorData(self, editor, index):
        value = index.data(Qt.DisplayRole)
        i = editor.findText(value)
        if i >= 0:
            editor.setCurrentIndex(i)

    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentText(), Qt.EditRole)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WindowRecipe()
    window.show()
    sys.exit(app.exec_())