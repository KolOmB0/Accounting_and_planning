import os
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QVBoxLayout, QWidget, QHBoxLayout,
    QStackedLayout, QTableView, QDialog, QVBoxLayout, QLineEdit, QDialogButtonBox, QApplication, QLabel, QCompleter,
    QComboBox, QGridLayout, QSizePolicy
)
from PyQt5.QtCore import Qt, QStringListModel
import Name_and_nomenclature
import dp_command
import recipe

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Сырье, заявки, материалы")
        self.setMinimumSize(800, 800)

        # Верхние кнопки для переключения страниц
        self.buttons = []
        self.top_tab = QHBoxLayout()
        for i in range(7):
            btn = QPushButton()
            btn.setObjectName(f"button{i+1}")
            btn.clicked.connect(lambda checked, index=i: self.set_current_tab(index))
            self.buttons.append(btn)
            self.top_tab.addWidget(btn)

        # Центральная часть — таблицы
        self.table_stack = QStackedLayout()
        self.table = []
        for i in range(7):
            table = QTableView()
            table.setObjectName(f"table{i + 1}")
            self.table_stack.addWidget(table)
            self.table.append(table)

        # Нижние кнопки (по 1 набору на каждую страницу)
        self.bottom_buttons_stack = QStackedLayout()
        for i in range(7):
            button_layout = QHBoxLayout()
            for j in range(2):
                if i == 5 and j==0:
                    layout_grid = QGridLayout()
                    self.label_stack6_recipe = QLabel("Наименование")
                    self.label_stack6_recipe.setAlignment(Qt.AlignRight)
                    self.label_stack6_recipe.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed))
                    self.combo_stack6_recipe = QComboBox()
                    self.label_stack6_version = QLabel("Рецептура № версий")
                    self.label_stack6_version.setAlignment(Qt.AlignRight)
                    self.label_stack6_version.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed))
                    self.combo_stack6_version = QComboBox()
                    layout_grid.addWidget(self.label_stack6_recipe, 0, 0)
                    layout_grid.addWidget(self.combo_stack6_recipe, 0, 1)
                    layout_grid.addWidget(self.label_stack6_version, 1, 0)
                    layout_grid.addWidget(self.combo_stack6_version, 1, 1)
                    button_layout.addLayout(layout_grid)
                    continue
                b = QPushButton()
                b.setObjectName(f"button{j+1}_in_tabl{i+1}")
                self.buttons.append(b)
                button_layout.addWidget(b)

            container_layout = QVBoxLayout()
            container_layout.addStretch()
            container_layout.addLayout(button_layout)  # Кнопки внизу

            container = QWidget()
            container.setLayout(container_layout)
            self.bottom_buttons_stack.addWidget(container)

        # Объединяем таблицы и нижние кнопки в вертикальный контейнер
        center_layout = QVBoxLayout()
        center_layout.addLayout(self.table_stack, stretch=1)
        center_layout.addLayout(self.bottom_buttons_stack)

        # Главный макет
        self.layout_window = QVBoxLayout()
        self.layout_window.addLayout(self.top_tab)
        self.layout_window.addLayout(center_layout)

        # Центральный виджет
        self.centr_window = QWidget()
        self.centr_window.setLayout(self.layout_window)
        self.setCentralWidget(self.centr_window)

        # Названия кнопок
        self.name_object()
        Name_and_nomenclature.NameAndNomenclature(self.table[4])

        # Обработка нажатие
        self.button1_in_5 = self.findChild(QPushButton, "button1_in_tabl5")
        self.button1_in_5.clicked.connect(lambda: self.append_bd(what_to_enter ="nomenclature"))
        self.button2_in_5 = self.findChild(QPushButton, "button2_in_tabl5")
        self.button2_in_5.clicked.connect(lambda: self.append_bd(what_to_enter="analogue"))
        self.button2_in_6 = self.findChild(QPushButton, "button2_in_tabl6")
        self.button2_in_6.clicked.connect(self.OpenWindowRecipe)
    def OpenWindowRecipe(self):
        dialog = recipe.WindowRecipe()
        result = dialog.exec_()
        if result == QDialog.Accepted:
            print("Диалог был закрыт с кодом Accepted")
    def append_bd(self,what_to_enter = None):
        existing_nomenclatures = Name_and_nomenclature.NameAndNomenclature.get_first_column()
        if what_to_enter == "nomenclature":
            dialog = NewDialogOnefield(existing_nomenclatures, "Новая номенклатура")
            if dialog.exec_() == QDialog.Accepted:
                new_name = self.normalize_text(dialog.get_text())
                dp_command.append_in_db(new_name,data = "nomenclature")
                Name_and_nomenclature.NameAndNomenclature(self.table[4])
        elif what_to_enter == "analogue":
            dialog = NewDialogTwofield(existing_nomenclatures,"Аналоги")
            if dialog.exec_() == QDialog.Accepted:
                tex_combo = dialog.get_selected()
                new_name = self.normalize_text(dialog.get_input())
                dp_command.append_in_db(new_name, data="analogue",check_date = tex_combo)
                Name_and_nomenclature.NameAndNomenclature(self.table[4])
        else:
            print("Пользователь отменил ввод")

    def normalize_text(self,text):
        words = text.strip().split()
        if not words:
            return ""
        # Склеиваем слова обратно через один пробел
        normalized = ' '.join(words)
        # Первая буква — заглавная, остальные — строчные
        return normalized[0].upper() + normalized[1:].lower()
    def set_current_tab(self, index):
        self.table_stack.setCurrentIndex(index)
        self.bottom_buttons_stack.setCurrentIndex(index)

    def name_object(self):
        name_button = {
            "button1": "Приказы/Планы",
            "button2": "Поставки из РФ",
            "button3": "Остатки по поставкам",
            "button4": "Расчет плана",
            "button5": "Наименование и номенклатура",
            "button6": "Рецептура",
            "button7": "Сводка",
            "button1_in_tabl5":"Добавить Наменклотуру",
            "button2_in_tabl5": "Добавить Аналог",
            "button2_in_tabl6": "Добавить Рецептуру"
        }
        for btn in self.buttons:
            name = btn.objectName()
            btn.setText(name_button.get(name, "имя не задано"))

