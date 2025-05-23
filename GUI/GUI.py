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
            button_layout = QHBoxLayout()
            for j in range(2):  # Пример: 1 кнопка на вкладку
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
            "button7": "Сводка",
            "button1_in_tabl5":"Добавить Наменклотуру",
            "button2_in_tabl5": "Добавить Аналог"
        }
        for btn in self.buttons:
            name = btn.objectName()
            btn.setText(name_button.get(name, "имя не задано"))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

