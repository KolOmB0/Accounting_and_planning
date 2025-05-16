from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пример dumpObjectInfo")

        # Создаем кнопку
        btn = QPushButton("Нажми меня", self)

        # Компоновка
        layout = QVBoxLayout(self)
        layout.addWidget(btn)

        # Вывести информацию об объекте и его иерархии
        self.dumpObjectInfo()
        self.dumpObjectTree()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())