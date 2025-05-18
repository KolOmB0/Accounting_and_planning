from PyQt5.QtCore import QAbstractTableModel, Qt

class NameAndNomenclatureModel(QAbstractTableModel):
    def __init__(self, data=None):
        super().__init__()
        # data — список кортежей (Nomenclature, Analogs)
        self._data = data or []

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return 2  # два столбца: номенклатура и аналоги

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        headers = ["Номенклатура", "Аналоги"]
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                if 0 <= section < len(headers):
                    return headers[section]
        return None

class NameAndNomenclature:
    def __init__(self, table_view):
        # Здесь можно загрузить данные из БД, а пока — тестовые
        sample_data = [
            ("Номенклатура 1", "Аналог 1, Аналог 2"),
            ("Номенклатура 2", "Аналог A"),
            ("Номенклатура 3", ""),
        ]
        self.model = NameAndNomenclatureModel(sample_data)
        table_view.setModel(self.model)
        # Пример настройки таблицы
        table_view.resizeColumnsToContents()
        table_view.setAlternatingRowColors(True)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QWidget, QTableView, QApplication, QMainWindow
    app = QApplication(sys.argv)
    Main = QMainWindow()
    Tabl = QTableView()
    NameAndNomenclature(Tabl)
    Main.setCentralWidget(Tabl)
    Main.show()
    app.exec()
    sys.exit(app.exec_())
