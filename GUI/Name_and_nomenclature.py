import sqlite3
from PyQt5.QtCore import QAbstractTableModel, Qt

class NameAndNomenclatureModel(QAbstractTableModel):
    def __init__(self, data=None, headers=None):
        super().__init__()
        self._data = data or []
        self._headers = headers or []

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._headers)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if 0 <= section < len(self._headers):
                return self._headers[section]
        return None

class NameAndNomenclature:
    def __init__(self, table_view):
        data, headers = self.load_from_db("C:\\Users\\User\\Project\\Accounting_and_planning\\BD\\BD_authentic.db")
        self.model = NameAndNomenclatureModel(data, headers)
        table_view.setModel(self.model)
        table_view.resizeColumnsToContents()
        table_view.setAlternatingRowColors(True)

    def load_from_db(self, db_path):
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Получаем названия колонок
            cursor.execute("PRAGMA table_info(Unique_nomenclature)")
            headers = [info[1] for info in cursor.fetchall()]

            cursor.execute(f"SELECT * FROM Unique_nomenclature")
            data = cursor.fetchall()

            conn.close()
            return data, headers
        except Exception as e:
            print(f"Ошибка при подключении к БД: {e}")
            return [], []

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QTableView, QApplication, QMainWindow
    app = QApplication(sys.argv)
    Main = QMainWindow()
    Tabl = QTableView()
    NameAndNomenclature(Tabl)
    Main.setCentralWidget(Tabl)
    Main.show()
    sys.exit(app.exec_())


