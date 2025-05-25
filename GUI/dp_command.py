import os
import sqlite3

# Получаем абсолютный путь к папке, где находится скрипт
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Склеиваем путь к папке BD и файлу BD_authentic.db
db_path = os.path.join(base_dir, "BD", "BD_authentic.db")


def append_in_db(input_date = None, db_path=db_path, data = None, check_date = None):
    try:
            normalized = ' '.join(input_date.strip().split()).capitalize()

            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            if data == "nomenclature":
                cursor.execute("""
                            INSERT INTO Unique_nomenclature ("Наменклатура")
                            VALUES (?)
                        """, (normalized,))
                conn.commit()
                print("Новая номенклатура успешно добавлена.")

            elif data == "analogue" and check_date:
                cursor.execute("""SELECT Наменклатура, Вариант_номенклатуры  FROM Unique_nomenclature, Nomenclature_Variants  """)
                data_bd = cursor.fetchall()
                data_bd = [rows[0],  for rows in data_bd]


            conn.commit()
            conn.close()


    except sqlite3.IntegrityError:
        print("Такая номенклатура уже существует!")
    except Exception as e:
        print(f"Ошибка при добавлении в БД: {e}")

