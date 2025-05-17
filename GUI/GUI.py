import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow, QPushButton,QVBoxLayout,QWidget,QHBoxLayout,
                             QStackedLayout, QTableView)
from PyQt5.Qt import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        # Основные обекты интерфейса
        super().__init__()
        self.setWindowTitle("Сырье,заявки,материалы")
        self.setFixedSize(800,800)
        self.button1 = QPushButton()
        self.button1.setObjectName("button1")
        self.button2 = QPushButton()
        self.button2.setObjectName("button2")
        self.button3 = QPushButton()
        self.button3.setObjectName("button3")
        self.button4 = QPushButton()
        self.button4.setObjectName("button4")
        self.button5 = QPushButton()
        self.button5.setObjectName("button5")
        self.button6 = QPushButton()
        self.button6.setObjectName("button6")
        # Макет интерфейса
        self.layout_window = QVBoxLayout()
        self.top_tab = QHBoxLayout()
        self.top_tab.addWidget(self.button1)
        self.top_tab.addWidget(self.button2)
        self.top_tab.addWidget(self.button3)
        self.top_tab.addWidget(self.button4)
        self.top_tab.addWidget(self.button5)
        self.top_tab.addWidget(self.button6)
        self.layout_window.addLayout(self.top_tab)
        self.bottom_tab = QStackedLayout()
        self.tabl_vidget1 = QTableView()
        self.tabl_vidget2 = QTableView()
        self.tabl_vidget3 = QTableView()
        self.tabl_vidget4 = QTableView()
        self.tabl_vidget5 = QTableView()
        self.tabl_vidget6 = QTableView()
        self.bottom_tab.addWidget(self.tabl_vidget1)
        self.bottom_tab.addWidget(self.tabl_vidget2)
        self.bottom_tab.addWidget(self.tabl_vidget3)
        self.bottom_tab.addWidget(self.tabl_vidget4)
        self.bottom_tab.addWidget(self.tabl_vidget5)
        self.bottom_tab.addWidget(self.tabl_vidget6)
        self.layout_window.addLayout(self.bottom_tab)
        self.centr_window = QWidget()
        self.centr_window.setLayout(self.layout_window)
        self.setCentralWidget(self.centr_window)



        self.name_object()
    def name_object(self):
        name_button = {
            "button1": "Рецептуры",
            "button2": "Наименование сырья 1С/Рецептур",
            "button3": "Заявки обшая выработка по приказам",
            "button4": "Наименование сырья Приказы",
            "button5": "Задолжность РФ",
            "button6": "Актуальность сырья и материалов по планам",
        }

        for btn in self.findChildren(QPushButton):
            btn_name = btn.objectName()
            if btn_name in name_button:
                btn.setText(name_button[btn_name])
            else:
                btn.setText("имя не заданно")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    sys.exit(app.exec_())