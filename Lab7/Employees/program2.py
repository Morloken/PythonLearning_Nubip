import pandas as pd
from datetime import datetime
import os

def calculate_age(birth_date_str):
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
    today = datetime.today().date()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

def main():
    if not os.path.exists("employees.csv"):
        print("Повідомлення: Відсутній, або проблеми при відкритті файлу CSV.")
        return

    try:
        df = pd.read_csv("employees.csv", encoding="utf-8")
        
        # Рахуємо вік
        df['Вік'] = df['Дата народження'].apply(calculate_age)
        
        # Структура для вікових категорій: №, Прізвище, Ім’я, По батькові, Дата народження, Вік
        # Створюємо стовпець №
        df.insert(0, '№', range(1, len(df) + 1))
        
        columns_for_sheets = ['№', 'Прізвище', 'Ім’я', 'По батькові', 'Дата народження', 'Вік']
        
        # Розбиваємо на категорії
        df_younger_18 = df[df['Вік'] < 18][columns_for_sheets].copy()
        df_18_45 = df[(df['Вік'] >= 18) & (df['Вік'] <= 45)][columns_for_sheets].copy()
        df_45_70 = df[(df['Вік'] > 45) & (df['Вік'] <= 70)][columns_for_sheets].copy()
        df_older_70 = df[df['Вік'] > 70][columns_for_sheets].copy()

        # Запис у XLSX
        try:
            with pd.ExcelWriter("employees.xlsx", engine="openpyxl") as writer:
                # Аркуш "all" містить усі дані з CSV (без стовпця Вік і №)
                df.drop(columns=['Вік', '№']).to_excel(writer, sheet_name="all", index=False)
                
                df_younger_18.to_excel(writer, sheet_name="younger_18", index=False)
                df_18_45.to_excel(writer, sheet_name="18-45", index=False)
                df_45_70.to_excel(writer, sheet_name="45-70", index=False)
                df_older_70.to_excel(writer, sheet_name="older_70", index=False)
            print("Ok")
        except Exception:
            print("Повідомлення: Неможливість створення XLSX файлу.")
            
    except Exception:
        print("Повідомлення: Відсутній, або проблеми при відкритті файлу CSV.")

if __name__ == "__main__":
    main()