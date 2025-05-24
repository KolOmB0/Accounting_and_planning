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
                # Получаем текущие аналоги
                cursor.execute(f"""
                            SELECT * FROM Unique_nomenclature WHERE "Наменклатура" = ?
                        """, (check_date,))
                row = cursor.fetchone()
                if not row:
                    print("Ошибка: такой номенклатуры нет!")
                    conn.close()
                    return

                col_names = [desc[0] for desc in cursor.description]

                # Проверка — есть ли уже такой аналог
                if normalized in row:
                    print("Такой аналог уже существует!")
                    conn.close()
                    return
            # Ищем первый свободный столбец "Аналог_наменклатуры_N"
            analogue_cols = [name for name in col_names if name.startswith("Аналог_наменклатуры")]
            for col in analogue_cols:
                idx = col_names.index(col)
                if row[idx] in (None, '', 0):
                    cursor.execute(f"""
                                    UPDATE Unique_nomenclature
                                    SET "{col}" = ?
                                    WHERE "Наменклатура" = ?
                                """, (normalized, check_date))
                    conn.commit()
                    print(f"Аналог добавлен в столбец {col}.")
                    conn.close()
                    return
            # Все столбцы заняты — создаем новый столбец
            new_col_num = len(analogue_cols) + 1
            new_col_name = f"Аналог_наменклатуры_{new_col_num}"
            cursor.execute(f"""
                    ALTER TABLE Unique_nomenclature ADD COLUMN "{new_col_name}" TEXT
                """)
            cursor.execute(f"""
                    UPDATE Unique_nomenclature
                    SET "{new_col_name}" = ?
                    WHERE "Наменклатура" = ?
                """, (normalized, check_date))
            conn.commit()
            print(f"Добавлен новый столбец {new_col_name} и записан аналог.")
            conn.close()


    except sqlite3.IntegrityError:
        print("Такая номенклатура уже существует!")
    except Exception as e:
        print(f"Ошибка при добавлении в БД: {e}")

