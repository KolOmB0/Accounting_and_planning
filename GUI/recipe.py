class SimpleModel:
    def __init__(self):
        self._headers = ["Наменклатура", "Аналог_1", "Аналог_2"]

    def headerData(self, section, orientation, role):
        # Симулируем константы Qt (для простоты)
        DisplayRole = 0
        Horizontal = 1
        Vertical = 2

        if role == DisplayRole and orientation == Horizontal:
            if 0 <= section < len(self._headers):
                return self._headers[section]
        return None


model = SimpleModel()

# Псевдо-константы, чтобы проверить разные варианты
DisplayRole = 0
Horizontal = 1
Vertical = 2

print(model.headerData(0, Horizontal, DisplayRole))  # "Наменклатура"
print(model.headerData(1, Horizontal, DisplayRole))  # "Аналог_1"
print(model.headerData(2, Horizontal, DisplayRole))  # "Аналог_2"
print(model.headerData(3, Horizontal, DisplayRole))  # None, т.к. index 3 вне диапазона
print(model.headerData(0, Vertical, DisplayRole))    # None, вертикальная ориентация
print(model.headerData(0, Horizontal, 999))          # None, не DisplayRole
