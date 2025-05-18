import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QVBoxLayout, QWidget, QHBoxLayout,
    QStackedLayout, QTableView
)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Сырье, заявки, материалы")
        self.setMinimumSize(800, 800)

        # Кнопки
        self.buttons = []
        for i in range(7):
            btn = QPushButton()
            btn.setObjectName(f"button{i+1}")
            btn.clicked.connect(lambda checked, index=i: self.bottom_tab.setCurrentIndex(index))
            self.buttons.append(btn)

        # Макет интерфейса
        self.layout_window = QVBoxLayout()
        self.top_tab = QHBoxLayout()
        for btn in self.buttons:
            self.top_tab.addWidget(btn)
        self.layout_window.addLayout(self.top_tab)

        # Нижняя часть со стеком таблиц
        self.bottom_tab = QStackedLayout()
        self.table = []
        for i in range(6):
            table = QTableView()
            table.setObjectName(f"table{i + 1}")
            self.bottom_tab.addWidget(table)
        self.layout_window.addLayout(self.bottom_tab)

        # Центральный виджет
        self.centr_window = QWidget()
        self.centr_window.setLayout(self.layout_window)
        self.setCentralWidget(self.centr_window)

        # Названия кнопок
        self.name_object()

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
    app.exec()
    sys.exit(app.exec_())