class NewDialogOnefield(QDialog):
    def __init__(self, existing_items=None, WindowTitle=None,parent=None):
        super().__init__(parent)
        self.setWindowTitle(WindowTitle)
        self.layout = QVBoxLayout(self)
        self.label = QLabel("Ввод:")
        self.layout.addWidget(self.label)

        # Текстовое поле
        self.line_edit = QLineEdit(self)
        self.layout.addWidget(self.line_edit)

        # Автозаполнение по списку существующих номенклатур
        existing_items = existing_items or []
        completer = QCompleter(existing_items, self)
        completer.setCaseSensitivity(False)
        self.line_edit.setCompleter(completer)

        # Кнопки OK и Отмена
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.layout.addWidget(self.button_box)

        self.button_box.accepted.connect(self.accept)  # OK
        self.button_box.rejected.connect(self.reject)  # Отмена

    def get_text(self):
        return self.line_edit.text()
class NewDialogTwofield(QDialog):
    def __init__(self, existing_items=None, WindowTitle=None,parent=None,change=None):
        super().__init__(parent)
        self.setWindowTitle(WindowTitle)
        self.layout = QVBoxLayout(self)
        self.label0 = QLabel("Наменклотура")
        self.layout.addWidget(self.label0)
        self.combo_edit = QComboBox(self)
        existing_items = existing_items or []
        self.combo_edit.addItems(existing_items)
        self.layout.addWidget(self.combo_edit)
        self.label = QLabel("Ввод:")
        self.layout.addWidget(self.label)

        # Текстовое поле
        self.line_edit = QLineEdit(self)
        self.layout.addWidget(self.line_edit)

        # Кнопки OK и Отмена
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.layout.addWidget(self.button_box)

        self.button_box.accepted.connect(self.accept)  # OK
        self.button_box.rejected.connect(self.reject)  # Отмена

    def get_selected(self):
        return self.combo_edit.currentText()

    def get_input(self):
        return self.line_edit.text()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

