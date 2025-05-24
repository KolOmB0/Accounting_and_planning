from PyQt5.QtWidgets import (
    QApplication, QDialog, QLabel, QPushButton, QVBoxLayout, QMainWindow, QWidget
)
import sys


# Модальное окно
class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Модальное окно")
        self.setMinimumSize(300, 100)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Это модальное окно"))

        # Кнопка закрытия
        close_button = QPushButton("Закрыть")
        close_button.clicked.connect(self.accept)  # Закрыть с кодом Accepted
        layout.addWidget(close_button)

        self.setLayout(layout)


# Главное окно
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Главное окно")
        self.setMinimumSize(400, 200)

        self.button = QPushButton("Открыть модальное окно")
        self.button.clicked.connect(self.show_modal_dialog)

        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        container.setLayout(layout)
        self.setCentralWidget(container)

    def show_modal_dialog(self):
        dialog = MyDialog()
        result = dialog.exec_()  # модальное открытие
        if result == QDialog.Accepted:
            print("Диалог был закрыт с кодом Accepted")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

