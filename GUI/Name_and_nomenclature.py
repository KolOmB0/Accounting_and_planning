import sqlite3
from PyQt5.QtCore import QAbstractTableModel, Qt
from dp_command import db_path
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
        self.data, self.headers = self.load_from_db(db_path)
        self.model = NameAndNomenclatureModel(self.data, self.headers)
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

    @classmethod
    def get_first_column(cls, db_path=db_path):
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Unique_nomenclature")
            data = cursor.fetchall()
            conn.close()
            return [row[0] for row in data]
        except Exception as e:
            print(f"Ошибка при подключении к БД: {e}")
            return []

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


