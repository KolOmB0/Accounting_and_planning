import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QVBoxLayout, QWidget, QHBoxLayout,
    QStackedLayout, QTableView
)
from PyQt5.QtCore import Qt
import Name_and_nomenclature

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
            layout = QHBoxLayout()
            container = QWidget()
            container.setLayout(layout)
            for j in range(3):  # Пример: 3 кнопки на вкладку
                b = QPushButton(f"Кнопка {j+1} для вкладки {i+1}")
                b.setObjectName(f"button{i+1}_in_tabl{i+1}")
                layout.addWidget(b)
            self.bottom_buttons_stack.addWidget(container)

        # Главный макет
        self.layout_window = QVBoxLayout()
        self.layout_window.addLayout(self.top_tab)
        self.layout_window.addLayout(self.table_stack)
        self.layout_window.addLayout(self.bottom_buttons_stack)

        # Центральный виджет
        self.centr_window = QWidget()
        self.centr_window.setLayout(self.layout_window)
        self.setCentralWidget(self.centr_window)

        # Заполнение таблиц
        Name_and_nomenclature.NameAndNomenclature(self.table[4])

        # Названия кнопок
        self.name_object()

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
            "button7": "Сводка"
        }
        for btn in self.buttons:
            name = btn.objectName()
            btn.setText(name_button.get(name, "имя не задано"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())